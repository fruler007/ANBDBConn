#coding: utf-8
import tornado.web
import tornado.httpserver
import tornado.ioloop
import torndb
import config
import tornado.options
import url_pattern
from utils import async_mysql
from tornado.options import options, define


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.MySQL = torndb.Connection(**config.mysql_db)
        self.ANBMySQL = async_mysql.ANBMySQL(**config.mysql_db)
        self.ANBRedis = ""
        self.ANBMongoDB = ""


if __name__ == "__main__":
    define(name="port", type=int, default=config.port,
           help="server run on given port")
    define(name="address", type=str, default=config.host,
           help="server run on given host")

    # 分割日志
    tornado.options.options.log_rotate_mode = "time"
    tornado.options.options.log_rotate_when = "D"
    tornado.options.options.log_rotate_interval = 1
    tornado.options.options.log_file_prefix = config.log_file_prefix
    tornado.options.parse_command_line()

    # 启动IOLoop
    app = Application(url_pattern.url_mapping, **config.settings)
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port, options.address)
    tornado.ioloop.IOLoop.current().start()
