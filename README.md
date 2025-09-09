# raspberrypi-mediapipe-hands
本项目演示了如何在树莓派 4B 上，使用 Picamera2 获取摄像头画面，并结合 MediaPipe Hands 实现实时手部关键点追踪与可视化，再将画面通过X11转发到windows系统上。    
This project demonstrates how to use Picamera2 on a Raspberry Pi 4B to capture camera images, combine it with MediaPipe Hands to achieve real-time hand keypoint tracking and visualization, and then forward the images to a Windows system through X11.    

本项目不包含摄像头配置相关的内容，请网络自查或询问你所购买摄像头店铺的客服

## 环境要求
- 硬件：Raspberry Pi 4B（经过4g版本实践）
- 系统：Raspberry Pi OS / Debian Bookworm（64-bit）
- 摄像头：官方 Camera Module（经过imx519实践）
- Python：最新版本Raspberry Pi OS自带3.11
- Windows系统电脑: 需安装mobaxterm等支持X11的ssh软件

## 环境配置
1. `sudo apt update && sudo apt -y upgrade`更新系统软件包
2. ```
   sudo apt install -y python3-pip python3-dev python3-venv \
    libopencv-dev libcamera-apps libcamera-dev python3-libcamera \
    x11-apps libcap-dev virtualenv`
   ```   安装常用工具、virtualenv 与一些系统依赖
3. 创建项目文件夹
4. `virtualenv -p python3 --system-site-packages cv`   在当前目录下创建虚拟环境（使用系统的依赖库，避免冲突）
5. `source cv/bin/activate`   激活虚拟环境
6. `pip install mediapipe opencv-python numpy`   安装 MediaPipe（手部追踪算法库）、 OpenCV、numpy

基于[树莓派文档](https://pidoc.cn/docs/computers/camera-software)的提示
> Raspberry Pi OS Bookworm 将摄像头捕捉应用程序从 libcamera-\* 更名为 rpicam-*。符号链接允许用户暂时使用旧名称。尽快采用新的应用程序名称。 Bookworm之前的 Raspberry Pi OS 版本仍使用 libcamera-* 名称。

## 功能测试
`rpicam-hello` 如果能显示摄像头，说明摄像头配置正常    
`xeyes`      如果能弹窗，说明 X11 转发正常    

## 运行代码
python3 finger.py
