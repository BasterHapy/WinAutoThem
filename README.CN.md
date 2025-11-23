# WinAuto
[![Python](https://img.shields.io/badge/Python-3.11-darkgreen.svg)](https://doc.qt.io/qtforpython-6/index.html)
[![PySide6 version](https://img.shields.io/badge/PySide6-6.10-green.svg)](https://doc.qt.io/qtforpython-6/index.html)
[![License](https://img.shields.io/badge/License-GPL3.0-blue.svg)](https://opensource.org/license/gpl-3-0)
[![Support System](https://img.shields.io/badge/Windows-%3e%3d10-red)](https://opensource.org/license/gpl-3-0)

这是一个PySide6实现的Windows自动切换主题的小工具！

[简体中文](./README.CN.md)

## 功能特性

- 自动切换主题
- 支持系统托盘
- 开机自启动

## 怎么运行

### 创建虚拟环境
```bash
uv venv pywin -p 3.11
```
### 使用虚拟环境
```bash
 .\pywin\Scripts\activate.bat
```
### 安装依赖
```bash
uv pip install -r ./requirements.txt
```
### 运行
```bash
python main.py
```