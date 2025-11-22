# 定义我的位置类
import geocoder

class MyLocation(object):
    """我的位置

    :param object: Python 基础类
    """
    def __init__(self):
        """构造函数"""
        self.location_info = geocoder.ip("me")

    def get_latlng(self) -> tuple[float,float]:
        """获取经纬度

        :return: 经度,纬度
        """
        return self.location_info.latlng
        
