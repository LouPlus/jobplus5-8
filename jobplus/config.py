class BaseConfig(object):
    SECRET_KEY = 'IAMAGOODMAN'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/jobplus5-8?charset=utf8' ## 指定连接的字符串,无法决定数据库的编码格式
    SQLALCHEMY_ECHO = True
    ADMIN_PER_PAGE = 10


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass

configs = {
    'development': DevelopmentConfig, # 开发是第一个环境
    'testing': TestingConfig, # 测试是检测开发的环境
    'production': ProductionConfig,
}


