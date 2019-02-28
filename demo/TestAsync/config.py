#coding: utf-8
# configure file
import os


BASE_DIR = os.path.dirname(os.path.basename(__file__))
print("===="+BASE_DIR)

port = "8002"
host = "0.0.0.0"

cookie_secret = b'qfTksZMFQdSXWitf/Y/2A/UOYkR7X0u8odaNFZAqtgo='

settings = {
    "debug": True,
    'static_path': os.path.join(BASE_DIR, 'statics'),
    'template_path': os.path.join(BASE_DIR, 'template'),
    'xsrf_cookies': True,
    'cookie_secret': cookie_secret
}


# logging
log_file = "logs/tornaod.log"
log_file_prefix = os.path.join(BASE_DIR, "logs/tornado.log")

# 加密秘钥
# str(base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes))
password_hash_key = 'WBWRmM2SSq2kcceCZvtFcN9LMo02Ik6wj0CGT3i2OUI='


# mysql数据库
mysql_db = dict(
    host="10.60.11.84",
    database="torndb",
    user="torndb",
    password="Torndb123!!!"
)

# redis数据库
redis = dict()

# mongoDB数据库
mongodb = dict()