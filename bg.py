import os
import time
import random

while True:
    # Set the path to the directory containing the images you want to use as your desktop background
    image_directory = '/home/USERNAME/Pictures/Wallpaper'

    # Get a list of all the images in the directory
    images = os.listdir(image_directory)

    # Choose a random image from the list
    image = images[int(random.random() * len(images))]

    # Set the image as the desktop background
    os.system(f'gsettings set org.gnome.desktop.background picture-uri file://{image_directory}/{image}')

    # Wait for a period of time before changing the background again
    time.sleep(45) # Change the background every 15s
