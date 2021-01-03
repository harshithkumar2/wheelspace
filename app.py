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

@app.route('/dash_staff')
def dash_staff():
    if "staff" in session and session["staff"] == True:
        return render_template('dash_staff.html')
    else:
        return redirect(url_for('stafflog'))

@app.route('/dash_admin')
def dash_admin():
    if "admin" in session and session["admin"] == True:
        return render_template('dash_admin.html')
    else:
        return redirect(url_for('admlog'))

@app.route('/dash_user')
def dash_user():
    if "user" in session and session["user"] == True:
        return render_template('dash_user.html')
    else:
        return redirect(url_for('userlog'))

@app.route('/search_results')
def search_results():
    return render_template('search_results.html')

@app.route('/carreg')
def carreg():
    if "staff" in session or "admin" in session:
        return render_template('regcar.html')
    else:
        return redirect(url_for('stafflog'))

@app.route('/regular_user')
def regular():
    return render_template('regular_user.html')

@app.route('/usereg')
def usereg():
    return render_template('userreg.html')


@app.route('/onlinereg')
def onlinereg():
    return render_template('onlinebook.html')

@app.route('/admlog')
def admlog():
    return render_template('admlog.html')

@app.route("/onlines_list")
def onlines_list():
    return render_template("onlines_list.html")

@app.route('/stafflog')
def stafflog():
    return render_template('stafflog.html')

@app.route('/userlog')
def userlog():
    return render_template('userlog.html')

@app.route('/admin_data', methods=['POST'])          #admin registration data
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

@app.route('/staff_data',methods=['POST'])            #staff registration form data
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

@app.route('/off_data',methods=['POST'])  # first time offline data registration
def off_data():
    if request.method == 'POST':
        name = request.form['nam']
        mail = request.form['mail']
        phone = request.form['phone']
        vech_no = request.form['vech_no']
        vech_type = request.form['vech_type']
        lic_no = request.form['lic_no']
        duration = request.form['dur']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute("select license_no from offline_user where license_no=%s",(lic_no,))
        result = db.fetchone()
        #print(result)
        if result is not None:
            flash("License Number used","error")
            db.close()
            return redirect(url_for('carreg'))
        else:
            db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            db.execute("select email from offline_user where email=%s", (mail,))
            result1 = db.fetchone()
            if result1 is not None:
                flash("Email already used","error")
                db.close()
                return redirect(url_for('carreg'))
            else:

                db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                db.execute("insert into offline_user values (%s,%s,%s,%s,%s,%s,%s)",(lic_no,name,mail,phone,vech_no,vech_type,duration))
                mysql.connection.commit()
                db.close()
                flash("Data inserted successfully","success")
                return redirect(url_for('dash_staff'))
    else:
        flash("some error occured","error")
        return redirect(url_for('stafflog'))


@app.route('/off_extend_data', methods=["POST"])  #for multiple offline booking
def off_extend_user():
    if request.method == 'POST':
        lic_no = request.form['lic_no']
        date = request.form['dat']
        duration = request.form['dur']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #db.execute("select license_no from offline_user where license_no=%s",(lic_no,))
        #result = db.fetchone()
        try:
            db.execute("insert into offline_extended (license_no,dates,duration)values (%s,%s,%s)",(lic_no,date,duration))
            mysql.connection.commit()
            db.close()
            flash("Parking Booked Successfully","success")
            return redirect(url_for('dash_staff'))
        except MySQLdb._exceptions.IntegrityError:  #since license no is primary key in offline_user and foreign key in offline_extended table both license no should match
            flash("Insert a valid license number","error")
            return redirect(url_for('regular'))
    else:
        flash("Some error occured", "error")
        return redirect(url_for('stafflog'))


@app.route('/admin_log', methods=['POST'])  #admin login
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
                session["admin"] = True
                return redirect(url_for('dash_admin'))
            else:
                flash("Password incorrect","error")
                return redirect(url_for('admlog'))
        else:
            flash("Email not found", "error")
            return redirect(url_for('admlog'))

    else:
        flash("Some error occured try again", "error")
        return redirect(url_for('admlog'))

@app.route('/staff_log',methods=['POST']) #staff login
def staff_log():
    if request.method == 'POST':
        mail = request.form['mail']
        pas = request.form['pass']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute("select * from staff where email=%s",(mail,))
        result=db.fetchone()
        db.close()
        if result is not None:
            pas_verify = sha256_crypt.verify(pas,result["password"])
            if pas_verify ==True:
                session["staff_mail"] = result["email"]
                session["staff_name"] = result["name"]
                session["staff"] = True
                flash(f"logged in as {result['name']}","success")
                return redirect(url_for('dash_staff'))
            else:
                flash("Password did not match","error")
                return redirect(url_for('stafflog'))
        else:
            flash("Email not found","error")
            return redirect(url_for('stafflog'))
    else:
        session.clear()
        flash("Some error occured","error")
        return redirect(url_for('stafflog'))


@app.route('/search_data', methods=['POST'])  #to search users license no and book slot for offline users
def search_data():
    if request.method == 'POST':
        query = request.form['search']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute("select * from offline_user where license_no=%s",(query,))
        result = db.fetchone()
        db.close()
        return render_template('search_results.html',data=result)

@app.route('/book/<string:id>')  #books slot for offlne users
def book(id):
    d = id
    db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    db.execute("select license_no from offline_user where license_no=%s",([d]))  #[d] bcz tuple is not iteratable so used list to traverse
    result = db.fetchone()
    db.close()
    if result is not None:
        return render_template('regular_user.html',data = result)
    else:
        return redirect(url_for('stafflog'))

@app.route("/online_data",methods=['POST'])          #online user registration
def online_data():
    if request.method == 'POST':
        name = request.form['nam']
        email = request.form['mail']
        phone = request.form['phone']
        lic_no = request.form['lic_no']
        pas = request.form['pass']
        rpas = request.form['repass']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute("select email from online_user where license_no=%s",(lic_no,))
        result = db.fetchone()
        db.close()
        if result is not None:
            flash("License number is already used","error")
            return redirect(url_for('usereg'))
        else:
            db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            db.execute("select email from online_user where email=%s", (email,))
            result = db.fetchone()
            db.close()
            if result is not None:
                flash("Email is already used", "error")
                return redirect(url_for('usereg'))
            else:
                if pas == rpas:
                    hash_pas = sha256_crypt.hash(pas)
                    db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    db.execute("insert into online_user values(%s,%s,%s,%s,%s)",(lic_no,name,email,phone,hash_pas))
                    mysql.connection.commit()
                    db.close()
                    flash("Registration successfull","success")
                    return redirect(url_for('userlog'))
                else:
                    flash("Password did not match","error")
                    return redirect(url_for("usereg"))
    else:
        flash("Some error occured", "error")
        return redirect(url_for("usereg"))

@app.route("/user_log",methods=["POST"])      #online user login
def user_log():
    if request.method == 'POST':
        email = request.form['mail']
        pas = request.form['pass']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute("select * from online_user where email=%s",(email,))
        result = db.fetchone()
        db.close()
        if result is not None:
            pas_verify = sha256_crypt.verify(pas, result["password"])
            if pas_verify == True:
                session["user_name"] = result["name"]
                session["user_mail"] = result['email']
                session["user"] = True
                session["lic_no"] = result["license_no"]
                flash(f"logged in as {result['name']}","success")
                return redirect(url_for("dash_user"))
            else:
                flash("Password did not match", "error")
                return redirect(url_for("userlog"))
        else:
            flash("Email not found", "error")
            return redirect(url_for("userlog"))
    else:
        flash("Some error occured", "error")
        return redirect(url_for("userlog"))

@app.route("/booking/<id>") # online user booking
def booking(id):
    if "user" in session and session["user"] == True:
        data = id
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute("select license_no from online_user where license_no=%s",(data,))
        result = db.fetchone()
        db.close()
        if result is not None:
            return render_template("onlinebook.html", dat = result["license_no"])
        else:
            flash("Some error occured try again","error")        #if he uses to enter his own or other lic no in url provides error
            session.clear()
            return redirect(url_for('userlog'))

    else:
        session.clear()
        flash("Some error occured try again", "error")
        return redirect(url_for('userlog'))


@app.route("/confirm_booking",methods=["POST"])  # inserting vehicle details to db of online user after log in
def confirm_booking():
    if "user" in session and session["user"] == True:
        if request.method == 'POST':
            vech_no = request.form["vech_no"]
            vech_type = request.form["vech_type"]
            lic_no = request.form["lic_no"]
            duration = request.form["dur"]
            date = request.form["dat"]
            db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            db.execute("insert into online_booking (license_no,vech_no,vech_type,duration,dates) values (%s,%s,%s,%s,%s)",(lic_no,vech_no,vech_type,duration,date))
            mysql.connection.commit()
            db.close()
            flash("Parking booked successfully","success")
            return redirect(url_for("dash_user"))
        else:
            session.clear()
            flash("some error occured", "error")
            return redirect(url_for("userlog"))
    else:
        session.clear()
        flash("some error occured","error")
        return redirect(url_for("userlog"))

@app.route("/online_list",methods=["POST","GET"])
def online_list():
    db=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    db.execute("select * from online_booking order by dates desc")
    result = db.fetchall()
    db.close()
    if result is not None:
        return render_template("onlines_list.html", data=result)

@app.route('/logout_admin')
def logout():
    session.clear()
    return redirect(url_for('admlog'))

@app.route('/logout_staff')
def logout_staff():
    session.clear()
    return redirect(url_for('stafflog'))

@app.route('/logout_user')
def logout_user():
    session.clear()
    return redirect(url_for('userlog'))




if __name__ == '__main__':
    app.run(debug=True)