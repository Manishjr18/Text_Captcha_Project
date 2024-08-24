from captcha.image import ImageCaptcha
import random
from flask import Flask, request, render_template, jsonify, url_for
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def generate_captcha():
    num = random.randint(100000, 999999)
    image = ImageCaptcha()
    tstr = time.strftime("%Y%m%d-%H%M%S")
    image_path = f'./static/images/{tstr}.png'
    image.write(str(num), image_path)
    return num, tstr

@app.route("/", methods=["GET", "POST"])
def index():
    global num1, tstr
    error = None
    success = None

    if request.method == "GET" or 'num1' not in globals():
        num1, tstr = generate_captcha()
        return render_template('index.html', tstr=tstr, error=error, success=success)

    if request.method == "POST":
        ip = request.form["ip"]
        try:
            if int(ip) == num1:
                success = "CAPTCHA passed successfully!"
                error = None
            else:
                error = "Invalid CAPTCHA. Please try again."
                success = None
                num1, tstr = generate_captcha()
        except:
            error = "Invalid CAPTCHA. Please try again."
            success = None
            num1, tstr = generate_captcha()

        return render_template('index.html', tstr=tstr, error=error, success=success)

@app.route("/refresh-captcha", methods=["GET"])
def refresh_captcha():
    global num1, tstr
    num1, tstr = generate_captcha()
    new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
    return jsonify(new_captcha_url=new_captcha_url)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", threaded=True, use_reloader=True)
