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
Version:
Old: 10th July - So far, the webpage has different items with their belonged category, can add items into basket, browse products (Calvin)
Latest: 22nd July - added create User and login function & payment (Calvin)

Details: In this project, you will develop an e-commerce platform that allows users to 
1. browse products (done)
2. add items to their shopping cart (done)
3. securely make purchases (should be done, not sure)

You will need to ensure that your platform is secure from command injection attacks, which occur when an attacker injects malicious code into a system through a command injection vulnerability. 
You will also need to ensure that all user data, including personal and financial information, is stored securely.
