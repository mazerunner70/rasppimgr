# Notes on creating a simple Raspberry PI manager

Things to test:
1. Simple python based rest server
1. Simple React based client
1. Tool for downloading raspbian images 
1. Tool for burning images to sd card
1. Tool for post burn edits to running pi


GFM notes
* [intro](https://guides.github.com/features/mastering-markdown/)

# Python based rest server
* Use Django https://www.djangoproject.com/

Deploy server through docker and kubernetes

1. Deploy sample app through kubernetes
1. Deploy simple react app to access it


## Deploy sample app through kubernetes
1. Do sample Django app provided
1. Deploy it through docker
1. use kubernets to control it

### Do sample Django app provided

Based in dir poc/sampledjango

#### Using a virtual env
As django is a python lib I want to keep it isolated from other python on my machine, so using virtualenv
https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv
Don't forget to activate and deactivate the venvs! This will neeed you to be in bash shell
Tags of milestones in git
Tag | Milestone
poc-v0.1 | part one tutorial complete: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

## Deploy it through docker
https://docs.docker.com/compose/django/

* If a docker image doesn;t work correctly find an image that worked and run it directly and then inspect files system etc to see the problem.
* Use command: docker run --rm -it <<image id>> bash
* Use docker-compose build, up to rebuild while in dev/test

 



