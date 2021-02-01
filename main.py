from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import models

@app.route("/")
def home():
 return render_template('home.html', title="HOME")

@app.route("/products-and-services/")
def products_and_services():
 return render_template('products-and-services.html', title="PRODUCTS AND SERVICES")

@app.route("/about-us/")
def about_us():
 return render_template('about-us.html', title="ABOUT US")

 @app.route("/signup/")
def signup():
 return render_template('signup.html', title="SIGN UP", information="Use the form displayed to register")

@app.route("/process-signup/", methods=['POST'])
def process_signup():
 firstname = request.form['firstname']
 lastname = request.form['lastname']
 dateofbirth = request.form['dateofbirth']
 residentialaddress = request.form['residentialaddress']
 nationality = request.form['nationality']
 nationalidentitynumber = request.form['nationalidentitynumber']

@app.route("/")
def home():
    return  '''My name is Ogheneyoma Adegor. This is my CA2 work.
    My GitHub URL is https://github.com/Ogheneyoma25/myISM209CA2'''



if __name__ == "__main__":
    app.run(port=5005)