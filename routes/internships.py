from flask import Blueprint, render_template, request
from flask_login import login_required
from models import Internship

internships_bp = Blueprint('internships', __name__)


@internships_bp.route('/')
@login_required
def index():
    query    = request.args.get('q', '').strip()
    category = request.args.get('category', '').strip()
    location = request.args.get('location', '').strip()
    remote   = request.args.get('remote', '').strip()

    internships = Internship.query

    if query:
        internships = internships.filter(
            (Internship.title.ilike(f'%{query}%')) |
            (Internship.company.ilike(f'%{query}%')) |
            (Internship.skills_required.ilike(f'%{query}%'))
        )

    if category:
        internships = internships.filter(Internship.category.ilike(f'%{category}%'))

    if location:
        internships = internships.filter(Internship.location.ilike(f'%{location}%'))

    if remote == 'yes':
        internships = internships.filter(Internship.is_remote == True)
    elif remote == 'no':
        internships = internships.filter(Internship.is_remote == False)

    internships = internships.order_by(Internship.posted_on.desc()).all()

    # Unique categories and locations for filter dropdowns
    all_internships  = Internship.query.all()
    categories       = sorted(set(i.category for i in all_internships if i.category))
    locations        = sorted(set(i.location  for i in all_internships if i.location))

    return render_template(
        'internships.html',
        internships=internships,
        categories=categories,
        locations=locations,
        query=query,
        selected_category=category,
        selected_location=location,
        selected_remote=remote,
    )
