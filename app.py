from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dateutil.parser import parse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning_tree.db'
db = SQLAlchemy(app)

class LearningItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    media_type = db.Column(db.String(100), nullable=False)
    date_started = db.Column(db.DateTime, nullable=False)
    date_finished = db.Column(db.DateTime, nullable=True)
    takeaways = db.Column(db.Text, nullable=True)
    inspiration_id = db.Column(db.Integer, db.ForeignKey('learning_item.id'), nullable=True)
    inspiration = db.relationship('LearningItem', remote_side=[id], backref='inspired_items')

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    items = LearningItem.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        media_type = request.form['media_type']
        date_started = parse(request.form['date_started'])
        date_finished = parse(request.form['date_finished']) if request.form['date_finished'] else None
        takeaways = request.form['takeaways']
        inspiration_name = request.form['inspiration']
        
        inspiration = None
        if inspiration_name:
            inspiration = LearningItem.query.filter_by(name=inspiration_name).first()
        
        new_item = LearningItem(
            name=name,
            media_type=media_type,
            date_started=date_started,
            date_finished=date_finished,
            takeaways=takeaways,
            inspiration=inspiration
        )
        
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True) 