from PIL import Image

# Ouvre et convertit l'image en RGB
image = Image.open("image.jpg").convert("RGB")

# image size
width, height = image.size

# Pixel 
x, y = 10, 20
pixel = image.getpixel((x, y))
print(f'Pixel ({x},{y}) : {pixel}')

# reverse colors
for vertical_pixel in range(height):
    for horizontal_pixel in range(width):
        r, g, b = image.getpixel((horizontal_pixel, vertical_pixel))
        image.putpixel((horizontal_pixel, vertical_pixel), (255-r, 255-g, 255-b))

# save new image
image.save("modified_image.jpg")
image.show()


def text_vers_binaire(text):
    binaire = ""
    for caractere in text:
        binaire += format(ord(caractere), "08b")  # 8 bits
    return binaire
text='watermark'
text_vers_binaire(text)
print(text_to_binaire(text))


