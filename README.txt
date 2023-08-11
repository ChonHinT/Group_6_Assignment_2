Install virtual environment
(Mac user) python3 -m pip install virtualenv

You need to create vitural environment
(Mac user) python3 -m venv venv

(activate vitural environment, also Mac user)
source venv/bin/activate 

More info about install and activate virtual environment, view the link below:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

---------------------------------------------------------

(install packages)
pip install django 
pip install Pillow
pip install django-country2
pip install stripe
pip install six
pip install django-axes (after installed this, may need to migrate axes --> python3 manage.py migrate)
pip install django-recaptcha

(run server)
python3 manage.py runserver  

---------------------------------------------------------

We refer to this Youtube tutorial to learn how to build an e-commerce platform 
https://www.youtube.com/watch?v=VOwfGW-ZTIY&t=660s
