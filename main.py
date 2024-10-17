from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path, bitrate="2000k"):
    video_clip = VideoFileClip(input_path)
    video_clip.write_videofile(output_path, bitrate=bitrate)
    video_clip.close()

compress_video("video.mp4", "compress_video3.mp4", bitrate="2000k")
