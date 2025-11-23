# 程序入口
from src.my_location import MyLocation
from src.one_day import OneDay
from win_theme_reg import WinThemeReg

def main():
    """主函数"""

    # 获取经纬度
    my_loc = MyLocation()
    latlng_list = my_loc.get_latlng()

    # 断言
    assert latlng_list ,"请连接网络"

    # 实例化一天
    one_day = OneDay(latlng_list)

    # 时间
    current_time = one_day.get_current_time()
    sun_rise = one_day.get_sun_rise()
    sun_set = one_day.get_sun_set()

    # 实例化注册表
    win_them_reg = WinThemeReg()

    # 判断当前是白天还是黑夜
    if current_time >= sun_rise and current_time <= sun_set:
        win_them_reg.set_system_theme(1)
        print("Light")
    elif current_time <= sun_rise:
        win_them_reg.set_system_theme(0)
        print("dark")
    elif current_time >= sun_set:
        win_them_reg.set_system_theme(0)
        print("dark")

if __name__ == "__main__":
    main()
