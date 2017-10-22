# encoding: utf-8
import os, random, string
from base64 import decodestring
from flask import Flask, request, abort, send_file

app = Flask(__name__)

upload_folder = WebhookHandler(os.environ['UploadFolder'])  # Upload folder path

@app.route('/post',methods=['POST'])
def show_post():
    imgb64 = request.values.get("imgb64")
    if not imgb64:
        return 'NO DATA'
    else:
        filename = get_filename('png')
        data = decodestring(imgb64.encode('ascii'))
        with open(os.path.join(upload_folder, 'o', filename), "wb") as fd:
            fd.write(data)
        #return flask.redirect(flask.url_for("img", filename=filename))
        return filename

def get_filename(ext):
    res = []
    for i in range(10):
        res.append(random.choice(string.ascii_letters))
    return ''.join(res) + '.' + ext

@app.route("/img/<filename>", methods=['GET', 'POST'])
def view(filename):
    pattern = re.compile(r'^[A-Za-z]+$')
    if pattern.match(filename):
        try:
            filename = (os.path.join(upload_folder, 'o', filename)) + '.png'
            return send_file(filename, mimetype='image/png')
        except FileNotFoundError as e:
            print(e)
            abort(404)
            #return 'nofound'
    else:
        abort(404)
        #return 're'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
