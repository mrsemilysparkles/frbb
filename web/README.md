# Development Guide
The development environment depends on the installation of [Docker and docker-compose](https://docs.docker.com/compose/install/) simplifying deployment and dependency management.

## Overview of Development Environment
The FRBB Web component is built ontop of [Django](https://www.djangoproject.com/) and several dependencies. To speed development and future deployments, FRBB now runs within a Docker Container and is easily built using a single `docker-compose` command. This `docker-compose` command builds a new docker image 'frbb' with dependencies installed, and uses the local `frbb/web` directory for the applications files. This means any local changes made will be reflected in the frbb container running locally on your machine.

huh? 

After running `sudo docker-compose up` the FRBB application will be available at http://localhost:8000/frbb

The FRBB application is running within a docker container that has all the dependencies installed and your local directory: `frbb/web/`, serves as the context root of the web application.

## Setup of FRBB Web Development 

**Get code, build environment, and launch server**
```
git clone https://github.com/seriouscamp/frbb.git
cd frbb/web
sudo docker-compose up -d
```





