# django-app
# Django Job Vacancy Application

## 📌 Project Overview
This is a **Full-Stack Django Application** that allows users to browse job vacancies that are added through the Django Admin Panel. The project includes:
- **Home Page**: Introduction to the job portal.
- **Vacancy List Page**: View available job postings with filtering options.
- **Vacancy Detail Page**: Display detailed job descriptions.
- **Django Admin Panel**: Manage job postings.

## 🚀 Features
- 🏠 **Home Page** with a brief service description and navigation.
- 📋 **Vacancy List Page** with search and filter options.
- 📝 **Vacancy Detail Page** with complete job information.
- 🔧 **Django Admin Integration** for adding and managing jobs.
- 🎨 **Responsive UI** using HTML, CSS (Bootstrap/Tailwind optional).

## 🔧 Installation & Setup
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/madiar-ops/django-app.git
cd django-app
```

### 2️⃣ **Set Up a Virtual Environment**
```sh
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate    # On Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Apply Migrations**
```sh
python manage.py migrate
python manage.py createsuperuser  # Create admin user
```

### 5️⃣ **Run the Server**
```sh
python manage.py runserver
```
🚀 Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## 📂 Project Structure
```
django-app/
│── vacancies/          # Django app for job postings
│   │── templates/      # HTML templates
│   │── views.py        # Django views
│   │── models.py       # Database models
│── static/             # CSS
│── manage.py           # Django management script
│── db.sqlite3          # SQLite database
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
```

## 📜 Environment Variables
Create a `.env` file for secret keys and database settings:
```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## ✅ Deployment
### Deploy on **Heroku / Render / AWS**
1. Install **Gunicorn & WhiteNoise** for production:
   ```sh
   pip install gunicorn whitenoise
   ```
2. Set up `Procfile`:
   ```
   web: gunicorn elbicho.wsgi --log-file -
   ```
3. Push changes and deploy:
   ```sh
   git add .
   git commit -m "Deploy app"
   git push heroku main
   ```

## 🛠 Technologies Used
- **Django** (Backend)
- **HTML, CSS** (Frontend Styling)

## 🤝 Contributing
Feel free to submit issues and pull requests! 🚀

## 📜 License
This project is open-source under the **MIT License**.

👨‍💻 Happy Coding!
