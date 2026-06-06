from flask import Flask

class Config:
    SECRET_KEY = 'SECRET_VALUE'

    @staticmethod
    def init_app(_: Flask):
        print('initializing config with app')
        pass

class DevelopmentConfig(Config):
    pass

class Test(Config):
    TESTING = True

config: dict[str, type[Config]] = {
    'development': DevelopmentConfig,
    'test': Test
}
