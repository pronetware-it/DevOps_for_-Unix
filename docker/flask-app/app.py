from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-25329-1381845415-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-25158-1381844793-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-23859-1381845509-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19645-1381845207-5.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-18774-1381844645-6.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-11864-1381846346-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3409-1381844582-13.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3391-1381844336-26.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-1376-1381846217-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-31540-1381844535-8.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26358-1381845043-13.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26383-1381845104-25.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-27208-1381845845-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-27162-1381845360-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-11980-1381846269-1.gif"
]
@app.route('/')
def index():
url = random.choice(images)
return render_template('index.html', url=url)
if __name__ == "__main__":
app.run(host="0.0.0.0")
