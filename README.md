# GoshadPy
Powered by Cookiecutter, Goshadpy is a framework for jumpstarting production-ready Django projects quickly.

## Usage
Let's pretend you want to create a Django project called "Potato". Rather than using startproject and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter to do all the work.



First install cookiecutter.
```
pip install cookiecutter
```

Now run it against this repo:
```
cookiecutter https://github.com/mohammadrezasolo69/GoshadPy
```

You'll be prompted for some values. Provide them, then a Django project will be created for you.


## Manual
First create virtualenv :
```
python3 -m venv venv
```

activated :
```
source venv/bin/activate
```

Now install requirement :
```
pip install -r requirements/requirements_local.txt
```

run command :
```
./manage.py migrate
./manage.py runserver --settings=core.settings.local
```


## Point
After creating the project, don't forget to add the `core/.env` file to `.gitignore`
