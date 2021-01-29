
# mysql
DIALECT = "mysql"
DRIVER = "pymysql"
USENAME = "root"
PASSWORD = "295213"
HOST = "localhost"
PORT = "3306"
DATABASE = "manage"

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT, DRIVER, USENAME, PASSWORD, HOST, PORT, DATABASE
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 60

# cache

CACHE_TYPE = "simple"
CACHE_DEFAULT_TIMEOUT = 60*5
CACHE_THRESHOLE = 50