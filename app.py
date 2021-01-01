from flask import Flask,redirect,render_template,url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)