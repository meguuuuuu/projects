from PIL import Image

def resize_image(size1, size2):
    image = Image.open('a23b0406af95fbc954661198b6bdf934.jpg')
    print(f"Current size: {image.size}")
    
    resized_image = image.resize((size1, size2))
    resized_image.save('a23b0406af95fbc954661198b6bdf934-new.jpg')
    
    print(f"New size: {resized_image.size}")

size1 = int(input("Desired width: "))
size2 = int(input("Desired length: "))
resize_image(size1, size2)