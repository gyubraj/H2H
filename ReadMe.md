## H2H

1. Do following to setup this project.

   In Terminal after going to the project directory.

```cmd
python3 -m venv venv

venv\Scripts\python

pip install -r requirements.txt

```

You need to chnage some code. Enter Email Address and Password so 

```
Goto H2H/settings.py line 99 and 100 and chnage it to your email and password
```

Then 
```

python manage.py migrate

python manage.py runserver
```
