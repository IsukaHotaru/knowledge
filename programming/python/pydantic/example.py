from datetime import datetime
from pydantic import BaseModel, PositiveInt

class User(BaseModel):
    # int表示将id属性强制约束为int类型, 其他类型如String, bytes, floats
    # 可以转换, 但是无法转换的类型会抛出异常
    id: int
    # 可以为name指派默认值
    name: str = "John Doe"
    signup_ts: datetime | None
    # tastes是一个字典. 值被限制为PositiveInt,
    # 等价于Annotated[int, annotated_types.Gt(0)]
    tastes: dict[str, PositiveInt]

external_data = {
    "id": 123,
    # 此处采用ISO 8601格式, 但pydantic会自动转换为datetime对象
    "signup_ts": "2025-04-26 17:55",
    "tastes": {
        "wine": 9,
        # b表示bytes, pydantic会自动将其转换为字符串
        b"cheese": 7,
        # pydantic会自动把字符串"1"转换为数字1
        "cabbage": "1",
    },
}

user = User(**external_data)

print(user.id)
# model_dump方法将对象转换为字典
print(user.model_dump())

# 如果User(**external_data)出错, 可通过实现更稳健的验证
from pydantic import ValidationError

external_data = {"id": "not an int", "taste": {}}

try:
    User(**external_data)
except ValidationError as e:
    print(e.errors())