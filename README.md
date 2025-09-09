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
2. `sudo apt –y install vim virtualenv`   安装 vim 编辑器和 virtualenv 虚拟环境工具
3. 创建项目文件夹
4. `svirtualenv cv`   在当前目录下创建名为 cv 的虚拟环境
5. `source cv/bin/activate`   激活虚拟环境
6. `pip install mediapipe python3-opencv python3-picamera2`   安装 MediaPipe（手部追踪算法库）、 OpenCV、 Picamera2（摄像头接口）

基于[树莓派文档](https://pidoc.cn/docs/computers/camera-software)的提示
> Raspberry Pi OS Bookworm 将摄像头捕捉应用程序从 libcamera-\* 更名为 rpicam-*。符号链接允许用户暂时使用旧名称。尽快采用新的应用程序名称。 Bookworm之前的 Raspberry Pi OS 版本仍使用 libcamera-* 名称。

## 功能测试
`rpicam-hello`  
