'''logging'''

import logging

# logging 是标准库中用于记录日志的工具

# 预备知识:
#
#   日志级别从低到高分为:
#       1 DEBUG: 调试信息 (最低级别)
#           - 调试时记录最详细日志信息, 在问题诊断时有用
#       2 INFO: 一般信息
#           - 记录一些设置的关键信息节点
#       3 WARNING: 警告信息
#           - 记录程序正常但不期望的事情发生时的信息 (如磁盘可用空间较少, 模块版本过低)
#       4 ERROR: 错误信息
#           - 记录由于错误导致软件无法执行某些功能时的信息
#       5 CRITICAL: 严重错误 (最高级别)
#           - 记录由于严重错误导致软件无法继续运行的信息
#   日志级别可通过logging.{logging_level}访问

# 主要组件:
#
#   1 Loggers: 日志记录器, 负责暴露接口供应用程序记录日志
#       使用方法:
#           - 使用默认logger输出日志 (名为root的logger)
#               logging.error("{error_message}")              
#           - 注册名为{Logger Name}的日志记录器
#               logger = logging.getLogger("{logger_name}")
#           - 设置logger可记录的最低日志等级
#               logger.setLevel(logging.DEBUG)
#           - 以该logger记录一条日志
#               logger.error("{error_information}")
#           - 使用exception方法输出日志 (与ERROR同级)
#               # exception除了输出错误的异常信息, 还会显示具体的错误堆栈信息
#               # logger.exception = logger.error("{message}", exc_info=True)
#               logger.exception("{exception_message}")
#           √ 使用结构化日志, 通过字典传递日志信息, 便于分析
#               logger.info("User login", 
#                            extra={'username': 'alice', 'status': 'success'})

#   2 Handlers: 处理器, 决定将日志记录发送到何处 (包括控制台, 文件等)
#       常用类型:
#           - StreamHandler: 输出到流 (如控制台)
#           - FileHandler: 输出到文件
#           - RotatingFileHandler: 按文件大小滚动日志
#           - TimeRotatingFileHandler: 按时间滚动日志
#           ! 使用后两种类型时需要从logging.handlers中import对应类型
#
#       使用方法:
#           - 设置将日志输出到指定文件名的handler
#               handler = logging.FileHandler("{file_name}")
#           - 设置将日志输出到指定流的handler, 若参数为None则默认输出到sys.stderr
#               handler = logging.StreamHandler(stream=None)
#           - 将handler添加到指定logger
#               logger.addHandler(handler)
#           - 设置handler可记录的最低日志等级
#               handler.setLevel(logging.DEBUG)

#   3 Formatters: 格式化器, 定义日志记录的格式
#       关键参数:
#           - fmt: 定义整个日志输出的格式字符串
#           - datefmt: 定义日志输出中日期/时间部分的格式字符串
#           - style: 定义格式字符串的风格, 可以是"%" (默认), "{"或"$"
#
#       常见格式化占位符:
#           - %(asctime)s: 日志消息的时间戳
#           - %(levelname)s: 日志级别
#           - %(name)s: logger的名称
#           - %(message)s: 日志内容
#           - %(filename)s: 生成日志的文件名
#           - %(funcName)s: 生成日志的函数名称
#           - %(lineno)d: 日志行所在的行号
#
#       常见时间戳显示格式:
#           - "%Y-%m-%d %H:%M:%S" (默认)
#
#       使用方法:
#           - 创建Formatter对象定义日志输出格式
#               formatter = logging.Formatter(
#                   fmt = """%(asctime)s - %(name)s - 
#                         %(levelname)s - %(message)s""",
#                   datefmt = "%Y-%m-%d %H:%M:%S")
#           - 将formatter应用于handler
#               handler.setFormatter(formatter)

#   4 Filters: 过滤器, 决定哪些记录应该被处理
#       使用方法:
#           - 创建自定义过滤器类
#               class MyFilter(logging.Filter):
#                   def filter(self, record):
#                       # 此处编写过滤逻辑
#                       # 返回True表示允许通过, False表示不允许
#                       # 例如只允许WARNING以上级别消息通过
#                       return record.levelno >= logging.WARNING
#           - 添加filter到handler
#               filter = MyFilter()
#               handler.addFilter(filter)

#   5 Configs: 配置方法, 决定日志系统的记录器的配置
#       √ 在程序启动时尽早配置日志, 避免日志信息丢失
#       √ 使用配置文件或字典管理日志, 避免硬编码
#
#       常用类型:
#           - basicConfig
#               参数详解:
#               filename: 指定使用的指定文件名 (与FileHandler配合)
#               filemode: 以("r", "w", "a"(默认))模式打开文件
#               format: 为处理程序使用指定的格式字符串
#               datefmt: 指定时间戳的格式字符串
#               style: 定义格式字符串的风格
#               level: 设置logger的最低记录级别 (默认WARNING)
#               stream: 使用指定的流初始化StreamHandler (与filename冲突)
#               handlers: 任何没有格式化程序的处理程序都将被分配给该handler处理
#                         (与filename和stream冲突)
#           - dictConfig
#               使用方法:
#               ! 需要import logging.config
#               - 传入字典配置文件
#                   LOGGING_CONFIG = {
#                       # version - 表示版本, 从1开始的整数, 该key必选, 其余可选
#                       "version": 1,
#                       # formatters - 日志格式化器, 其value值为一个字典, 字典的
#                                      每个键值对都代表一个formatter
#                       "formatters": {
#                           "default": {
#                               "format": "%(asctime)s -  %(message)s",
#                           },
#                           "plain": {
#                               "format": "%(message)s",
#                           },
#                       },
#                       # handlers - 日志处理器, 同formatters
#                       "handlers": {
#                           "console": {
#                               "class": "logging.StreamHandler",
#                               "level": "INFO",
#                               "formatter": "default",
#                           },
#                           "console_plain": {
#                               "class": "logging.StreamHandler",
#                               "level": logging.INFO
#                               "formatter": "plain",
#                           },
#                           "file": {
#                               "class": "logging.FileHandler",
#                               "level": 20,
#                               "filename": "./log.txt",
#                               "formatter": "default",
#                           },
#                       },
#                       # loggers - 同formatters
#                       "loggers": {
#                           "console_logger": {
#                               "handlers": ["console"],
#                               "level": "INFO",
#                               "propagate": False,
#                           },
#                           "console_plain_logger": {
#                               "handlers": ["console_plain"],
#                               "level": "DEBUG",
#                               "propagate": False,
#                           },
#                           "file_logger": {
#                               "handlers": ["file"],
#                               "level": "INFO",
#                               "propagate": False,
#                           },
#                       },
#                       "disable_existing_loggers": True
#                       # root - 默认logger
#                       "root": {
#                           # 遇到handler与logger的注册level不同, 取最高的一个
#                           "handlers": ["console"]
#                           "level": "DEBUG",
#                       },
#                   },
#                   # 注册loggers
#                   config.dictConfig(LOGGING_CONFIG)
#                   # 使用其中的logge
#                   logger = logging.getLogger("console_logger")
#                   logger.info("debug message")
#                   logger = logging.getLogger(root)
#                   logger.error("error message")

# 更多最佳实践
#   √ 避免记录敏感信息
#   √ 使用dictConfig等配置文件注册logger
#   √ 按模块定义logger, 每个模块使用独立的logger, 并以该模块命名
#   √ 合理设置日志轮转, 避免日志文件过大