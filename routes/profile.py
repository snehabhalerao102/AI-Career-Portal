from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, Student, Skill

profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/')
@login_required
def index():
    all_skills = Skill.query.order_by(Skill.category, Skill.name).all()
    return render_template('profile.html', all_skills=all_skills)


@profile_bp.route('/update', methods=['POST'])
@login_required
def update():
    student = Student.query.get(current_user.id)

    student.name      = request.form.get('name', student.name).strip()
    student.college   = request.form.get('college', '').strip()
    student.degree    = request.form.get('degree', '').strip()
    student.branch    = request.form.get('branch', '').strip()
    student.bio       = request.form.get('bio', '').strip()
    student.interests = request.form.get('interests', '').strip()

    year_str = request.form.get('year', '')
    if year_str.isdigit():
        student.year = int(year_str)

    cgpa_str = request.form.get('cgpa', '')
    try:
        student.cgpa = float(cgpa_str)
    except (ValueError, TypeError):
        pass

    # Skills: checkboxes
    selected_skill_ids = request.form.getlist('skills')
    # Clear existing
    for sk in list(student.skills):
        student.skills.remove(sk)

    for sid in selected_skill_ids:
        skill = Skill.query.get(int(sid))
        if skill:
            student.skills.append(skill)

    db.session.commit()
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('profile.index'))
