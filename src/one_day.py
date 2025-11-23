# 这是一个抽象类，用于获取一天的日出和日落时间以及当前时间。
import time
from src.sun_rise_set import get_sunrise_sunset

class OneDay(object):
    """一天

    :param object: Python 基础类
    """
    def __init__(self,latlng: tuple[float,float]):
        """构造函数

        :param latlng: 经纬度
        """
        self.sun_info = get_sunrise_sunset(latlng)
    
    def get_current_time(self) -> float:
        """获取当前时间

        :return: Unix 时间戳
        """
        return time.time()
    
    def get_sun_rise(self) -> float:
        """获取日出时间

        :return: Unix 时间戳
        """
        return self.sun_info[0]
        

    def get_sun_set(self) -> float:
        """获取日落时间

        :return: Unix 时间戳
        """
        return self.sun_info[1]
