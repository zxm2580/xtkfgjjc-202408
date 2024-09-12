from PIL import Image

image_1 = Image.open("ori.jpg")

image_2 = image_1.resize((640, 480))
image_2.save("exp1.jpg")

image_3 = image_2.convert("L")
image_3.save("exp2.jpg")

image_3.save("exp3.gif")
