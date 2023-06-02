import os
import cv2
vidcap = cv2.VideoCapture('C:\\Users\\msi\\Desktop\\PFE\\pfe\\video\\fire.mp4')
num_subvideos = 32
num_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
frames_per_subvideo = num_frames // num_subvideos
if not os.path.exists('Fire053_x264'):
    os.makedirs('Fire053_x264')
frame_count = 0
subvideo_count = 0
while True:
    success, image = vidcap.read()
    if not success:
        break
    # Incrémenter le compteur de frame
    frame_count += 1
    if frame_count % frames_per_subvideo == 0:
        subvideo_count += 1
        # Définir le nom de la sous-vidéo et le chemin complet
        subvideo_name = f'Fire053_x264_{subvideo_count}.mp4'
        subvideo_path = os.path.join('Fire053_x264', subvideo_name)
        subvideo_writer = cv2.VideoWriter(subvideo_path, cv2.VideoWriter_fourcc(*'mp4v'), 
                                          vidcap.get(cv2.CAP_PROP_FPS), (image.shape[1], 
                                                                         image.shape[0]))
        for i in range(frames_per_subvideo):
            success, image = vidcap.read()
            if success:
                subvideo_writer.write(image)
            else:
                break
        subvideo_writer.release()
vidcap.release()
