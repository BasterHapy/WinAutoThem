# 程序主界面
from PySide6.QtWidgets import QWidget,QRadioButton,QSpinBox,QHBoxLayout,QMessageBox
from PySide6.QtCore import QTimer
from src.my_location import MyLocation
from src.one_day import OneDay
from src.win_theme_reg import WinThemeReg
import time

class MainWidget(QWidget):
    """主界面

    :param QWidget: PySide6 基础窗口
    """
    def __init__(self,interval_minutes=1):
        """构造函数"""
        super().__init__() #继承父类方法

        # 定义属性
        self.current_time = 0
        self.interval_minutes = interval_minutes

        # 初始化界面 定时器 事件绑定
        self.setup_ui()
        self.setup_timer()
        self.setup_event_bind()

    def setup_ui(self):
        """设置用户界面"""
        # 窗口设置 
        self.setWindowTitle("WinAutoTheme")

        # 全局使用水平布局
        self.glob_hbox = QHBoxLayout(self)

        # 创建控件
        self.auto_choose_btn = QRadioButton("自动选择主题",self)
        self.minute_spin_box = QSpinBox(self,value=1)

        # 添加控件
        self.glob_hbox.addWidget(self.auto_choose_btn)
        self.glob_hbox.addWidget(self.minute_spin_box)

    def setup_event_bind(self):
        """设置事件绑定"""
        self.auto_choose_btn.clicked.connect(self.handel_auto_choose_theme)

    def handel_auto_choose_theme(self):
        """自动选择主题"""

        # 间隔分钟数 使用自动选择按钮
        self.interval_minutes = int(self.minute_spin_box.value())
        
        # 更新当前时间
        self.interval_upgrade_current_time()

        # 选择主题
        self.auto_choose_theme()

    def auto_choose_theme(self):
        """自动选择"""

        # 获取位置
        my_loc = MyLocation()
        latlng_list = my_loc.get_latlng()

        # 断言
        assert latlng_list ,QMessageBox.information(self,"WinAutoTheme","请连接网络!")

        # 实例化一天
        one_day = OneDay(latlng_list)

        # 获取当前时间、日出日落
        current_time = self.current_time
        sun_rise = one_day.get_sun_rise()
        sun_set = one_day.get_sun_set()

        # 实例化注册表
        win_them_reg = WinThemeReg()

        # 判断当前是白天还是黑夜 => 设置对应主题
        if current_time >= sun_rise and current_time <= sun_set:
            win_them_reg.set_system_theme(1)
        elif current_time <= sun_rise:
            win_them_reg.set_system_theme(0)
        elif current_time >= sun_set:
            win_them_reg.set_system_theme(0)

    def setup_timer(self):
        """设置定时器具"""
        self.timer = QTimer(self)
    
    def interval_upgrade_current_time(self):
        """间隔几分钟获取当前时间"""
        self.upgrade_current_time()        
        self.timer.timeout.connect(self.upgrade_current_time)
        self.timer.start(self.interval_minutes*60000)

    def upgrade_current_time(self):
        """更新当前时间"""
        self.current_time = time.time()
        print(self.current_time)