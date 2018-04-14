import os
import yaml

# 配置文件, 使用yaml, 在根目录下建立 env文件夹,创建.yml配置文件

class YmlCfg:

    def __init__(self, cfg_path):
        self.cfg_path = cfg_path

    def load(self):
        if os.path.exists(self.cfg_path):
            with open(self.cfg_path) as f:
                return yaml.load(f)
        return None

cfg = YmlCfg('env/env.yml').load()

class BaseConfig(object):
    SECRET_KEY = 'IAMAGOODMAN'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = cfg.get('SQLALCHEMY_DATABASE_URI')
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


