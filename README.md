# raspberrypi-mediapipe-hands
本项目演示了如何在树莓派 4B 上，使用 Picamera2 获取摄像头画面，并结合 MediaPipe Hands 实现实时手部关键点追踪与可视化。
This project demonstrates how to use Picamera2 on a Raspberry Pi 4B to acquire camera images and combine it with MediaPipe Hands to achieve real-time hand keypoint tracking and visualization.

## 环境要求
- 硬件：Raspberry Pi 4B（经过4g版本实践）
- 系统：Raspberry Pi OS / Debian Bookworm（64-bit）
- 摄像头：官方 Camera Module（经过imx519实践）
- Python：最新版本Raspberry Pi OS自带3.11

## 环境配置
1. `sudo apt update && sudo apt -y upgrade`更新系统软件包
2. 
sudo apt -y install vim virtualenv       # 安装 vim 编辑器和 virtualenv 虚拟环境工具
sudo apt -y install python3-pip          # 安装 Python 包管理工具 pip
sudo apt -y install libatlas-base-dev    # 安装加速数学库（OpenCV/NumPy 会用到）
sudo apt -y install python3-opencv       # 安装 OpenCV（系统版）
sudo apt -y install python3-picamera2    # 安装 Picamera2（摄像头接口）
