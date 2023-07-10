You need to create vitural environment
(mac user) python3 -m venv venv


(activate vitural environment)
source venv/bin/activate 

(run server)
pip install django 
* may also need to install Pillow (pip install Pillow)
python3 manage.py makemigrations
python3 manage.py migrate 
python3 manage.py runserver  

http://127.0.0.1:8000/admin/
username: admin
password: password

(tutorial)
https://www.youtube.com/watch?v=VOwfGW-ZTIY&t=660s

Latest version
10th July - So far, the webpage has different items with their belonged category, can add items into basket (Calvin)

Details: In this project, you will develop an e-commerce platform that allows users to 
1. browse products
2. add items to their shopping cart (done)
3. securely make purchases. 

You will need to ensure that your platform is secure from command injection attacks, which occur when an attacker injects malicious code into a system through a command injection vulnerability. You will also need to ensure that all user data, including personal and financial information, is stored securely.
