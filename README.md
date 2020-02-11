# GigFinder

A location aware Django web app for keeping track of Events
close to your location.  
Add venues via the admin page and add events to be hosted at the venues

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The following have to be installed on your computer

```
Python 3
PostgreSQL
PostGIS
```
Create a PostgreSQL Database with a PostGIS extension
### Installing

Clone The repo to your local machine by running the following command in your Terminal

```
git clone https://github.com/jayanwana/django-location-project.git
```

Enter the cloned repo directory

```
cd django-location-project/gigfinder
```

Install project dependencies
```
pip install requirements.txt
```
Edit the Database settings in settings.py file in gigfinder, use the username and password of the Database you created earlier.  
Make migrations to create the Database tables

```
python manage.py makemigrations
python manage.py migrate
```
Create super User for Admin pages
```
python manage.py createsuperuser
```
Start the web app with the following command
```
python manage.py runserver
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view the app.  
Events and Venues can be added via the Admin page at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
## Running the tests

Testing can be done using 
```
python manage.py test
```
### Test Breakdown

Tests have been written for both models included in this project, and also for the views.
```
VenueTest
EventTest
LookupViewTest
```


## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used
* [PostgreSQL](https://www.postgresql.org/) - Database


## Authors

* **Anwana John** - *Initial work* - [jayanwana](https://github.com/jayanwana)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
Special thanks to

* [**Matthew Daly**](https://matthewdaly.co.uk/)

