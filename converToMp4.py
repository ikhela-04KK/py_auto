import moviepy
# convertir grâce à un fichier weba 
import moviepy.editor

video = moviepy.editor.VideoFileClip("C:/Users/ikhela/Videos/Cyberpunk Music — Energetic Workout Playlist.weba")
audio = video.audio

audio.write_audiofile("new_audio.mp3")
