[![Build Status](https://travis-ci.org/Xorast/MJC-Website.svg?branch=master)](https://travis-ci.org/Xorast/MJC-Website)

# PROJECT MJC - YOUTH & COMMUNITY CENTER

MJC association's website (2,800 members).

Temporary domain: [https://www.mjc-mauguio-carnon.com/](https://www.mjc-mauguio-carnon.com/)  
Long term domain: [http://www.mjcmauguiocarnon.fr/](http://www.mjcmauguiocarnon.fr/) - Redirects towards the temporary domain for now.

## OVERVIEW - WHAT IS THIS APPLICATION FOR ?

The MJC is a public organisation that offers a large panels of activities (sports, arts, ...) and workshop (cooking, science, ...) and organises events for children and families.

This application is the organisation's website.

The aim of this website is to display the whole panels of activities, workshop and events that the MJC offers.
Any information is at 3 clicks away maximum from the user position.

The MVP - Minimum Viable Product - has been delivered for the Back-To-School day (where 90% of the registrations happens).
The first development stage is complete. More features might be added later (Profile page for members,...).

## WHO IS THIS APPLICATION FOR ?

This application used by members of the association or people that are not members yet and might be interested.

## HOW TO USE IT

The content and the UI is straightforward: you look for an information by accessing the sections throught the navbar and then click your way to more and more specific pages/information. 

## AUTHOR(S)

* Xorast

## ARCHITECTURE

The application is built with Django.
It uses Postgres for the databases.
It uses AWS S3 for the media and static files.

It is built with seven subapplications:

* Views - Handles the information sections
* Activities - Handles the "Activités" section of the website
* Workshops - Handles the "Stage" section of the website
* Events - Handles the "Evénement" section of the website
* News - Handles the "Actu" section of the website
* Accounts - Login / User space
* Checkout - Handles online payment for registrations to activities.

## DEPLOYMENT

To deploy this application, you'll need to:

* Fork and deployed directly on Heroku, as it is.
* Set a AWS S3 account and set Django the media/static folders.
* Set a Postgres database.
* Set a Stripe account and set tokens.

## TESTING

CI - Continuous Integration has been used :
Test are written in a file for each tested file (test_models.py to test the models.py file).
The application is tested with [Travis](https://travis-ci.org/) and the host service (Heroku) wait for CI to pass before deploy.

There are two types of files that are tested : those created for this application and those coming from libraries.
Tests have been developed only to test the files created for this application.

The first focus is testing that each page is responding (tests_views.py) and that forms processing is working.
More specific test to be developed (checking links in pages, checking content, ...).

## WIREFRAME

See pictures in the "wireframe" folder.
The big pictures has been drawn to give the structure and then the details has been design as I coded the project.

## BUILT WITH
### LANGUAGES
The application is written in:
* [Python 3](https://www.python.org/) (3.4.3) 
* JavaScript - Frontend  (jQuery - Research tool)
* HTML5 
* CSS3

### FRAMEWORKS & LIBRAIRIES
The following frameworks and librairies have been used:
* [Django 2.0](https://www.djangoproject.com/)
* [jQuery](https://jquery.com/)
* [Bootstrap](https://getbootstrap.com/) version 4.1.1


### SERVICES
* Online Database : [Postgres](https://www.heroku.com/postgres)
* AWS Storage : [S3](https://aws.amazon.com/s3/)
* Continuous Integration : [Travis](https://travis-ci.org/)
* Host : [Heroku](https://heroku.com)
* Scheduler : [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler)

## CREDITS
* Theme: [Bootswatch](https://bootswatch.com/) - Used theme [here](https://bootswatch.com/cerulean/)
* Pictures are provided by the association