class ProductionConfig:
    DEBUG = False
    TESTING = False
    host="0.0.0.0"
    port=43760

class DevelopmentConfig:
    DEBUG = True
    TESTING = True
    host="0.0.0.0"
    port=3333
