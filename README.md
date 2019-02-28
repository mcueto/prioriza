# prioriza

prioriza is an app that lets groups of people prioritize it's ideas based on a budget, options and cost for each of it's options.

Speed up your proyects and get things done democratically with prioriza.


## Deploy to Heroku
With the following button you can get yout prioriza instance up and running quickly, just click the button, configure your environment variables(on heroku's website) and voila.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/mcueto/prioriza/)


## Project requirements
This projects uses:
- Python 3
- Django 2
- Vuejs 2
- js-data 3 with httpAdapter
- Bootstrap 4
- FontAwesome 5

## Deploying on local machine
```
NOTE: i'm assuming you have python3, virtualenvwrapper and a running postgresql instance
```

To deploy in your local machine you must follow the following steps:
- Clone the repo
``` shell
https://github.com/mcueto/prioriza/
```
- Get into repo folder
``` shell
cd prioriza
```
- Create virtual environment
``` shell
mkvirtualenv -p `which python3` prioriza
```
- Activate environment variables(modify setenvvars.sh file to fit your settings)
``` shell
source setenvvars.sh
```
- Execute migrations
``` shell
python manage.py migrate
```
- Run the server
``` shell
python manage.py runserver
```
- Visit http://127.0.0.1:8000
