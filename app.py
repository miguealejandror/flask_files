from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello_world():
    if 'img' not in request.files:
        return "<p> IMG not found </p>"

    else:
        img = request.files.get('img')
        img_name = request.files.get('img').filename
        img.save(f'{img_name}')
        return f"<p> IMG {img_name}</p>"
        

if __name__ == '__main___':
    app.run()