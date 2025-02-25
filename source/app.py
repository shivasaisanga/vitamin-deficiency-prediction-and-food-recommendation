import os
import MySQLdb
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import db_connect
from database import db_connect,vit_act,view_vit,user_reg,user_loginact,user_viewimages,vit_info,get_recomendations,getdisease_recomendations
from database import db_connect 
from werkzeug.utils import secure_filename

 

app = Flask(__name__)
app.secret_key = os.urandom(24)
PEOPLE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route("/")
def FUN_root():
    return render_template("index.html")

@app.route("/index.html")
def logout():
    return render_template("index.html")

# @app.route("/upload.html")
# def upload():
#     return render_template("upload.html")

@app.route("/register.html")
def reg():
    return render_template("register.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

# @app.route("/upload.html")
# def up():
#     username = session['username']
#     data = view_vit(username)
#     return render_template("upload.html" , data = data)

@app.route("/viewdata.html")
def up1():
    return render_template("viewdata.html")

# -------------------------------------------register-------------------------------------------------------
@app.route("/regact", methods = ['GET','POST'])
def registeract():
   if request.method == 'POST':    
      id="0"
      status = user_reg(id,request.form['username'],request.form['password'],request.form['email'],request.form['mobile'],request.form['address'])
      if status == 1:
       return render_template("login.html",m1="sucess")
      else:
       return render_template("register.html",m1="failed")


@app.route("/Vitaminact", methods = ['GET','POST'])
def Vitaminact1():
   if request.method == 'POST': 
      username=session['username']
      status = vit_act(username,float(request.form['vita']),float(request.form['vitb']),float(request.form['vitc']),float(request.form['vitd']),float(request.form['vite']),float(request.form['vitek']))
      #data = view_vit(username)
      print("dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd")
      print(status)
      if status[0]==1:
          vara="Deficient"
      else:
          vara="In Range"
      if status[1]==1:
          varb="Deficient"
      else:
          varb="In Range"
      if status[2]==1:
          varc="Deficient"
      else:
          varc="In Range"
      if status[3]==1:
          vard="Deficient"
      else:
          vard="In Range"
      if status[4]==1:
          vare="Deficient"
      else:
          vare="In Range"
      if status[5]==1:
          vark="Deficient"
      else:
          vark="In Range"
      reco=get_recomendations(status[6])
      recom=getdisease_recomendations(status[7])
      print(status[6])
      print(recom[0])
      if status[6]==1:
         full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fd.jpg') 
      if status[6]==2:
         full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fcvmd.jpg') 
      if status[6]==3:
         full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'cereals.jpg') 
      if status[6]==4:
         full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'dryfruits.jpg') 
      if status[6]==5:
         full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fruits.jpg') 
      if status[6]==6:
         full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'vegetables.jpg') 

       
      if status:
       return render_template("upload.html",m1="sucess",first=vara,second=varb,third=varc,fourth=vard,fifth=vare,sixth=vark,seventh=reco[0],eight=recom[0],user_image = full_filename)
      else:
       return render_template("userhome.html",m1="failed")
#--------------------------------------------Login-----------------------------------------------------
@app.route("/loginact", methods=['GET', 'POST'])
def useract():
    if request.method == 'POST':
        status = user_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']                             
            return render_template("userhome.html", m1="sucess")
        else:
            return render_template("login.html", m1="Login Failed")
#-------------------------------------------Upload Image----------------------------------

#--------------------------------------View Images-----------------------------------------
@app.route("/viewimage.html")
def viewimages():
    data = user_viewimages(session['username'])
	 
    print(data)
    return render_template("viewimage.html",user = data)



@app.route("/track")
def track():
    username = request.args.get('username')
    vita = request.args.get('vita')
    vitb = request.args.get('vitb')
    vitc = request.args.get('vitc')
    vitd = request.args.get('vit')
    vite = request.args.get('vite')

    data = vit_info(username,vita,vitb,vitc,vitd,vite)
    print("dddddddddddddddddddddddddddd")
    print(data)
    print("dddddddddddddddddddddddddddd")
    print(data)
    return render_template("viewimage.html",m1="sucess",data=data)

#---------------------------------------Track-----------------------------------------------

       
# ----------------------------------------------Update Item------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000,use_reloader=False)
