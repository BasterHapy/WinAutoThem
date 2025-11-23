# windows 注册表
import winreg

class WinThemeReg:
    """windows主题注册表"""
    def __init__(self):
        """构造函数"""
        # 打开需要操作的位置
        self.__key =  winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, 
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",
            0, 
            winreg.KEY_READ | winreg.KEY_WRITE
        )

    def __del__(self):
        """对象销毁时关闭注册表键"""
        if hasattr(self, '__key') and self.__key:
            winreg.CloseKey(self.__key)

    def get_system_theme(self) -> bool:
        """获取系统主题

        :return: 0 is dark ; 1 is light
        """
        # 获取相关的俩个值
        apps_used_theme = winreg.QueryValueEx(self.__key , "AppsUseLightTheme")[0]
        system_used_theme = winreg.QueryValueEx(self.__key , "SystemUsesLightTheme")[0]

        # 如果俩个值 都为 0 则 值设置为0 否则设置为1
        if (apps_used_theme and system_used_theme) == 0:
            return 0
        else:
            return 1
        
    def set_system_theme(self,module:bool):
        """设置系统主题

        :param module: 0 is dark; 1 is light
        """
        winreg.SetValueEx(self.__key, "AppsUseLightTheme", 0, winreg.REG_DWORD, module)
        winreg.SetValueEx(self.__key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, module)

    def reset_windows_theme(self):
        """重新设置主题为亮色或者暗色"""
        module = not self.get_system_theme()
        self.set_system_theme(module)
        winreg.CloseKey(self.__key)




