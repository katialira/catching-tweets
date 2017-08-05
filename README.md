# Catching-tweets
2017 DjangoCon Us Tutorial

### Includes
* Twitter bootstrap 3
* django-annoying
* django-compressor
* Django Rest Framework
* Tweepy

### How to use
Create virtual environment, change project_name with your projects name :D
```sh
mkvirtualenv project_name
```

Install django
```sh
pip install Django
```

Run django startproject with the --template option
```sh
django-admin.py startproject --template=https://github.com/katialira/catching-tweets/archive/master.zip project_name
```

Install requirements, for development
```sh
pip install -r requirements.txt
```

Set 'PROJECT_ENV' environment variable.
* 'development'
* 'production',
* 'staging'

If no 'PROJECT_ENV' especified takes 'development' settings as default

For development environment:
```sh
sudo sh -c 'echo "export PROJECT_ENV=development" >> /etc/profile.d/environment.sh' && source /etc/profile.d/environment.sh
```
Done.