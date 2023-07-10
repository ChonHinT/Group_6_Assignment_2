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


(install django for the first time)
pip install django 
* may also need to install Pillow (pip install Pillow)

(run server)
python3 manage.py runserver  

(To access admin page)
http://127.0.0.1:8000/admin/
username: admin
password: password

-----------------------------------------------------------------
Version:
Latest: 10th July - So far, the webpage has different items with their belonged category, can add items into basket, browse products (Calvin)

Details: In this project, you will develop an e-commerce platform that allows users to 
1. browse products (done)
2. add items to their shopping cart (done)
3. securely make purchases. 

You will need to ensure that your platform is secure from command injection attacks, which occur when an attacker injects malicious code into a system through a command injection vulnerability. 
You will also need to ensure that all user data, including personal and financial information, is stored securely.
