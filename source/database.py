import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from datetime import datetime
from model import *  
import numpy as np 
import numpy as np
import os 
import datetime

 
 
 

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="sai@2003", db="vitamin")
    c = _conn.cursor()

    return c, _conn

# -------------------------------register-----------------------------------------------------------------
def user_reg(id,username, password, email, mobile, address,):
    try:
        c, conn = db_connect()
        print(id,username, password, email,
               mobile, address)
        j = c.execute("insert into register (id,username,password,email,mobile,address) values ('"+id+"','"+username +
                      "','"+password+"','"+email+"','"+mobile+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def vit_act(username, vita, vitb, vitc, vitd,vite,vitk):
    
        #c, conn = db_connect()
    va=vit_A(vita)
    vb=vit_B(vitb)
    vc=vit_C(vitc)
    vd=vit_D(vitd)
    ve=vit_E(vite)
    vk=vit_K(vitk)
    rec,recdi=reco(va,vb,vc,vd,ve,vk)
    print(username, va, vb, vc, vd,ve,vk,rec,recdi)
    results =[va, vb, vc, vd,ve,vk,rec,recdi]      
        #j = c.execute("insert into upload (username, vita, vitb, vitc, vitd,vite,vitek) values ('"+username+"','"+str(va)+
        #              "','"+str(vb)+"','"+str(vc)+"','"+str(vd)+"','"+str(ve)+"','"+str(vk)+"')")
        #conn.commit()
        #conn.close()
        #print(j)
        #return j
    #except Exception as e:
        #print(e)
    return(results)
        #return(str(e))
# -------------------------------------Login --------------------------------------
def user_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from register where username='" +
                      username+"' and password='"+password+"'")
        data = c.fetchall()
        for a in data:
           session['uname'] = a[0]
       
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
#-------------------------------------Upload Image------------------------------------------
# def user_upload(id,name, image):
#     try:
#         c, conn = db_connect()
#         print(name,image)
#         username = session['username']
#         j = c.execute("insert into upload (id,name,image,username) values ('"+id+"','"+name+"','"+image +"','"+username +"')")
#         conn.commit()
#         conn.close()
#         print(j)
#         return j
#     except Exception as e:
#         print(e)
#         return(str(e))

#---------------------------------------View Images---------------------------------------
def user_viewimages(username):
    c, conn = db_connect()
    c.execute("select * from upload where  username='"+username +"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def vit_info(username,vita,vitb,vitc,vitd,vite):
    c, conn = db_connect()
    c.execute("select * from food ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def view_vit(username):
    c, conn = db_connect()
    c.execute("select * from upload where  username='"+username +"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

#------------------------------------Track----------------------------------------------------
def v_image(name):
    c, conn = db_connect()
    c.execute("Select * From images where name='"+name+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result
# ----------------------------------------------Update Items------------------------------------------
def get_recomendations(name):
    c, conn = db_connect()
    c.execute("Select recomend From recomend where predicted='"+str(name)+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result[0]

def getdisease_recomendations(name):
    c, conn = db_connect()
    c.execute("Select diseaserecomend From disease where predicted='"+str(name)+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result[0]

if __name__ == "__main__":
    print(db_connect())
