from flask import Flask, redirect , url_for , request
app = Flask(__name__)
@app.route('/confirm/<name>/<passw>')
def confirm(name,passw):
    dic = {'pani' : '2561' , 'dhoni' : '4101' , 'cred' : 'hell' }
    if name in dic:
        if dic.get(name) == passw:
            return 'WELCOME %s' %name
        else:
            return 'Wrong Password'
    else:
        return 'User Name Not Found'
 
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        password = request.form['ps']
        return redirect(url_for('confirm',name = user, passw = password))
    else:
        user = request.args.get('nm')
        password = request.args.get('ps')
        return redirect(url_for('confirm',name = user, passw = password))
if __name__ == '__main__': 
   app.run(debug = True) 