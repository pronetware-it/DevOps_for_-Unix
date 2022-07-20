# Task #
Using docker lection2 create a docker image with Python Flask app that displays random cat pix.

1 - Create directory structure

- `mkdir -p flask-app/templates`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/mkdir.gif)

2 - Create file structure 


- `touch ./flask-app/{app.py,requirement.txt,templates/index.html,templates/Dockerfile}`


![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/touch.gif)

3 - Content of app.py

- `nano app.py`

```from flask import Flask, render_template
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
```

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/app.gif)

4 - Content of requirements.txt

- `echo "Flask==0.10.1"> requirements.txt`

  - `Flask==0.10.1`


![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/requ.gif)

5 - Content of index.html

- `nano index.html`

```<html>
<head>
<style type="text/css">
body {
background: black;
color: white;
}
div.container {
max-width: 500px;
margin: 100px auto;
border: 20px solid white;
padding: 10px;
text-align: center;
}
h4 {
text-transform: uppercase;
}
</style>
</head>
<body>
<div class="container">
<h4>Cat Gif of the day</h4>
<img src="{{url}}" />
<p><small>Courtesy: <a href="https://www.catshaming.co.uk/20-best-cat-gif-posts/">Catshaming</a></small></p>
</div>
</body>
</html>
```

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/index.gif)

6 - Content of Dockerfile

- `nano Dockerfile`

```# our base image
FROM alpine:3.5
# Install python and pip
RUN apk add --update py2-pip
# upgrade pip
RUN pip install --upgrade pip
# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/
# tell the port number the container should expose
EXPOSE 5000
# run the application
CMD ["python", "/usr/src/app/app.py"]
```

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/content-docker.gif)


7 - Move of Dockerfile

- `mv ./flask-app/templates/Dockerfile ~/DevOps_for_Unix/docker/flask-app/`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/mv-dockerfile.gif) 


8 - Docker images building

- `docker build -t serhii_rozhko/mycatapp .`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/docker-build.gif)

Not a mistake, but a warning

'''DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020.
Please upgrade your Python as Python 2.7 is no longer maintained. 
pip 21.0 will drop support for Python 2.7 in January 2021. 
More details about Python 2 support in pip can be found at 
https://pip.pypa.io/en/latest/development/release-process/#python-2-support 
pip 21.0 will remove support for this functionality.
'''
