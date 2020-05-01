"""
This is the file for redis connection in which various redis method are written
Author : Shruti Zarbade
"""
import redis
import logging
import os
from dotenv import load_dotenv
from config.singleton import singleton
logging.basicConfig(level=logging.DEBUG)
load_dotenv()


@singleton  # singleton is decorator
class RedisConnection:

    def __init__(self, **kwargs):
        self.connection = self.connect(**kwargs)

    # this is the function for connecting
    def connect(self, **kwargs):
        connection = redis.StrictRedis(host=kwargs['host'],
                                       port=kwargs['port'],
                                       db=kwargs['db'])
        if connection:
            logging.info('Redis Cache Connection established')
        return connection

    # this function set the data in redis
    def set(self, key, value, exp_s=None, exp_ms=None):
        self.connection.set(key, value, exp_s, exp_ms)
        logging.info(f'{key} : {value}')

    # this function get data from the redis
    def get(self, key):
        return self.connection.get(key)

    # this function check weather the key exists in redis or not
    def exists(self, key):
        return self.connection.exists(key)

    # this function delete key from redis
    def delete(self, key):
        logging.info(f'Key to Delete : {key}')
        self.connection.delete(key)


redis_con = RedisConnection(host=os.getenv('redis_host'),
                            port=os.getenv('redis_port'),
                            db=os.getenv('redis_db'))