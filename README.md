
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
├── app.py                
├── models.py              
├── init_db.py             
├── requirements.txt       
├── .gitignore
├── README.md
│
├── routes/
│   ├── __init__.py
│   ├── main.py            
│   ├── auth.py            
│   ├── dashboard.py       
│   ├── careers.py          
│   ├── internships.py      
│   └── profile.py          
│
├── templates/
│   ├── base.html          
│   ├── index.html         
│   ├── dashboard.html
│   ├── careers.html
│   ├── internships.html
│   ├── profile.html
│   └── auth/
│       ├── login.html
│       └── register.html
│
└── static/
    ├── css/style.css      
    └── js/main.js         
```

