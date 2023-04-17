import moviepy
# convertir grâce à un fichier weba 
from moviepy.editor import AudioFileClip
import os
#lien vers le document contenant les musics

folder ="C:\\Users\\ikhela\\Downloads\\Simiane\\"
mp3_files = os.listdir(folder)

for mp3_file in mp3_files:
    old_name=folder+mp3_file
    new_name = folder+mp3_file[:-5]+".mp3"

    # video = moviepy.editor.VideoFileClip(old_name)
    audio = AudioFileClip(old_name)

    #Créer l'objet weba
    audio.write_audiofile(new_name)

    #ensuite verifier si le fichier n'existe pas et le supprime
    if os.path.exists(new_name):
        print(new_name, "créée avec succès")
        os.remove(old_name)
        print(old_name, "supprimé avec succès")


