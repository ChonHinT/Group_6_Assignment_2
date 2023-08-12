This project is an e-commerce platform for Adelaide BookStore.
It allows customer to search products, add selected products to shopping basket.
Register customers are able to checkout securely.

---------------------------------------------------------
How to run the application
---------------------------------------------------------

Install virtual environment
(Mac user) python3 -m pip install virtualenv

You need to create vitural environment
(Mac user) python3 -m venv venv

(activate vitural environment, also Mac user)
source venv/bin/activate 

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
Starting development server at http://127.0.0.1:8000/

---------------------------------------------------------

After creating a testing account:
the acivation email with link will be found in the termial for testing virtual environment

---------------------------------------------------------

We refer to this Youtube tutorial to learn how to build an e-commerce platform 
https://www.youtube.com/watch?v=VOwfGW-ZTIY&t=660s
