(tutorial)
https://www.youtube.com/watch?v=VOwfGW-ZTIY&t=660s

---------------------------------------------------------

install virtual environment
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

(run server)
python3 manage.py runserver  

(To access admin page)
http://127.0.0.1:8000/admin/
email: admin1@gmail.com
password: password

You may want to create another admin account: then run
python3 manage.py createsuperuser

-----------------------------------------------------------------
Maybe useful for prevention

MFA 
1. https://dev.to/arnopretorius/multi-factor-authentication-mfa-for-your-django-admin-page-4ec9

2. Security in Django 
https://docs.djangoproject.com/en/4.2/topics/security/

-----------------------------------------------------------------

Things need to reinforce: 
1. admin password no restriction (admin password can be password, may fix it similar to user registration, using strong password)
2. two-factor authentication
3. restrict limit of attempt, like after 3-5 times wrong password then block 5 mins to re-try again

-----------------------------------------------------------------

Version:
Old: 10th July - So far, the webpage has different items with their belonged category, can add items into basket, browse products (Calvin)
Old: 22nd July - added create User and login function & payment (Calvin)
Old: 25th July - reinforced password requirement when user register an account (Calvin)
Latest: 1st Aug - hashed password reinforcement

Details: In this project, you will develop an e-commerce platform that allows users to 
1. browse products (done)
2. add items to their shopping cart (done)
3. securely make purchases (should be done, not sure)

You will need to ensure that your platform is secure from command injection attacks, which occur when an attacker injects malicious code into a system through a command injection vulnerability. 
You will also need to ensure that all user data, including personal and financial information, is stored securely.

