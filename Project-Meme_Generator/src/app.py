import random
import os
from flask import Flask, render_template, abort, request
import requests
from .Engines.IngestorEngine.Ingestor import Ingestor
from .Engines.MemeEngine.MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for quote_file_path in quote_files:
        quotes.extend(Ingestor.parse(quote_file_path))

    images_path = "./_data/photos/dog/"
    imgs = []
    for image_file in os.listdir(images_path):
        if image_file.endswith(".jpg"):
            imgs.append(os.path.join(images_path, image_file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    image = requests.get(url, allow_redirects=True)

    f = open('./tmp/uploaded_image.jpg', 'wb')
    f.write(image.content)
    f.close()
    path = meme.make_meme('./tmp/uploaded_image.jpg', body, author)
    print(path)
    os.remove('./tmp/uploaded_image.jpg')

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
