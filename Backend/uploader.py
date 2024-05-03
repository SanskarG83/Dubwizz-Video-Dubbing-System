from mega import Mega

# Replace these with your Mega.nz credentials
mega_email = 'omgore6443@gmail.com'
mega_password = "V'W=SNyU?Pjf4j7"

# Initialize Mega client
mega = Mega()

# Log in to your Mega.nz account
m = mega.login(mega_email, mega_password)

# Specify the names of the folders you created manually
audio_folder_name = 'Audio'
video_folder_name = 'Video'
subtitles_folder_name = 'Subtitles'

video_file_path = 'Final\\dubbed_video.mp4'
video_folder = m.find(audio_folder_name)
if video_folder:
    m.upload(video_file_path, video_folder[0])
print("Uploaded")

audio_file_path = 'Output\\translated_audio.mp3'
audio_folder = m.find(audio_folder_name)
if audio_folder:
    m.upload(audio_file_path, audio_folder[0])
print("Uploaded")

text_file_path = 'Output\\eng_sub.txt'
subtitles_folder = m.find(subtitles_folder_name)
if subtitles_folder:
    m.upload(text_file_path, subtitles_folder[0])
print("Uploaded")

print("Files uploaded successfully to Mega.nz.")
