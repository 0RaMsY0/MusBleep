# import subprocess

# from utils.random_id import random_id

#def extract_vocals(music_path: str) -> str:
    # """
    #     Uses spleeter to separate vocals from
    #     the beat then it returns that path to
    #     the extracted vocals
    # """
#    random_music_name = random_id()
#    save_path = f"cache/{random_music_name}.mp3"
#    command = ["python3", "-m", "spleeter", "separate", f"{music_path}", "-o", f"cache/{random_music_name}"]
#    convert_to_mp3 = ["ffmpeg", "-i", f"cache/{random_music_name}/{music_path.split('/')[-1].replace('.mp3', '')}/vocals.wav", f"{save_path}"]
#    clean_up = ["rm", "-rif", f"cache/{random_music_name}"]
#    
#    # Extract Vocals
#    subprocess.run(command, shell=False)
#    # Convert to MP3
#    subprocess.run(convert_to_mp3, shell=False)
#    # Clean up
#    subprocess.run(clean_up, shell=False)
#    
#    return save_path