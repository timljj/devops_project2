import io
import json

import requests
from PIL import Image
from flask import Flask, jsonify, request, render_template, flash
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import base64


app = Flask(__name__)

app.config['SECRET_KEY'] = '3f651974d8272f5f35717559f41023c8a567f70c34ea3568'

# device = "cuda" if torch.cuda.is_available() else "cpu"


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# img_url = "https://tensorflow.org/images/surf.jpg"
# img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
def open_image_from_url(img_url):
    raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')
    return raw_image

def process_image(raw_image, text='A picture of'):
    # conditional image captioning
    inputs = processor(raw_image, text, return_tensors="pt")
    return inputs

def get_caption(inputs):
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/caption_from_url', methods=['GET', 'POST'])
# def caption_from_url_page():
#     return render_template('caption_from_url.html')

# @app.route('/caption_from_file')
# def caption_from_file_page():
#     return render_template('caption_from_file.html')

@app.route('/caption_from_file', methods=['POST'])
def caption_from_file():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_caption(image_bytes=img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name})

@app.route('/caption_from_url', methods=['GET', 'POST'])
def caption_from_url():
    caption = None
    img_url = None
    if request.method == 'POST':
        img_url = request.form['url']
        print(img_url)
        if not img_url:
            flash("Image URL is Required!")
        else:
            raw_image = open_image_from_url(str(img_url))
            disp_img = base64.b64encode(raw_image)
            processed_img = process_image(raw_image)
            caption = get_caption(processed_img)
            print(f'Caption: {caption}')
            # caption = [jsonify({'caption': caption})]
    return render_template('caption_from_url.html', context=[{'caption': caption, 'img': disp_img}]) # need to send list of dictionary


if __name__ == '__main__':
    app.run()