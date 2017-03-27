# Development Guide
The development environment depends on the installation of [Docker and docker-compose](https://docs.docker.com/compose/install/) simplifying deployment and dependency management.

## Overview of Development Environment
The FRBB Web component is built ontop of [Django](https://www.djangoproject.com/) and several dependencies. To speed development and future deployments, FRBB now runs within a Docker Container and is easily built using a single `docker-compose` command. This `docker-compose` command builds a new docker image 'frbb' with dependencies installed, and uses the local `frbb/web` directory for the application's files. This means any local changes made will be reflected in the frbb container running locally on your machine.

huh? 

After running `sudo docker-compose up -d` the FRBB application will be available at http://localhost:8000/frbb

The FRBB application is running within a docker container that has all the dependencies installed, and your local directory: `frbb/web/`, serves as the context root of the web application.

## Setup of FRBB Web Development 

**Get code, build environment, and launch server**
```
git clone https://github.com/seriouscamp/frbb.git
cd frbb/web
sudo docker-compose up -d
```
**Watch Django Web Logs**
```
cd frbb/web
sudo docker-compose logs -f
```

**Shutdown environment**
```
cd frbb/web
sudo docker-compose stop
```

**Delete Environment**
```
cd frbb/web
sudo docker-compose rm
```

**See runing containers**
```
sudo docker ps
```

## Available Pages
Currently the css styling and buttons are missng :anguished: and I don't understand why. This makes the site painfully hard to navigate. 
* http://localhost:8000/frbb/login
* http://localhost:8000/frbb/register
* http://localhost:8000/frbb/dashboard
* http://localhost:8000/frbb/deposit
* http://localhost:8000/frbb/withdraw
* http://localhost:8000/frbb/logout


## Adding new python dependencies
Dependencies are built into the frbb container created with `sudo docker-compose up -d` to install a new dependency the old environment must be stopped if running and deleted `sudo docker-compose stop` followed by `sudo docker-compose rm`.  Add a new line to the `frbb/web/requirements.txt` file then issue `sudo docker-compose up -d` to build a new development environment with the additional dependency.






