from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models import Career

careers_bp = Blueprint('careers', __name__)


@careers_bp.route('/')
@login_required
def index():
    query   = request.args.get('q', '').strip()
    careers = Career.query.all()

    student_skill_names = [s.lower() for s in current_user.skills_list()]
    student_interests   = [i.lower() for i in current_user.interests_list()]

    results = []
    for career in careers:
        req = [s.lower() for s in career.required_skills_list()]
        match_count = sum(1 for s in student_skill_names if s in req)
        match_pct   = int((match_count / len(req)) * 100) if req else 0

        # Filter by search query
        if query and query.lower() not in career.title.lower() and query.lower() not in (career.description or '').lower():
            continue

        results.append({
            'career':    career,
            'match_pct': match_pct,
            'matched':   [s for s in student_skill_names if s in req],
            'missing':   [s for s in req if s not in student_skill_names],
        })

    results.sort(key=lambda x: x['match_pct'], reverse=True)

    return render_template('careers.html', results=results, query=query)
