"""
init_db.py
Run once to create all tables and seed sample data.
Usage: python init_db.py
"""
import os
from datetime import datetime, timedelta, timezone
from app import create_app
from models import db, Skill, Career, Internship, Student

app = create_app()

SKILLS = [
    # Programming
    ('Python',           'Programming'),
    ('Java',             'Programming'),
    ('JavaScript',       'Programming'),
    ('C++',              'Programming'),
    ('C',                'Programming'),
    ('TypeScript',       'Programming'),
    ('Go',               'Programming'),
    ('Kotlin',           'Programming'),
    ('Swift',            'Programming'),
    ('R',                'Programming'),
    # Web
    ('HTML/CSS',         'Web Development'),
    ('React.js',         'Web Development'),
    ('Node.js',          'Web Development'),
    ('Flask',            'Web Development'),
    ('Django',           'Web Development'),
    ('Vue.js',           'Web Development'),
    ('Bootstrap',        'Web Development'),
    ('REST API',         'Web Development'),
    # Data & AI
    ('Machine Learning', 'Data & AI'),
    ('Deep Learning',    'Data & AI'),
    ('Data Analysis',    'Data & AI'),
    ('Pandas',           'Data & AI'),
    ('NumPy',            'Data & AI'),
    ('TensorFlow',       'Data & AI'),
    ('PyTorch',          'Data & AI'),
    ('NLP',              'Data & AI'),
    ('Computer Vision',  'Data & AI'),
    ('SQL',              'Data & AI'),
    # Cloud & DevOps
    ('AWS',              'Cloud & DevOps'),
    ('Docker',           'Cloud & DevOps'),
    ('Kubernetes',       'Cloud & DevOps'),
    ('Git',              'Cloud & DevOps'),
    ('Linux',            'Cloud & DevOps'),
    ('CI/CD',            'Cloud & DevOps'),
    # Design
    ('UI/UX Design',     'Design'),
    ('Figma',            'Design'),
    ('Adobe XD',         'Design'),
    # Soft Skills
    ('Communication',    'Soft Skills'),
    ('Problem Solving',  'Soft Skills'),
    ('Teamwork',         'Soft Skills'),
    ('Leadership',       'Soft Skills'),
]

CAREERS = [
    {
        'title':            'Full Stack Developer',
        'description':      'Design and build both frontend and backend web applications. Work with modern frameworks, APIs, and databases to deliver complete web solutions.',
        'required_skills':  'HTML/CSS, JavaScript, React.js, Node.js, REST API, SQL, Git',
        'avg_salary':       '₹6–18 LPA',
        'growth_rate':      'High (25%)',
        'icon':             'bi-code-slash',
        'color':            'grad-1',
    },
    {
        'title':            'Data Scientist',
        'description':      'Analyse large datasets to extract insights, build predictive models, and drive data-driven decisions using statistical and machine learning methods.',
        'required_skills':  'Python, Machine Learning, Data Analysis, Pandas, NumPy, SQL, TensorFlow',
        'avg_salary':       '₹8–24 LPA',
        'growth_rate':      'Very High (35%)',
        'icon':             'bi-bar-chart-fill',
        'color':            'grad-2',
    },
    {
        'title':            'Machine Learning Engineer',
        'description':      'Build, deploy, and maintain ML models in production. Bridge the gap between research and real-world AI applications.',
        'required_skills':  'Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, Docker, AWS',
        'avg_salary':       '₹10–30 LPA',
        'growth_rate':      'Very High (40%)',
        'icon':             'bi-cpu-fill',
        'color':            'grad-3',
    },
    {
        'title':            'Mobile App Developer',
        'description':      'Build native and cross-platform mobile applications for Android and iOS platforms.',
        'required_skills':  'Java, Kotlin, Swift, JavaScript, React.js, Git',
        'avg_salary':       '₹5–16 LPA',
        'growth_rate':      'High (22%)',
        'icon':             'bi-phone-fill',
        'color':            'grad-4',
    },
    {
        'title':            'Cloud & DevOps Engineer',
        'description':      'Design and manage cloud infrastructure, automate deployments and maintain CI/CD pipelines for scalable applications.',
        'required_skills':  'AWS, Docker, Kubernetes, Linux, CI/CD, Git, Python',
        'avg_salary':       '₹8–22 LPA',
        'growth_rate':      'High (30%)',
        'icon':             'bi-cloud-fill',
        'color':            'grad-1',
    },
    {
        'title':            'UI/UX Designer',
        'description':      'Create user-centred digital experiences through research, wireframing, prototyping and visual design.',
        'required_skills':  'UI/UX Design, Figma, Adobe XD, HTML/CSS, Communication',
        'avg_salary':       '₹4–14 LPA',
        'growth_rate':      'Medium (18%)',
        'icon':             'bi-palette-fill',
        'color':            'grad-5',
    },
    {
        'title':            'Cybersecurity Analyst',
        'description':      'Protect systems and networks from cyber threats. Conduct vulnerability assessments and incident response.',
        'required_skills':  'Linux, Python, Networking, Problem Solving, AWS',
        'avg_salary':       '₹6–20 LPA',
        'growth_rate':      'Very High (33%)',
        'icon':             'bi-shield-lock-fill',
        'color':            'grad-2',
    },
    {
        'title':            'Backend Developer',
        'description':      'Build robust server-side applications, RESTful APIs and database systems to power web and mobile apps.',
        'required_skills':  'Python, Java, Flask, Django, SQL, REST API, Docker, Git',
        'avg_salary':       '₹5–16 LPA',
        'growth_rate':      'High (24%)',
        'icon':             'bi-server',
        'color':            'grad-3',
    },
    {
        'title':            'Data Analyst',
        'description':      'Collect, process and visualise data to help organisations make better business decisions.',
        'required_skills':  'Python, SQL, Data Analysis, Pandas, R, Communication',
        'avg_salary':       '₹4–12 LPA',
        'growth_rate':      'High (28%)',
        'icon':             'bi-graph-up-arrow',
        'color':            'grad-4',
    },
    {
        'title':            'NLP / AI Research Engineer',
        'description':      'Research and develop natural language processing systems, chatbots, and AI-powered text analysis tools.',
        'required_skills':  'Python, NLP, Deep Learning, TensorFlow, PyTorch, Machine Learning',
        'avg_salary':       '₹12–35 LPA',
        'growth_rate':      'Very High (45%)',
        'icon':             'bi-chat-dots-fill',
        'color':            'grad-5',
    },
]

INTERNSHIPS = [
    # --- Tech companies ---
    {
        'title': 'Python Backend Intern',
        'company': 'TechNova Solutions',
        'location': 'Bengaluru',
        'duration': '3 Months',
        'stipend': '15,000',
        'skills_required': 'Python, Flask, SQL, REST API, Git',
        'description': 'Work on RESTful APIs using Flask and manage SQLite/PostgreSQL databases. Collaborate with the senior backend team.',
        'category': 'Software Development',
        'is_remote': False,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=1),
    },
    {
        'title': 'Frontend React Developer Intern',
        'company': 'Webcraft India',
        'location': 'Remote',
        'duration': '2 Months',
        'stipend': '12,000',
        'skills_required': 'React.js, JavaScript, HTML/CSS, Bootstrap, Git',
        'description': 'Build responsive UI components using React.js. Integrate APIs and deliver pixel-perfect designs.',
        'category': 'Web Development',
        'is_remote': True,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=2),
    },
    {
        'title': 'Data Science Intern',
        'company': 'Analytics Hub',
        'location': 'Hyderabad',
        'duration': '6 Months',
        'stipend': '20,000',
        'skills_required': 'Python, Machine Learning, Pandas, NumPy, SQL',
        'description': 'Analyse datasets, build ML models and present insights through dashboards. Real-world data science work.',
        'category': 'Data Science',
        'is_remote': False,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=3),
    },
    {
        'title': 'Machine Learning Intern',
        'company': 'DeepMind Labs (India)',
        'location': 'Remote',
        'duration': '3 Months',
        'stipend': '25,000',
        'skills_required': 'Python, TensorFlow, Deep Learning, NumPy, Machine Learning',
        'description': 'Implement and experiment with deep learning architectures. Work with large-scale datasets.',
        'category': 'Data Science',
        'is_remote': True,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=4),
    },
    {
        'title': 'Android App Development Intern',
        'company': 'AppForge Studio',
        'location': 'Mumbai',
        'duration': '2 Months',
        'stipend': '10,000',
        'skills_required': 'Java, Kotlin, Android SDK, Git',
        'description': 'Develop Android features, fix bugs, and write clean Kotlin/Java code under senior guidance.',
        'category': 'Mobile Development',
        'is_remote': False,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=5),
    },
    {
        'title': 'Cloud Engineering Intern',
        'company': 'CloudBase Technologies',
        'location': 'Pune',
        'duration': '3 Months',
        'stipend': '18,000',
        'skills_required': 'AWS, Docker, Linux, Python, CI/CD',
        'description': 'Assist in deploying cloud infrastructure on AWS, manage Docker containers and automate deployments.',
        'category': 'Cloud & DevOps',
        'is_remote': False,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=6),
    },
    {
        'title': 'UI/UX Design Intern',
        'company': 'PixelCraft Designs',
        'location': 'Remote',
        'duration': '2 Months',
        'stipend': '8,000',
        'skills_required': 'Figma, UI/UX Design, Adobe XD, HTML/CSS',
        'description': 'Design wireframes, prototypes and final UI screens for mobile and web applications using Figma.',
        'category': 'Design',
        'is_remote': True,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=7),
    },
    {
        'title': 'Full Stack Web Developer Intern',
        'company': 'Startify Co.',
        'location': 'Delhi',
        'duration': '4 Months',
        'stipend': '15,000',
        'skills_required': 'HTML/CSS, JavaScript, React.js, Node.js, SQL, REST API',
        'description': 'Develop full-stack features for our SaaS product. Work with React frontend and Node.js backend.',
        'category': 'Web Development',
        'is_remote': False,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=8),
    },
    {
        'title': 'NLP Research Intern',
        'company': 'LangTech AI',
        'location': 'Remote',
        'duration': '3 Months',
        'stipend': '22,000',
        'skills_required': 'Python, NLP, Deep Learning, TensorFlow, PyTorch',
        'description': 'Research and implement NLP models for text classification, summarisation and sentiment analysis.',
        'category': 'Data Science',
        'is_remote': True,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=9),
    },
    {
        'title': 'DevOps Intern',
        'company': 'InfraGeek Pvt Ltd',
        'location': 'Bengaluru',
        'duration': '3 Months',
        'stipend': '16,000',
        'skills_required': 'Docker, Kubernetes, Linux, Git, CI/CD, AWS',
        'description': 'Manage CI/CD pipelines, container orchestration with Kubernetes, and support production deployments.',
        'category': 'Cloud & DevOps',
        'is_remote': False,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=10),
    },
    {
        'title': 'Data Analyst Intern',
        'company': 'InsightX Analytics',
        'location': 'Chennai',
        'duration': '2 Months',
        'stipend': '12,000',
        'skills_required': 'Python, SQL, Data Analysis, Pandas, R',
        'description': 'Analyse sales and marketing data, create dashboards and generate weekly reports for business teams.',
        'category': 'Data Science',
        'is_remote': False,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=11),
    },
    {
        'title': 'Cybersecurity Intern',
        'company': 'SecureNet India',
        'location': 'Hyderabad',
        'duration': '3 Months',
        'stipend': '14,000',
        'skills_required': 'Linux, Python, Problem Solving, Networking',
        'description': 'Conduct security audits, vulnerability assessments, and assist in incident response activities.',
        'category': 'Cybersecurity',
        'is_remote': False,
        'posted_on': datetime.now(timezone.utc) - timedelta(days=12),
    },
]


def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()
        print('[OK] Tables created.')

        # ── Seed Skills ──
        skill_map = {}
        for name, category in SKILLS:
            sk = Skill(name=name, category=category)
            db.session.add(sk)
            skill_map[name] = sk
        db.session.commit()
        print(f'[OK] {len(SKILLS)} skills seeded.')

        # ── Seed Careers ──
        for c in CAREERS:
            career = Career(**c)
            db.session.add(career)
        db.session.commit()
        print(f'[OK] {len(CAREERS)} careers seeded.')

        # ── Seed Internships ──
        for i in INTERNSHIPS:
            internship = Internship(**i)
            db.session.add(internship)
        db.session.commit()
        print(f'[OK] {len(INTERNSHIPS)} internships seeded.')

        # ── Demo Student ──
        demo = Student(name='Demo Student', email='demo@example.com',
                       college='Demo University', degree='B.Tech',
                       branch='Computer Science', year=4, cgpa=8.7,
                       bio='Final year CSE student passionate about AI and Web Development.',
                       interests='Machine Learning, Web Development, Open Source')
        demo.set_password('demo123')
        # Add a few starter skills
        for sname in ['Python', 'JavaScript', 'Machine Learning', 'SQL', 'HTML/CSS', 'Git', 'Flask']:
            if sname in skill_map:
                demo.skills.append(skill_map[sname])
        db.session.add(demo)
        db.session.commit()
        print('[OK] Demo student created --> email: demo@example.com  |  password: demo123')

        print('\nDatabase initialised successfully!')
        print('Run:  python app.py   to start the server.')


if __name__ == '__main__':
    seed()
