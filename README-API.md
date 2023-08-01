# "BATTLEBOXES - API"

This is the supplimentary readme for the BattleBoxes API 

[Live Site] (https://pp5-django-api-b2580fe4fff7.herokuapp.com/)


---

## CONTENTS

* [Features](#features)
  * [Resources](#resources)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)


---




## Features

The API provides all of the data for the companion React App. It is a RESTful API built using Django and Django Rest Framework. It is hosted on Heroku and uses ElephantSQL for the database. The API is used to store and retrieve data for the React App. It is also used to authenticate users and provide them with a JWT token for use with the React App to keep users authenticated.


## Resources

The API has 5 main resources:

The following are the endpoints for the API:
- Profiles
- Builds
- Comments
- User Saved Builds

The following are the urls for each endpoint of the API:

- https://pp5-django-api-b2580fe4fff7.herokuapp.com/profiles/
- https://pp5-django-api-b2580fe4fff7.herokuapp.com/builds/
- https://pp5-django-api-b2580fe4fff7.herokuapp.com/comments/
- https://pp5-django-api-b2580fe4fff7.herokuapp.com/saved/


The Users resource is not directly accessible but is used for authenticating users and providing them with a session token for use with the React App to store their information and status of the current user (logged-in/not signed up etc). It also enalbed the user to reset their password if they forget it.

### Future Implementations

I had hoped to add numerous features to the site but due to time constraints I have had to limit the scope of the project. I have listed some of the features I would like to add in the future below:

- Ability for admins to choose posts to be features on the homepage
- Variation on the standard build content type features a step by step guide to building a PC with additional information and images.
- Add a rating system for content where users could vote on different aspects of the content (Parts chosen, looks, tidyness etc).


## Technologies Used

The project is comprised of a backend, written in Django and a frontend written in React. The frontend also makes use of React Router for routing and React Bootstrap to aid with the structure and layout of the site.
Both are hosted on Heroku and the backend database is hosted on ElephantSQL remotely and a CDN is used for hosting images (Cloudinary).

### Languages Used
- Python
- JavaScript
- React/JSX
- CSS

### Frameworks, Libraries & Programs Used

- Django
- JWT for Django
- React Router
- React Bootstrap
- Google Fonts
- Cloudinary

## Deployment & Local Development

The project can be run locally using python3 manage.py runserver in the terminal. It is recommended to enabled debug in the settings.py file (located in the pp5djangoapi folder)

### Deployment

Both projects are deployed to Heroku via the Github integrations. Once you have the project files, please commit them both to their own new repositories and connect them to Heroku via the Github integration. You will need to set the following config vars in Heroku for the Django App:

CLIENT_ORIGIN_DEV: If you are using gitpod or similar online IDE you will need to add the URL of your development preview here (e.g. https://8000-brown-otter-7j5j2j7b.ws-eu03.gitpod.io)

CLOUDINARY_API_KEY: This is the API key for your Cloudinary account, available in the dashboard.
CLOUDINARY_NAME: This is the name of your Cloudinary account, available in the dashboard.
CLOUDINARY_SECRET: This is the secret for your Cloudinary account, available in the dashboard.
CLOUDINARY_URL: This is the URL for your Cloudinary account, available in the dashboard.

DATABASE_URL: This is the URL for your ElephantSQL database, available in the dashboard.

DISABLE_COLLECTSTATIC: Set to 1 to disable collectstatic and use Cloudinary for hosting assets. Please disable in production only.

CLIENT_ORIGIN: "The URL for the deployed React App in heroku" (e.g. https://rnc-personal-react.herokuapp.com)
**Only avaialble after deployment** 

ALLOWED_HOST: "The URL for the deployed Django App in heroku" (e.g. https://rnc-personal-django.herokuapp.com) 
**Only avaialble after deployment** 

SECRET_KEY: THis is the secret key for your Django app. You can generate one here: https://miniwebtool.com/django-secret-key-generator/

#### How to Fork

You can fork either project by clicking the fork button in the top right of the repository page. This will create a copy of the project in your own github account. You can then clone the project to your local machine and make any changes you wish.

#### How to Clone

You can clone either project by clicking the green code button in the top right of the repository page. This will open a dropdown with the option to clone the project using HTTPS or SSH. Copy the link for the method you wish to use and then in your terminal navigate to the folder you wish to clone the project to and run the following command:

```bash
git clone <link>
``` 


  
