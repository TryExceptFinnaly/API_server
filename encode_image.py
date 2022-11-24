import base64

CODE = 'utf-8'


class ImageBase64:
    @staticmethod
    def encode(image_file):
        with open(image_file, 'rb') as bin_image:
            base64_img = base64.b64encode(bin_image.read())
            base64_img = base64_img.decode(CODE)
            return base64_img

    @staticmethod
    def decode(base64_img, image_file):
        base64_img = base64_img.encode(CODE)
        with open(image_file, 'wb') as image_to_save:
            decoded_img = base64.b64decode(base64_img)
            image_to_save.write(decoded_img)
        return image_file
