# prioriza

prioriza is an app that lets groups of people prioritize it's ideas based on a budget, options and cost for each of it's options.

Speed up your proyects and get things done democratically with prioriza.


## Deploy to Heroku
With the following button you can get yout prioriza instance up and running quickly, just click the button, configure your environment variables(on heroku's website) and voila.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/mcueto/prioriza/)

**NOTE:** In order to get it working properly, your `APP_HOST` environment variable MUST be the same that your project url(eg: `prioriza.herokuapp.com`)

---

## Project requirements
This projects uses:
- Python 3
- Django 2
- Vuejs 2
- js-data 3 with httpAdapter
- Bootstrap 4
- FontAwesome 5

---

## Deploying on local machine
**NOTE:** i'm assuming you have python3, virtualenvwrapper and a running postgresql instance called prioriza with user='prioriza' password='prioriza') running on 127.0.0.1:5432 to create this instance with docker, just run:
``` shell
docker run --name prioriza -e POSTGRES_USER=prioriza -p 5432:5432 -d postgres:10
```

---

To deploy in your local machine you must follow the following steps:
- Clone the repo
``` shell
git clone https://github.com/mcueto/prioriza/
```
- Get into repo folder
``` shell
cd prioriza
```
- Create virtual environment
``` shell
mkvirtualenv -p `which python3` prioriza
```
- Install requirements
``` shell
pip install -r requirements.txt
```
- Activate environment variables(modify setenvvars.sh file to fit your settings)
``` shell
source setenvvars.sh
```
- Execute migrations
``` shell
python manage.py migrate
```
- Create default user(admin user):

  username:`prioriza`

  password:`aziroirp`
``` shell
python manage.py runscript create_default_user
```
- Run the server
``` shell
python manage.py runserver
```
- Visit http://127.0.0.1:8000
