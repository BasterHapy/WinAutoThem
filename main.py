# 程序入口
from PySide6.QtWidgets import QApplication
from src.main_widget import MainWidget
import sys

def main():
    """主函数"""
    # 应用程序
    app = QApplication([])

    # 实例化窗口并显示
    widget = MainWidget()
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
