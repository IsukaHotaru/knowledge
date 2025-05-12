'''dotenv'''

from dotenv import load_dotenv, find_dotenv, dotenv_values
import os

# dotenv 是用于从.env文件加载环境变量的工具, 常用于管理不同环境 (如开发
# 测试, 生产等) 的配置.

# 安装方法:
# pip install -U python-dotenv

# 优点:
#   - 环境变量管理: 通过将配置信息 (如数据库连接, API密钥) 存储在.env文件中, 
#     避免硬编码.
#   - 多环境支持: 通过不同的.env文件 (如.env.development, .env.production)
#     管理不同环境配置.

# .env文件
#   - 每行一个键值对, 格式为KEY=VALUE.
#   - 变量也可以没有值
#   - 如果在VALUE中使用变量, 需要通过${VARIABLE_NAME}格式书写
#   - 使用"#"添加注释
#       DB_HOST=localhost
#       DB_PORT=5432
#       EMAIL=admin@${DOMAIN}
#   - 对于带有锚点的url, 其中的#会被解析为注释, 因此需要用双引号/单引号括起来
#   √ .env文件通常包含敏感信息, 为避免泄漏信息, 不要将.env文件提交到版本控制
#     系统中 (如Git). 可以在项目根目录下创建一个.gitignore文件并添加.env解决.
#   √ 建议为不同环境创建独立的.env文件
#   √ 结合加密工具 (如sops) 或环境变量传递敏感信息.

# 主要函数:
# load_dotenv, find_dotenv, dotenv_values

# load_dotenv:
#   功能: 加载.env文件中的环境变量到当前进程的环境变量中
#   dotenv_path=".env": 指定.env文件路径, 默认为None, 当为None时会自动调用
#                find_env()查找文件位置. 如果文件名不为.env则必须传递该参数.
#   override=False: 当.env文件中有变量与系统中原来的环境变量冲突时, 默认使用系统变量,
#             若置值为True, 则临时使用.env中的变量值
#   encoding="utf-8": 指定文件的编码方式
#   stream: 通过流的方式传入配置文件
#       from io import StringIO
#       config = StringIO("USER=foo\nEMAIL=foo@example.org")
#       load_dotenv(stream=config)
#
# 注意要点:
#   - load_dotenv函数默认不会更新配置项, 也就是在调用load_dotenv后, 用户再更新
#     .env文件中配置项时, load_dotenv不会生效, 原因时load_dotenv默认不会更新
#     已经存在的配置项. 可使用override=True解决.

# find_dotenv
#   功能: 自动查找.env文件, 返回找到的文件路径
#   filename=".env": 指定要查找的文件名
#   usecwd=True: 如果设置为True, 则从当前工作目录开始查找.
#   raise_error_if_not_found=False: 如果设置为True, 则在没有找到文件时抛出异常

# dotenv_values
#   功能: 以字典形式返回配置文件中所有信息
#   dotenv_path=".env": 指定.env文件的路径
#   encoding="utf-8": 指定文件的编码格式

# 访问环境变量方法:
#   - 使用os模块访问环境变量
#       # 加载.env文件
#       load_dotenv()
#       # 访问环境变量
#       os.getenv("{VARIABLE_NAME}")
#       # 或者
#       # os.environ.get["{VARIABLE_NAME}"]