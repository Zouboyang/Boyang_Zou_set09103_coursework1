from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', username=request.args.get('username'))

@app.route('/guitarist')
def guitarist():
    return render_template('page1.html')

@app.route('/guitarist/Paul/')
def guitarist_1():
    return render_template('people1.html')

@app.route('/guitarist/Hendrix/')
def guitarist_2():
    return render_template('people2.html')

@app.route('/guitarist/Atkins/')
def guitarist_3():
    return render_template('people3.html')

@app.route('/guitarist/Tedesco/')
def guitarist_4():
    return render_template('people4.html')

@app.route('/guitarist/Christian/')
def guitarist_5():
    return render_template('people5.html')

@app.route('/guitarist/Red/')
def guitarist_6():
    return render_template('people6.html')

@app.route('/guitarist/Berry/')
def guitarist_7():
    return render_template('people7.html')


@app.route('/picture')
def picture():
    return render_template('page2.html')

@app.route('/introduction')
def introduction():
    return render_template('page3.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']=='Zouboyang' and request.form['password']=='zby962311':                    
            return redirect(url_for('index', username=request.form['username']))
        else:
            error = "Invalid password or password"
    return render_template('login.html',error=error)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)





