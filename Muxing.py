import os,sys 
import subprocess
cmd = 'ffmpeg -y -i [abc.mp4]  -r 30 -i [abc.mp3]  -filter:a aresample=async=1 -c:a flac -c:v copy [abc.mkv]'
subprocess.call(cmd, shell=True)                                   
print('Muxing Done')
