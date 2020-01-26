import time
from picamera import PiCamera
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/capture")
def caputre_photo():
    camera = PiCamera()
    camera.capture('/home/pi/img{counter:03d}.jpg')
    return "Photo captured"

@app.route("/disable")
def disable():
    camera.destroy()
    return "Photo captured"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)