# coding = utf-8
import tornado.web
import config
import os
from handler import testconn


url_mapping = [
    #(r"^/test/batchinsert$", testconn.BatchInsert),
    (r"^/test", testconn.TestConn),
    (r"^/test/mysql", testconn.TestConnMysql),
    (r"^/test/asyncmysql", testconn.TestConnAsyncMysql),
    (r"/(.*)", tornado.web.StaticFileHandler,
     dict(path=os.path.join(os.path.dirname(__file__), "template"),
          default_filename="index.html")),
]
