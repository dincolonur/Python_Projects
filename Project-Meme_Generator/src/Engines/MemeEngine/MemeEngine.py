from PIL import Image, UnidentifiedImageError, ImageDraw, ImageFont
import os
import random


class MemeEngine:
    """MemeEngine object.

    MemeEngine class is used to create Meme to given input Image.
    This class has additional functions like resize_image,
    add_caption and make_meme.
    All of these functions can be used separately.
    """

    def __init__(self, output_dir):
        """Create a new `MemeEngine`.

        :param output_dir: Output Directory of Meme Image
        """
        self.output_dir = output_dir

    def resize_image(self, img_path, width):
        """Resizing the image in the given path with given width

        :param img_path: Image Path
        :param width: Image width, max 500 px
        :return: Resized Image saved path
        """
        tmp = f'{self.output_dir}/{random.randint(0,100000000)}.jpg'
        try:
            img = Image.open(img_path)
            img = img.convert('RGB')
        except UnidentifiedImageError:
            print("failed to open image")
        img_width, img_height = img.size

        if img_width > 500:
            ratio = width / img_width
            height = int(ratio * float(img_height))
            img = img.resize((width, height), Image.NEAREST)
        img.save(tmp)

        return tmp

    def add_caption(self, img_path, body, author):
        """Adding text to the image in the given path
        with given text body and author

        :param img_path: Image Path
        :param body: Text Body
        :param author: Text Author
        :return: Caption Added Image saved path
        """
        tmp = f'{self.output_dir}/result_{random.randint(0,100000000)}.jpg'
        try:
            img = Image.open(img_path)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            message = f'{body}, {author}'
            draw.text((10, 30), message, font=font, fill='white')
            img.save(tmp)
        except Exception as e:
            print("Exception caught: ", e)

        return tmp

    def make_meme(self, img_path, text, author, width=500):
        """Adding text to the image in the given path with
        given text body and author

        :param img_path: Image Path
        :param text: Text Body
        :param author: Text Author
        :param width: Image Width, optional. deafult 500px
        :return: Meme Made Image saved path
        """
        resized_image = self.resize_image(img_path, width)
        outfile = self.add_caption(resized_image, text, author)
        os.remove(resized_image)
        return outfile
