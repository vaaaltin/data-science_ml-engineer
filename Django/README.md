#create users
python manage.py createsuperuser

#new app
django-admin starapp <appname>

#migrations
python manage.py makemigrations
python manage.py migrate

#run the server
python <main django file>.py runserver

#django shell
python manage.py shell