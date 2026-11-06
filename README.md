# Robot Learning

ROS 2、ロボティクス、AI、制御工学の学習記録。

## Project 1: Happy Mini Basic Control

### 環境
- Ubuntu 22.04
- ROS 2 Humble
- Gazebo Classic 11
- Happy Mini

### 実験内容
PythonプログラムからHappy Miniを制御する。

1. 2秒間前進
2. 1秒間停止
3. 2秒間左旋回
4. 2秒間停止

### 使用したROS 2の機能
- Node
- Publisher
- Topic (`/cmd_vel`)
- Twist message
- Timer

### プログラム
`ros2/happy_mini/happy_basic_control.py`
