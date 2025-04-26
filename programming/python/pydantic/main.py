'''pydantic'''

# pydantic是基于类型注解(type annotation)的数据验证库

# Models
# 实现模式定义的最主要方法是通过Models, Models是继承BaseModel且通过
# 属性注解来定义字段的的子类. 可以理解为C中的结构体.
# pydantic可以通过models来验证数据的有效性

# 在pydantic中, validation指初始化服从特定类型与约束的model(或其他类型)
# 这意味着数据类型的转换也可以视为一种validation, 从而允许改变数据类型而
# 不改变原数据.