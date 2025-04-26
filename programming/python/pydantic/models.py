from pydantic import BaseModel, ConfigDict, ValidationError

class User(BaseModel):
    # 小心字段名称与类型名称相同
    id: int
    name: str = "Jane Doe"

    # ConfigDict用于控制pydantic的行为
    model_config = ConfigDict(str_max_length=10)

# try:
#     u = User(id=1, name="hello world!")
# except ValidationError as e:
#     print(e)

user = User(id="123")
# models的字段可以通过访问正常元素的方式访问
assert user.name == "Jane Doe"
assert user.id == 123
assert isinstance(user.id, int)

# 模型实例可通过model_dump()方法序列化(字典)
assert user.model_dump() == {"id": 123, "name": "Jane Doe"}

# 对于传参中的额外数据, pydantic默认忽视
# 可以使用extra配置字段控制行为
class Model(BaseModel):
    x: int
    # extra="forbid"时禁止额外传参
    model_config = ConfigDict(extra="allow")

m = Model(x=1, y="a")
assert m.model_dump() == {"x": 1, "y": "a"}
assert m.__pydantic_extra__ == {"y":"a"}

# 当欲图定义包含尚未构建的注解类型的类时, 
# 可以使用model_rebuild()来规避
from typing import List, Optional
from pydantic import PydanticUserError


class Foo(BaseModel):
    x: "Bar"

try:
    Foo.model_json_schema()
except PydanticUserError as e:
    print(e)

class Bar(BaseModel):
    pass

Foo.model_rebuild()
# classname.mode_json_schema()将元数据序列化
print(Foo.model_json_schema())

# 通过普通类实例来构建响应pydantic类实例
# 使用classname.model_validate(object)实现
from typing import Annotated
from sqlalchemy import ARRAY, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import StringConstraints

class Base(DeclarativeBase):
    pass

class CompanyOrm(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    public_key: Mapped[str] = mapped_column(
        String(20), index=True, nullable=False, unique=True
    )
    domains: Mapped[list[str]] = mapped_column(ARRAY(String(255)))

class CompanyModel(BaseModel):
    # 设置从对象的属性中提取数据, 不必传入字典
    # 用于之后的model_validate()
    model_config = ConfigDict(from_attributes=True)

    id: int
    public_key: Annotated[str, StringConstraints(max_length=20)]
    domains: list[Annotated[str, StringConstraints(max_length=255)]]

co_orm = CompanyOrm(
    id=123,
    public_key="foobar",
    domains=["example.com", "foobar.com"],
)

print(co_orm)
# 这里实现转换
co_model = CompanyModel.model_validate(co_orm)
print(co_model)

# 使用通过属性解析model时, 可以读取各层次嵌套数据

class PetCls:
    def __init__(self, *, name: str, species: str):
        self.name = name
        self.species = species

class PersonCls:
    def __init__(self, *, name: str, age: float = None, pets: list[PetCls]):
        self.name = name
        self.age = age
        self.pets = pets

class Pet(BaseModel):
    # revalidate_instances: 防止验证通过后又篡改实例使得绕过验证
    # 例: m = Model(a=0)
    # m.a = "not an int"
    # m2 = Model.model_validate(m) 如果上述选项为false, 则该条语句仍成立
    model_config = ConfigDict(from_attributes=True, revalidate_instances=True)

    name: str
    species: str

class Person(BaseModel):
    # 设置从对象的属性中提取数据, 不必传入字典
    # 用于model_validate()
    model_config = ConfigDict(from_attributes=True)

    name: str
    age: float = None
    pets: list[Pet]

bones = PetCls(name="Bones", species="dog")
orion = PetCls(name="Orion", species="cat")
anna = PersonCls(name="Anna", age=20, pets=[bones, orion])
anna_model = Person.model_validate(anna)
print(anna_model)

# 异常处理
class Model(BaseModel):
    list_of_ints: list[int]
    a_float: float

data = dict(
    list_of_ints=["1", "2", "bad"],
    a_float = "not a float",
)

try:
    Model(**data)
# 发现验证不匹配时, 抛出ValidationError
except ValidationError as e:
    print(e)

# 验证数据的方法
# model_validate() 参数使用字典或对象
# model_validate_json() 参数使用json格式
# model_validate_strings() 参数使用JSON格式, 但是键值对都是string类型

from datetime import datetime

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Optional[datetime] = None

m = User.model_validate({"id": 123, "name": "James"})
print(m)

try:
    User.model_validate(["not", "a", "dict"])
except ValidationError as e:
    print(e)

m = User.model_validate_json("{'id': 123, 'name': 'James'}")
print(m)

try:
    m = User.model_validate_json("{'id': 123, 'name': 123}")
except ValidationError as e:
    print(e)

m = User.model_validate_strings({"id": "123", "name": "James"})
print(m)

m = User.model_validate_strings(
    {"id": "123", "name": "James", "signup_ts": "2024-04-01T12:00:00"}
)
print(m)

try:
    m = User.model_validate_strings(
        {"id": "123", "name": "James", "singup_ts": "2024-04-01"}, strict=True
    )
except ValidationError as e:
    print(e)


# 使用model_construct(), 不用validate也能构造pydantic实例
# 场景: 已知通过验证的复杂数据, 验证函数不幂等, 验证函数有副作用等等

# generic models(泛化模型)
from typing import Generic, TypeVar

DataT = TypeVar("DataT")

class DataModel(BaseModel):
    number: int

class Response(BaseModel, Generic[DataT]):
    data: DataT

print(Response[int](data=1))
print(Response[str](data="value"))
print(Response[str](data="value").model_dump())

data = DataModel(number=1)
print(Response[DataModel](data=data).model_dump())
try:
    Response[int](data="value")
except ValidationError as e:
    print(e)

# 泛型model的子类也必须时泛型, 也就是必须继承Generic
TypeX = TypeVar("TypeX")

class BaseClass(BaseModel, Generic[TypeX]):
    X: TypeX

class ChildClass(BaseClass[TypeX], Generic[TypeX]):
    pass

print(ChildClass[int](X=1))

# 子类也可以部分或者全部替换父类中的类型变量
TypeX = TypeVar("TypeX")
TypeY = TypeVar("TypeY")
TypeZ = TypeVar("TypeZ")

class BaseClass(BaseModel, Generic[TypeX, TypeY]):
    x: TypeX
    y: TypeY

class ChildClass(BaseClass[int, TypeY], Generic[TypeY, TypeZ]):
    z: TypeZ

print(ChildClass[str, int](x="1", y="y", z="3"))

# 未参数化类型变量与已参数化类型变量
from typing_extensions import TypeVar
T = TypeVar("T")
U = TypeVar("U", bound=int)
V = TypeVar("V", default=str)

class Model(BaseModel, Generic[T, U, V]):
    t: T
    u: U
    v: V

print(Model(t="t", u=1, v="v"))

try:
    Model(t="t", u="u", v=1)
except ValidationError as exc:
    print(exc)

# 动态创建model
from pydantic import create_model

# 等价于
# class StaticFoobarModel(BaseModel):
#   foo: str
#   bar: int = 123
DynamicFoobarModel = create_model("DynamicFoobarModel", foo=str, bar=(int, 123))

# 进阶案例
from pydantic import Field, PrivateAttr

DynamicModel = create_model(
    "DynamicModel",
    foo=(str, Field(alias="FOO")),
    bar=Annotated[str, Field(description="Bar field")],
    _private=(int, PrivateAttr(default=1))
)

class StaticModel(BaseModel):
    foo: str = Field(alias="FOO")
    bar: Annotated[str, Field(description="Bar field")]
    _private: int = PrivateAttr(default=1)
