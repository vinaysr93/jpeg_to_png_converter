from PIL import Image
import sys,os

dir='.\Pokemons'


image_folder=os.fsencode(".\Pokemon")
output_folder=os.fsencode(r".\png_files")


if os.path.exists(output_folder):
    pass

else:
    os.makedirs(output_folder)
    ndir=".\png_files"

for filename in os.listdir(dir):

    q=filename.rstrip(".jpg")
    print(filename)

    img=Image.open(f"{dir}\{filename}")
    img.save(f"{ndir}\{q}.png","png")