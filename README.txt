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

10th July - So far, the webpage has different items with their belonged categories, can add items into basket (Calvin)
