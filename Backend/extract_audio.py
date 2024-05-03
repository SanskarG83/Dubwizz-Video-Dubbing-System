from moviepy.editor import VideoFileClip
import os
import ML_Model as Ml


def extract_video_and_audio(input_video_path, language):
    if not os.path.exists("extracted"):
        os.makedirs("extracted")
    video_clip = VideoFileClip(input_video_path)

    video_without_audio = video_clip.set_audio(None)

    video_output_path = os.path.join("extracted", "video_without_audio.mp4")
    audio_output_path = os.path.join("extracted", "audio_only.mp3")

    video_without_audio.write_videofile(video_output_path, codec="libx264")
    video_clip.audio.write_audiofile(audio_output_path)
    print("Audio Extracted Successfully")

    Ml.mlalgo(language)

    return audio_output_path
