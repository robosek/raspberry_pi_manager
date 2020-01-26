import time
from gpiozero import LED
from flask import Flask
from threading import Thread

app = Flask(__name__)

led = LED(16)
blink_interval = .5
shouldBlink = False

def run():
    while True:
        if shouldBlink:
            led.on()
            time.sleep(blink_interval)
            led.off()
            time.sleep(blink_interval)
        else: 
            led.off()

thread = Thread(target = run, args = [])
thread.start()

@app.route("/enable")
def enable():
    global shouldBlink
    shouldBlink = True
    return "Led enabled"

@app.route("/disable")
def disable():
    global shouldBlink
    shouldBlink = False
    return "Led disabled"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)