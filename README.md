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
