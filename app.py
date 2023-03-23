from flask import Flask,request,render_template,redirect
from flask_mysqldb import MySQL
import mysql.connector


app=Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'foodbank'

cursor = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="foodbank"
  )
 
mysql = MySQL(app)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
            return render_template("index.html")

    if request.method=="POST":
            
            name=request.form["name"];
            address=request.form["address"];
            phone=request.form["phone"];
            classes=request.form["classes"];
            name1=request.form["name1"];
            quantity1=request.form["quantity1"];
            cursor=mysql.connection.cursor()
            cursor.execute('''Insert INTO donor(Name,Address, Phone_Number,Food_Type,Item_Name,Quantity) Values(%s,%s,%s,%s,%s,%s)''',(name,address,phone,classes,name1,quantity1))
            mysql.connection.commit();

        


    
            return redirect("/")


@app.route("/Donor",methods=["GET","POST"])
def l():
        
        if request.method=="GET":
            return render_template("index.html")

        if request.method=="POST":
            
            name=request.form["name"];
            address=request.form["address"];
            phone=request.form["phone"];
            classes=request.form["classes"];
            name1=request.form["name1"];
            quantity1=request.form["quantity1"];

            rname=request.form["rname"];
            mno=request.form["mno"];
            don=request.form["dno"];
            add=request.form["add"];
            needs=request.form["needs"];
            


            
            cursor=mysql.connection.cursor()
            cursor.execute('''Insert INTO donor(Name,Address, Phone_Number,Food_Type,Item_Name,Quantity) Values(%s,%s,%s,%s,%s,%s)''',(name,address,phone,classes,name1,quantity1))
            cursor.execute('''Insert INTO Request(Name,Address, No,needs,item_Type) Values(%s,%s,%s,%s,%s)''',(rname,mno,add,needs,don))

            mysql.connection.commit();

        


    
        return render_template("index.html")



@app.route("/Requestee")
def Donor2():
    render_template("")


@app.route("/Registration")
def Donor():
    render_template("")


    
if __name__ == '__main__':
  app.run(debug=True)