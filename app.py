from flask import Flask,redirect,render_template,url_for, session, request, flash
import json
import os
from flask_mysqldb import MySQL
import MySQLdb.cursors
from passlib.hash import sha256_crypt

app = Flask(__name__)

with open("db.json","r") as f:
    data= json.load(f)["data"]

app.secret_key= os.urandom(24)
app.config['MYSQL_HOST'] = data["host"]
app.config['MYSQL_USER'] = data["db_user"]
app.config['MYSQL_PASSWORD'] = data["password"]
app.config['MYSQL_DB'] = data["db_name"]
app.config['MYSQL_PORT'] = data["port"]

mysql = MySQL(app)


@app.route('/admreg')
def admreg():
    return render_template('admreg.html')

@app.route('/staffreg')
def staffreg():
    return render_template('staffreg.html')

@app.route('/carreg')
def carreg():
    return render_template('regcar.html')

@app.route('/usereg')
def usereg():
    return render_template('userreg.html')


@app.route('/onlinereg')
def onlinereg():
    return render_template('onlinebook.html')

@app.route('/admlog')
def admlog():
    return render_template('admlog.html')

@app.route('/stafflog')
def stafflog():
    return render_template('stafflog.html')

@app.route('/userlog')
def userlog():
    return render_template('userlog.html')

@app.route('/admin_data', methods=['POST'])
def admin_data():
    if request.method == 'POST':
        email = request.form['mail']
        name = request.form['nam']
        pas = request.form['pass']
        rpas = request.form['repass']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute("select email from admin where email=%s",(email,))
        result = db.fetchone()
        if result is not None:
            flash("Email already taken", "error")
            db.close()
            return redirect(url_for('admreg'))
        else:
            if pas == rpas:
                hash_pas = sha256_crypt.hash(pas)
                db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                db.execute("INSERT INTO admin (email,name,password) VALUES (%s,%s,%s)",(email,name,hash_pas))
                mysql.connection.commit()
                db.close()
                return render_template('admreg.html')
            else:
                flash("Password did not match", "error")
                return redirect(url_for('admreg'))
    else:
        flash("Some error occured try again","error")
        return redirect(url_for('admreg'))

@app.route('/staff_data',methods=['POST'])
def staff_data():
    if request.method == 'POST':
        name = request.form['nam']
        mail = request.form['mail']
        phone = request.form['phone']
        pas = request.form['pass']
        rpas = request.form['repass']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute("select email from staff where email=%s",(mail,))
        result = db.fetchone()
        if result is not None:
            flash("Email already taken","error")
            db.close()
            return redirect(url_for("staffreg"))
        else:
            if pas == rpas:
                hash_pas = sha256_crypt.hash(pas)
                db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                db.execute("insert into staff (name,email,phone,password) values(%s,%s,%s,%s)",(name,mail,phone,hash_pas))
                mysql.connection.commit()
                db.close()
                return render_template('staffreg.html')
            else:
                flash("Password did not match", "error")
                return redirect(url_for('staffreg'))
    else:
        flash("Some error occured try again","error")
        return redirect(url_for('staffreg'))

@app.route('/admin_log', methods=['POST'])
def admin_log():
    if request.method == 'POST':
        mail = request.form['mail']
        pas = request.form['pass']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute("select * from admin where email=%s",(mail,))
        result = db.fetchone()
        db.close()
        if result is not None:
            dec_hash = sha256_crypt.verify(pas,result["password"])
            if dec_hash == True:
                session["email"] = result['email']
                session["name"] = result["name"]
                return render_template('staffreg.html')
            else:
                flash("Password incorrect","error")
                return redirect(url_for('admlog'))
        else:
            flash("Email not found", "error")
            return redirect(url_for('admlog'))

    else:
        flash("Some error occured try again", "error")
        return redirect(url_for('admlog'))

if __name__ == '__main__':
    app.run(debug=True)