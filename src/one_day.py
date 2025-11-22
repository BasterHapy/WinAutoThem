# 这是一个抽象类，用于获取一天的日出和日落时间以及当前时间。

import time

class OneDay(object):
    """一天

    :param object: Python 基础类
    """
    def __init__(self):
        """构造函数"""
        pass
    
    def get_current_time(self) -> float:
        """获取当前时间

        :return: Unix 时间戳
        """
        return time.time()
    
    def get_sun_rise(self) -> float:
        """获取日出时间

        :return: Unix 时间戳
        """
        pass

    def get_sun_set(self) -> float:
        """获取日落时间

        :return: Unix 时间戳
        """
        pass
