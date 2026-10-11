# 🎓 AI Based Smart Career Guidance and Internship Portal

> A Final Year Computer Science Engineering Project  
> Built with Python Flask · SQLite · Bootstrap 5 · Chart.js

---

## 📌 Project Overview

The **AI Based Smart Career Guidance and Internship Portal** is a web application that helps students discover suitable career paths and internship opportunities based on their skills and interests.  
The system uses a skill-matching algorithm to calculate compatibility scores between a student's profile and available career paths, presenting personalised recommendations on an attractive, responsive dashboard.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🏠 Landing Page | Modern hero section with feature highlights |
| 🔐 Authentication | Secure register / login / logout with password hashing |
| 📊 Dashboard | Colorful stat cards, career matches with progress bars, skill doughnut chart |
| 🧭 Career Guidance | AI-matched career paths with skill gap analysis |
| 💼 Internships | Search & filter internships by role, company, location, category, and remote |
| 👤 Student Profile | Manage skills (checkbox picker), education, CGPA, and interests |
| 📱 Responsive | Mobile-friendly layout using Bootstrap 5 |

---

## 🛠️ Technology Stack

- **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons, JavaScript
- **Backend:** Python 3.10+, Flask 3.x
- **Database:** SQLite (via SQLAlchemy ORM)
- **Charts:** Chart.js 4
- **Auth:** Flask-Login + Werkzeug password hashing

---

## 📁 Project Structure

```
AI-Career-Portal/
├── app.py                  # Flask application factory
├── models.py               # SQLAlchemy database models
├── init_db.py              # DB initialisation + seed script
├── requirements.txt        # Python dependencies
├── .gitignore
├── README.md
│
├── routes/
│   ├── __init__.py
│   ├── main.py             # Landing page
│   ├── auth.py             # Register / Login / Logout
│   ├── dashboard.py        # Student dashboard
│   ├── careers.py          # Career guidance
│   ├── internships.py      # Internship listings
│   └── profile.py          # Student profile
│
├── templates/
│   ├── base.html           # Shared layout (navbar + footer)
│   ├── index.html          # Landing page
│   ├── dashboard.html
│   ├── careers.html
│   ├── internships.html
│   ├── profile.html
│   └── auth/
│       ├── login.html
│       └── register.html
│
└── static/
    ├── css/style.css       # Custom styles + CSS variables
    └── js/main.js          # Chart.js init, animations, helpers
```

---

## ⚙️ Setup Instructions (Windows)

### Step 1 – Clone or download the project

```cmd
cd Desktop
:: if cloned from GitHub:
git clone https://github.com/YOUR_USERNAME/AI-Career-Portal.git
cd AI-Career-Portal
```

### Step 2 – Create and activate a virtual environment

```cmd
python -m venv venv
venv\Scripts\activate
```

> You should see `(venv)` at the start of your prompt.

### Step 3 – Install dependencies

```cmd
pip install -r requirements.txt
```

### Step 4 – Initialise the database and seed data

```cmd
python init_db.py
```

This creates `instance/career_portal.db` with all tables and sample data.

### Step 5 – Run the application

```cmd
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**

### 🔑 Demo Login

| Field | Value |
|---|---|
| Email | `demo@example.com` |
| Password | `demo123` |

---

## 📸 Pages

| Page | URL |
|---|---|
| Landing | `/` |
| Register | `/auth/register` |
| Login | `/auth/login` |
| Dashboard | `/dashboard/` |
| Career Guidance | `/careers/` |
| Internships | `/internships/` |
| Profile | `/profile/` |

---

## 🔒 Security

- Passwords are **bcrypt/PBKDF2 hashed** using `werkzeug.security`
- All dashboard/career/internship/profile routes are **login-protected**
- Flask `SECRET_KEY` is used for secure session management
- CSRF protection is provided by Flask sessions

---

## 🚀 Upload to GitHub

```cmd
:: 1. Initialise git (if not already)
git init
git add .
git commit -m "Initial commit: AI Career Portal"

:: 2. Create a new repo on github.com, then link it:
git remote add origin https://github.com/YOUR_USERNAME/AI-Career-Portal.git
git branch -M main
git push -u origin main
```

---

## 👩‍💻 Developer

| Name | Role |
|---|---|
| [Your Name] | Developer – Final Year CSE Project |

---

## 📄 License

This project is created for **educational purposes** as a final year college project.  
Free to use and modify for academic submissions.

---

*Made with ❤️ using Python Flask and Bootstrap 5*
