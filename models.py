from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aui_id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class CourseMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    material_type = db.Column(db.String(50), nullable=False)
    professor = db.Column(db.String(100), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'))
