from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
	"https://c.tenor.com/e-LsbnNHQ5cAAAAM/catjam-cat-dancing.gif",
	"https://c.tenor.com/9fmM6Pvs5UYAAAAM/thinking-cat.gif",
	"https://c.tenor.com/7r-BGEoIohkAAAAM/meme-cat.gif",
	"https://c.tenor.com/z2IqVLn-acMAAAAM/meme.gif",
	"https://c.tenor.com/imInjg-rh-sAAAAM/man.gif",
	"http://forgifs.com/gallery/d/287423-2/Supermarket-for-cats.gif",
	"https://c.tenor.com/zrpyKEyxZGwAAAAM/fat-cat-laser-eyes.gif",
	"https://c.tenor.com/yQ0MhaCh-u0AAAAM/bv0j-help.gif",
	"https://c.tenor.com/CspedX6mLi8AAAAM/cat-dancing-cat.gif",
	"https://c.tenor.com/e4Y1zFJQIEQAAAAM/cat-rich.gif",
	"https://c.tenor.com/9beDx3ElF4gAAAAM/digibyte-dgb.gif",
	"https://c.tenor.com/8rcw4jwz_0EAAAAM/bitcoin-bitcoin-dip.gif",
	"https://c.tenor.com/ogsH7Ailje8AAAAM/cat-funny-cat.gif",
	"https://c.tenor.com/E0CNoE9DCdwAAAAM/tech-catto.gif",
	"https://c.tenor.com/QUL6BSSHKswAAAAM/sassy-cat.gif"
]
@app.route('/')
def index():
 url = random.choice(images)
 return render_template('index.html', url=url)
if __name__ == "__main__":
 app.run(host="0.0.0.0")
