from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

db = SQLAlchemy()


# Association table: student <-> skills
student_skills = db.Table(
    'student_skills',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('skill_id',   db.Integer, db.ForeignKey('skills.id'),   primary_key=True),
)


class Student(UserMixin, db.Model):
    __tablename__ = 'students'

    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(120), nullable=False)
    email        = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    college      = db.Column(db.String(200))
    degree       = db.Column(db.String(100))
    branch       = db.Column(db.String(100))
    year         = db.Column(db.Integer)
    cgpa         = db.Column(db.Float)
    bio          = db.Column(db.Text)
    interests    = db.Column(db.String(500))   # comma-separated
    created_at   = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    skills       = db.relationship('Skill', secondary=student_skills, backref='students', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def skills_list(self):
        return [s.name for s in self.skills]

    def interests_list(self):
        if self.interests:
            return [i.strip() for i in self.interests.split(',') if i.strip()]
        return []

    def __repr__(self):
        return f'<Student {self.email}>'


class Skill(db.Model):
    __tablename__ = 'skills'

    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(100))   # e.g. Programming, Design, Soft Skill

    def __repr__(self):
        return f'<Skill {self.name}>'


class Career(db.Model):
    __tablename__ = 'careers'

    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.String(200), nullable=False)
    description  = db.Column(db.Text)
    required_skills = db.Column(db.String(500))   # comma-separated skill names
    avg_salary   = db.Column(db.String(100))
    growth_rate  = db.Column(db.String(50))
    icon         = db.Column(db.String(100))       # Bootstrap icon class
    color        = db.Column(db.String(50))        # CSS gradient label

    def required_skills_list(self):
        if self.required_skills:
            return [s.strip() for s in self.required_skills.split(',') if s.strip()]
        return []


class Internship(db.Model):
    __tablename__ = 'internships'

    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.String(200), nullable=False)
    company      = db.Column(db.String(200), nullable=False)
    location     = db.Column(db.String(200))
    duration     = db.Column(db.String(100))
    stipend      = db.Column(db.String(100))
    skills_required = db.Column(db.String(500))
    description  = db.Column(db.Text)
    category     = db.Column(db.String(100))
    posted_on    = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_remote    = db.Column(db.Boolean, default=False)

    def skills_list(self):
        if self.skills_required:
            return [s.strip() for s in self.skills_required.split(',') if s.strip()]
        return []
