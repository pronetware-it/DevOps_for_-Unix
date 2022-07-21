# Task #
Using docker lection2 create a docker image with Python Flask app that displays random cat pix.

0 - Structure app

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/structure-app.png)

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
```

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/content-app.gif)

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
- `docker images`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/docker-build.gif)

- Not a mistake, but a warning

```
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020.
Please upgrade your Python as Python 2.7 is no longer maintained. 
pip 21.0 will drop support for Python 2.7 in January 2021. 
More details about Python 2 support in pip can be found at 
https://pip.pypa.io/en/latest/development/release-process/#python-2-support 
pip 21.0 will remove support for this functionality.
```

9 - Docker run 

- `docker run -d -p 8888:5000 --name mycatapp serhii_rozhko/mycatapp`

- `docker ps`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/docker-run.gif)


10 - Result

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/docker-run-result.gif)


11 - Login on docker hub

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/docker-login.gif)

12 - Docker push images

- `docker tag serhii_rozhko/mycatapp pronetwareit/mycatapp`

- `docker push pronetwareit/mycatapp`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/docker-push-result.png)

- ![Link on Docker Hub](https://hub.docker.com/repository/docker/pronetwareit/mycatapp)


