# **Health-care Project Django Application**

A simple Django-based web application that allows users to upload personal information, including an ID, name, age, and file, storing the data locally.

## **Features**

- Upload personal information through a web form.
- Save files locally using Django's `FileField`.
- Validates user input to ensure proper data storage.
- View uploaded files directly from the local directory.

---

## **Requirements**

To run this project, you need the following installed:

- Python (>= 3.8)
- Django (>= 4.0)
- SQLite (default database)
- Any web browser (for testing the UI)

---

## **Setup Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/person-upload-django.git
   cd person-upload-django
   ```

# **File Structure**

```
person-upload-django/
│
├── person_upload/          # Main Django app
│   ├── migrations/         # Database migration files
│   ├── templates/          # HTML templates
│   ├── views.py            # Application views
│   ├── models.py           # Data models
│   ├── forms.py            # Django forms
│   └── urls.py             # App-specific URL routes
│
├── media/                  # Directory for uploaded files
│
├── manage.py               # Django project management script
├── db.sqlite3              # SQLite database
├── requirements.txt        # Project dependencies
└── README.md               # a readme file
```

## How to Use

#### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Dependencies

```bash

pip install -r requirements.txt
```

#### Run Database Migrations

```bash
python manage.py migrate
```

#### Start the Development Server

```bash

python manage.py runserver
```

#### To create Migration

```bash
py manage.py makemigrations
```

#### To appy Migration

```bash
py manage.py migrate
```

#### To run the server

```bash
py manage.py run runserver
```

**Navigate to the upload page at http://127.0.0.1:8000/upload/.**

#### Fill out the form:

1. Enter your name.
2. Provide your age.
3. Select a file to upload.
4. Click the Upload button to save your data.
5. View uploaded files in the media/uploads/ directory.
