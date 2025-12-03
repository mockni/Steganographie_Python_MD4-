from PIL import Image

# Ouvre et convertit l'image en RGB
image = Image.open("image.jpg").convert("RGB")

# Taille de l'image
width, height = image.size

# Pixel spécifique
x, y = 10, 20
pixel = image.getpixel((x, y))
print(f'Pixel ({x},{y}) : {pixel}')

# Inverser toutes les couleurs
for vertical_pixel in range(height):
    for horizontal_pixel in range(width):
        r, g, b = image.getpixel((horizontal_pixel, vertical_pixel))
        image.putpixel((horizontal_pixel, vertical_pixel), (255-r, 255-g, 255-b))

# Sauvegarder et afficher l'image modifiée
image.save("modified_image.jpg")
image.show()
