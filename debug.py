from encode_image import ImageBase64

result = ImageBase64.encode('1.jpg')

with open('image_base64', 'w', encoding='utf-8') as image_base64:
    image_base64.write(result)