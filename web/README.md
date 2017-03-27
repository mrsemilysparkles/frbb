# Development Guide
The development environment depends on the installation of [Docker and docker-compose](https://docs.docker.com/compose/install/) simplifying deployment and dependency management.

## Setup of FRBB Web Development 
The FRBB Web component is built ontop of [Django](https://www.djangoproject.com/) and several dependencies. To speed development and future deployments, FRBB now runs within a Docker Container and is easily built using a single `docker-compose` command.

**Pull the latest code from GitHub**
```git clone https://github.com/seriouscamp/frbb.git```

**Build and launch a development container**
```
cd frbb/web
sudo docker-compose up -d
```




