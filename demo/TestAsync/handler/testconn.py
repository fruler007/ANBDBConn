# coding: utf-8
from handler.base_handler import BaseHandler
import tornado.gen
import datetime
import random


class BatchInsert(BaseHandler):
    def get(self):
        for i in range(1, 1000001):


            # 插入用户信息
            user_id = i
            user_name = 'dandan' + str(i)
            user_mobile = 1999999999-i
            user_email = str(i) + "@fruler.com"
            sql = "insert into td_user_profile(up_name, up_mobile, up_email)" \
                  " value( %(user_name)s, %(user_mobile)s, %(user_email)s)"
            user_result = self.db.execute(sql, user_name=user_name,
                                     user_mobile=user_mobile, user_email=user_email)
            print("------> Insert user record user_id:%s" % user_result)


            # 插入产品信息
            product_id = i
            product_name = "p" + str(i)
            product_price = i
            sql = "insert into td_product(pr_name, pr_price) " \
                  "value(%(product_name)s, %(product_price)s)"
            product_result = self.db.execute(sql, product_name=product_name,
                                     product_price=product_price)
            print("------> Insert product record product_id:%s" % product_result)

            # 插入订单信息
            order_id = i
            product_id = i
            user_id = i
            ctime = utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = "insert td_order(or_user_id, or_product_id,or_ctime, or_utime)" \
                  " value(%(product_id)s, %(user_id)s, %(ctime)s, %(utime)s)"
            order_result = self.db.execute(sql, product_id=product_id, user_id=user_id,
                                     ctime=ctime, utime=utime)
            print("------> Insert order record order_id:%s" % order_result)


        return self.write("succuess")


class TestConn(BaseHandler):
    def get(self):
        return self.write("test")


class TestConnMysql(BaseHandler):
    def get(self):
        user_id = 1000
        #user_id = random.randrange(1, 10000001)
        sql = "select * from td_user_profile where up_user_id=%(user_id)s"
        query = self.db.get(sql, user_id=user_id)
        return self.write(query)


class TestConnAsyncMysql(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        user_id = 1000
        #user_id = random.randrange(1, 10000001)
        sql = "select * from td_user_profile where up_user_id=%(user_id)s"
        query = yield self.asyncdb.get(sql, user_id=user_id);
        print(query)
        return self.write(query)



class TestConnRedis(BaseHandler):
    pass


class TestConnAsyncRedis(BaseHandler):
    pass


class TestConnMongoDB(BaseHandler):
    pass


class TestConnAsyncMongoDB(BaseHandler):
    pass

