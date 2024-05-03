from moviepy.editor import VideoFileClip, AudioFileClip

def combine_video_with_audio(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)


    video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile(output_path, codec="libx264")

