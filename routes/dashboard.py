from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import Internship, Career

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
@login_required
def index():
    # Recent internships (latest 3)
    recent_internships = Internship.query.order_by(Internship.posted_on.desc()).limit(3).all()

    # Career matches based on student skills
    student_skill_names = [s.lower() for s in current_user.skills_list()]
    careers = Career.query.all()

    matched_careers = []
    for career in careers:
        req = [s.lower() for s in career.required_skills_list()]
        match_count = sum(1 for s in student_skill_names if s in req)
        if req:
            match_pct = int((match_count / len(req)) * 100)
        else:
            match_pct = 0
        matched_careers.append((career, match_pct))

    # Sort by match percentage descending, take top 4
    matched_careers.sort(key=lambda x: x[1], reverse=True)
    top_careers = matched_careers[:4]

    # Skill distribution for chart
    skill_categories = {}
    for skill in current_user.skills:
        cat = skill.category or 'Other'
        skill_categories[cat] = skill_categories.get(cat, 0) + 1

    return render_template(
        'dashboard.html',
        recent_internships=recent_internships,
        top_careers=top_careers,
        skill_categories=skill_categories,
        total_internships=Internship.query.count(),
        total_careers=Career.query.count(),
        total_skills=current_user.skills.count(),
    )
