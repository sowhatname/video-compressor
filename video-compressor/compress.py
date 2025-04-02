import subprocess  # 调用外部ffmpeg命令
import os


def compress_video(
    input_file, output_file, quality=23, preset="fast", audio_bitrate="128k"
):
    """
    压缩单个视频文件
    :param input_file: 输入文件路径
    :param output_file: 输出文件路径
    :param quality: CRF质量参数(18-28)
    :param preset: 编码速度预设
    :param audio_bitrate: 音频比特率
    :return: True成功 / False失败
    """
    ffmpeg_path = r"F:\ffmpeg\bin\ffmpeg.exe"
    if not ffmpeg_path:
        print("❌ 错误：未找到 ffmpeg，请安装并添加到系统PATH")
        return False

    if not os.path.exists(input_file):
        print(f"❌ 错误：输入文件不存在 {input_file}")
        return False

    command = [
        ffmpeg_path,
        "-i",
        input_file,             # 输入文件
        "-vcodec",
        "libx264",              # 使用H.264编码
        "-crf",
        str(quality),           # 质量参数
        "-preset",
        preset,                 # 编码速度预设
        "-acodec",
        "aac",                  # 音频编码
        "-b:a",
        audio_bitrate,          # 音频比特率
        output_file,            # 输出文件
    ]

    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(
            f"压缩失败：{os.path.basename(input_file)} - {e.stderr.decode('utf-8')[:200]}..."
        )
        return False
