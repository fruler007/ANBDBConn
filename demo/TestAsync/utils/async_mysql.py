#!/usr/bin/env python
"""
一个torndb的异步封装
基于asyncio库的实现，用于tornado框架的mysql的数据操作
"""

from lib import newtorndb

import functools
import asyncio.futures


def async_mysql_db(func):
    wrapped = func

    @functools.wraps(wrapped)
    def wrapper(query, *args, **kwargs):
        fn = asyncio.futures.Future()
        result = func(query, *args, **kwargs)
        try:
            fn.set_result(result)
            return fn
        finally:
            fn = None
    return wrapper



class ANBMySQL(newtorndb.Connection):
    @async_mysql_db
    def execute(self, query, *parameters, **kwparameters):
        return super(ANBMySQL, self).execute(query, *parameters, **kwparameters)

    @async_mysql_db
    def query(self, query, *parameters, **kwparameters):
        return super(ANBMySQL, self).query(query, *parameters, **kwparameters)

    @async_mysql_db
    def get(self, query, *parameters, **kwparameters):
        return super(ANBMySQL, self).get(query, *parameters, **kwparameters)