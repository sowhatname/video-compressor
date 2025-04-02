from compress import compress_video
import os
from tqdm import tqdm


def main():
    input_dir = "input"
    output_dir = "output"

    video_files = [
            f
            for f in os.listdir(input_dir)
            if f.lower().endswith((".mp4", ".mov", ".avi", ".mkv", ".flv"))
    ]
    
    if not video_files:
        print(f"❌ 错误：{input_dir} 中没有找到视频文件")

    # input_file = os.path.join(input_dir, "Image of Jia County.mp4")
    # output_file = os.path.join(output_dir, "compressed_video.mp4")

    # if not os.path.exists(input_file):
    #     print(f"错误，输入文件不存在 {input_file}")
    #     return

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # #使用示例1：压缩单个文件
    # compress_video(input_file, output_file, quality=28)
    # print("压缩完成！")

    # 使用示例2：批量压缩 使用进度条显示处理进度
    print(f"开始压缩 {len(video_files)} 个视频...")
    for filename in tqdm(video_files, desc="压缩进度"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, "compressed_" + filename)
        compress_video(input_path, output_path)

    print(f"✅ 完成！压缩后的视频保存在 {output_dir}")

if __name__ == "__main__":
    main()
