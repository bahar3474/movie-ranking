# movie-ranking

Django application for ranking movies and show top 5 according to the members' rating.

#### Getting Started
- Create a virtualenv with python version 3 and activate it.
- Install requirements: 
```bash
pip install -r requirements.txt
```
- Create an admin user:
```bash
python manage.py createsuperuser
```
- Database:
```bash
cd ranking
python manage.py migrate
```
- Run:
```bash
python manage.py runserver
```

