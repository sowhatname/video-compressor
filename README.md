# video-compressor
A Python tool for compressing videos with FFmpeg
# 简单视频压缩工具

## 功能
- 压缩单个视频文件
- 批量处理目录中的视频文件
- 可调整压缩质量参数

## 使用要求
- Python 3
- FFmpeg
- tqdm库（用于进度条）

## 使用方法
1. 安装依赖：
   ```bash
   pip install tqdm
2. 准备：
   将视频放入input文件夹
   确保FFmpeg已安装（或修改compress.py中的路径）
3. 运行：
   ```bash
   python main.py
4. 输出：
   压缩后的视频保存在output文件夹
   文件名添加compressed_前缀
