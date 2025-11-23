# 程序入口
from src.my_location import MyLocation
from src.one_day import OneDay

def main():
    """主函数"""

    # 获取经纬度
    my_loc = MyLocation()
    latlng_list = my_loc.get_latlng()

    # 实例化一天
    one_day = OneDay(latlng_list)

    # 时间
    current_time = one_day.get_current_time()
    sun_rise = one_day.get_sun_rise()
    sun_set = one_day.get_sun_set()

    # 判断当前是白天还是黑夜
    if current_time >= sun_rise and current_time <= sun_set:
        print("Light")
    elif current_time <= sun_rise:
        print("dark")
    elif current_time >= sun_set:
        print("dark")

if __name__ == "__main__":
    main()
