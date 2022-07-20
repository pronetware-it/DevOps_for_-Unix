# Task #
Using docker lection2 create a docker image with Python Flask app that displays random cat pix.



## Install docker on Ubuntu 20.04 server ##

1 `sudo apt-get update`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/apt-update.gif)

2 `sudo apt install -y ca-certificates curl gnupg lsb-release`

3 ```sudo mkdir -p /etc/apt/keyrings
     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

4 ```echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

5 ```sudo apt-get update
     sudo apt-get install docker-ce docker-ce-cli containerd.io
```


6 `docker --version`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/docker/docker-v.gif) 

7 `sudo usermod -aG docker serhii_rozhko`


