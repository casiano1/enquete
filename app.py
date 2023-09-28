from flask import Flask, app, render_template, request, url_for, redirect, send_file, flash
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://helmerc:6h7#e61CfWEFl#@oege.ie.hva.nl/zhelmerc"
app.config['SQLAlchemy TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sdjhdjhsnkdnkdsnkshuhuhnn'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'ssl':{'fake_flag_to_enable_tls':True}}}
db = SQLAlchemy(app)

class Enquete(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        age = db.Column(db.String(100), nullable=False)
        vraag_1 = db.Column(db.Text, nullable=False)
        vraag_2 = db.Column(db.Text, nullable=False)
        vraag_3 = db.Column(db.Text, nullable=False)
        vraag_4 = db.Column(db.Text, nullable=False)
        vraag_5 = db.Column(db.Text, nullable=False)
        vraag_6 = db.Column(db.Text, nullable=False)
  
        

        def __repr__(self):
            return f'Response {self.name}'

    
@app.route("/submit", methods=["POST"])
def submit():
        age = request.form['age']
        vraag_1 = request.form['vraag_1']
        vraag_2 = request.form['vraag_2']
        vraag_3 = request.form['vraag_3']
        vraag_4 = request.form['vraag_4']
        vraag_5 = request.form['vraag_5']
        vraag_6 = request.form['vraag_6']
    
        

        enquete = Enquete(age=age, vraag_1=vraag_1, vraag_2=vraag_2, vraag_3=vraag_3, vraag_4=vraag_4, vraag_5=vraag_5, vraag_6=vraag_6)

        db.session.add(enquete)
        db.session.commit()

        flash('Bedankt voor uw medewerking')

        return redirect(url_for('enquete')) 

      
     
       





@app.route('/')
def home():
    return render_template ('home.html')


@app.route('/menu')
def menu():
    return render_template ('menu.html')


@app.route('/enquete')
def enquete():
    return render_template ('enquete.html')
    




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')