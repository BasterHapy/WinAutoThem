#请求API来获取日出日落
import requests
from datetime import datetime

def get_sunrise_sunset(latlng:tuple[float,float]):
    """获取日出日落

    :param latlng: 精度维度时间戳列表
    """
    # 定义请求地址
    url = f"https://api.sunrise-sunset.org/json?lat={latlng[0]}&lng={latlng[1]}&date=today&formatted=0"

    # 返回请求
    data = requests.get(url,timeout=50).json()
    
    # 处理返回数据
    if data["status"] == "OK":
        
        sun_rise = datetime.fromisoformat(data["results"]["sunrise"]).timestamp()
        sun_set = datetime.fromisoformat(data["results"]["sunset"]).timestamp()

        # 返回经纬度
        return sun_rise,sun_set
    
    else:
        return None,None


    

