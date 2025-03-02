import sys
from PIL import Image

# assuming you have tw ogif images costume1.gif and costume2.gif

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    "costumes.gif", save_all = True, append_images=[images[1]], duration = 200, loop=0
)