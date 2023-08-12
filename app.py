import email
from unittest import result
from urllib.error import HTTPError
import bottle
import bottle.ext.sqlite
from bottle import get, post, request

# Sean Skinner
# CptS 327
# SQL Injection Project
#
# TO DO List
#   Add encryption to database passwords (should be easy to break on easier levels of security)
#       Side Note: Might give timetables to break hashes with at higher levels of security instead of actually cracking them.
#
#   Implement Low, Medium, High, and Impossible Security levels to try and break
#       In addition explain these protections and their vulnerabilities
#       Easy level should not be blind injection while higher levels should be blind
#   
#   Refactor code base to make it cleaner and easier to read and write
#
#   Add testing capabilities



app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='Users.db')
app.install(plugin)


@app.route('/')
def index():
    #Home Page to navigate the website
    print("On the home web page")
    html =  """<h1>Home Page</h1>
            <a href='/SQL/Easy'>Easy SQL Injection </a>
            <br><a href='/SQL/Medium'>Medium SQL Injection </a>
            <br><a href='/SQL/Hard'>Hard SQL Injection </a>
            <br><a href='/SQL/Impossible'>Impossible SQL Injection </a>
            <br><a href ='/DBview'>Go to database preview </a>"""
    # Give options for the user to navigate to new pages
    return html 

# Route that will lead to easy level SQL injection protections
@app.route('/SQL/<id>')
def SQLEasy(id):
    print("On SQL Injection Page level " + id)
    html =  """<h1>Viewing the SQL Injection """+ id +""" Page </h1> 
            <a href='/'>Go to Home Page </a>"""
    #Return to the home page
    return html

# Route that will lead to easy level SQL injection protections
@app.route('/SQL/Easy')
def SQLEasy():
    print("On SQL Injection Page level Easy")
    return  """<h1>Viewing the SQL Injection Easy Page </h1><br>
                <form action="/SQL/Easy" method="post">
                    Username: <input name="username" type="text" />
                    Password: <input name="password" type="password" />
                    <input value="Login" type="submit" />

                </form><br>
            <a href='/'>Go to Home Page </a>"""
@app.post('/SQL/Easy')
def doSQLEasy(db):
    print("On the SQL injection Easy Post")
    username = request.forms.get('username')
    password = request.forms.get('password')
    sql_statement = "SELECT * FROM Users WHERE User = '{username}' AND (Password = '{password}')"
    user = db.execute(sql_statement.format(username=username, password=password)).fetchone()

    if(user):
        name = user[0]
        password = user[1]
        id = str(user[2])
        email = user[3]
        return """<h1>Username is: """ + name + """<br>password is: """ + password + """
         <br>id is: """ + id + """<br>email is: """ + email + """</h1>
         <br><a href='/'>Go to Home Page </a>"""
    return "<h1> Error </h1>"

# Route that will lead to medium level SQL injection protections
@app.route('/SQL/Medium')
def SQLMedium():
    print("On SQL Injection Page level Medium")
    return  """<h1>Viewing the SQL Injection Medium Page </h1>
                <form action="/SQL/Medium" method="post">
                    Username: <input name="username" type="text" />
                    Password: <input name="password" type="password" />
                    <input value="Login" type="submit" />

                </form><br> 
            <a href='/'>Go to Home Page </a>"""

@app.post('/SQL/Medium')
def doSQLMedium(db):
    print("On the SQL injection Medium Post")
    username = request.forms.get('username')
    password = request.forms.get('password')
    sql_statement = "SELECT * FROM Users WHERE User = '{username}' AND (Password = '{password}')"
    user = db.execute(sql_statement.format(username=username, password=password)).fetchone()

    if(user):
        name = user[0]
        password = user[1]
        id = str(user[2])
        email = user[3]
        return """<h1>Username is: """ + name + """<br>password is: """ + password + """
         <br>id is: """ + id + """<br>email is: """ + email + """</h1>
         <br><a href='/'>Go to Home Page </a>"""
    return "<h1> Error </h1>"

# Route that will lead to hard level SQL injection protections
@app.route('/SQL/Hard')
def SQLhard():
    print("On SQL Injection Page level Hard")
    html =  """<h1>Viewing the SQL Injection Hard Page </h1> 
                <form action="/SQL/Hard" method="post">
                    Username: <input name="username" type="text" />
                    Password: <input name="password" type="password" />
                    <input value="Login" type="submit" />


                </form><br>
            <a href='/'>Go to Home Page </a>"""
    #Return to the home page
    return html
@app.post('/SQL/Hard')
def doSQLHard(db):
    print("On the SQL injection Hard Post")
    username = request.forms.get('username')
    password = request.forms.get('password')
    sql_statement = "SELECT * FROM Users WHERE User = '{username}' AND (Password = '{password}')"
    user = db.execute(sql_statement.format(username=username, password=password)).fetchone()

    if(user):
        name = user[0]
        password = user[1]
        id = str(user[2])
        email = user[3]
        return """<h1>Username is: """ + name + """<br>password is: """ + password + """
         <br>id is: """ + id + """<br>email is: """ + email + """</h1>
         <br><a href='/'>Go to Home Page </a>"""
    return "<h1> Error </h1>"

# Route that will lead to impossible level SQL injection protections
@app.route('/SQL/Impossible')
def SQLEasy():
    print("On SQL Injection Page level Impossible")
    return  """<h1>Viewing the SQL Injection Impossible Page </h1> 
                <form action="/SQL/Impossible" method="post">
                    Username: <input name="username" type="text" />
                    Password: <input name="password" type="password" />
                    <input value="Login" type="submit" />

                </form><br>
            <a href='/'>Go to Home Page </a>"""

@app.post('/SQL/Impossible')
def doSQLImpossible(db):
    print("On the SQL injection Impossible Post")
    username = request.forms.get('username')
    password = request.forms.get('password')
    sql_statement = "SELECT * FROM Users WHERE User = '{username}' AND (Password = '{password}')"
    user = db.execute(sql_statement.format(username=username, password=password)).fetchone()

    if(user):
        name = user[0]
        password = user[1]
        id = str(user[2])
        email = user[3]
        return """<h1>Username is: """ + name + """<br>password is: """ + password + """
         <br>id is: """ + id + """<br>email is: """ + email + """</h1>
         <br><a href='/'>Go to Home Page </a>"""
    return "<h1> Error </h1>"

#Route used to test database connection, will become obselete and removed later
@app.route('/DBview')
def DBview(db):
    username = "Alex"
    sql_statement = "SELECT * FROM Users WHERE User = '{username}'"
    user = db.execute(sql_statement.format(username=username)).fetchone()
    if(user):
        name = user[0]
        password = user[1]
        id = str(user[2])
        email = user[3]

        print("successfully pulled from database")
        return """<h1>Username is: """ + name + """<br>password is: """ + password + """
         <br>id is: """ + id + """<br>email is: """ + email + """</h1>
         <br><a href='/'>Go to Home Page </a>"""
    return "<h1> Error </h1>"

if __name__ == '__main__':
    app.run(debug=True, reloader=True)
