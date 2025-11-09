# Characafe

![Characafe on amiresponsive.dev](characafe-amiresponsive.png)

[Vist the live website.](https://characafe-1eb4a9dff267.herokuapp.com/)

Characafe is a cafe with a menu based on five cute characters, as well as a variety of goods dedicated to these characters. 

## Features 

### Home Page 


The front page displays a carousel of the five characters, allowing the visitor to get an understanding of them, and some of the dishes on the menu.

![front page screenshot]()

There are three sections to the front page - 

![front page carousel](media/characafe-carousel.png)

A carousel showing the characters that are the feature of the website. 

![front page menu](media/menu-characafe.png)

The menu with menu items. 

![front page location section]()

### Navbar

The navigation bar changes depending on whether a user is logged in or not. 

When logged out, the visitor/user shall see the home page, the option to login or sign up to use the website. 

![navbar when logged out screenshot](media/characafe-navbar.png)

When logged in, the user will see their username and avatar with a drop down for their profile, wishlist and logout page. 

![navbar when logged in screenshot](media/characafe-navbar-logged.png)

Both versions will show the cart and the number of the items that are currently in the user's cart at any given time. 



### Characters Page 

![character display screenshot]()

This is the page displaying the five characters so users can learn more about them, their likes, dislikes, birthday etc. There is also a button to see goods of these characters so users can buy them. 

### Menu Page 

![menu page screenshot](static/images/submitimagepage.png)

This page allows a user to look at what is currently on the menu. 

### Products page 

![products page screenshot](static/images/contactuspage.png)

This page allows a visitor or a user to view all the products, as well as sort products by character. Prices are listed and users, if in a rush, can buy a product on this page by pressing the button or click on the product name or image to find out more information.

### Login Page 

![login page screenshot](static/images/signinpage.png)

This is the page to allow a user to log in by entering their email and password.

### Signout Page 
![signout page screenshot](static/images/signoutsection.png)
This is a page to confirm with the user if they want to log out or not. 

### Signup Page 

![sign up page screenshot](static/images/signuppage.png)

This is for visitors to register for an account with the website. 

## UX 

### Colour Scheme 

![Characafe Palette](static/images/)

The colour scheme for Characafe was derived from a poster of a Sanrio character, as I wanted the colour scheme to be cute but still good for accessibility purposes, with a variety of colours. 

### Typography 

The Friendcurate logo is in the [Rubik 80s Fade](https://fonts.google.com/specimen/Rubik+80s+Fade) font. The main header font for the main headers is [Cabin Sketch](https://fonts.google.com/specimen/Cabin+Sketch) - to reflect the art element of the website. Some of the headings use the [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) to give a cool, retro feel to the website and accompanies the Rubik 80s Fade font. 

### Wireframes 

_Home Page_ 

* [main page desktop](https://wireframe.cc/0iwC3p)
* [main page tablet](https://wireframe.cc/Bf2JI6)
* [main page mobile](https://wireframe.cc/SiHKW5 )

_Products Page_

* [products page desktop](https://wireframe.cc/EI3Cje)
* [products page tablet](https://wireframe.cc/jMg7bh)
* [products page mobile](https://wireframe.cc/VyUqu9)

_Characters Page_

* [characters page desktop](https://wireframe.cc/7UdzCk)
* [characters page tablet](https://wireframe.cc/IuJedb)
* [characters page mobile]( https://wireframe.cc/41b8Rr)

_Menu Page_

* [menu page desktop](https://wireframe.cc/LqSGhy)
* [menu page tablet](https://wireframe.cc/rBWUCs)
* [menu page mobile](https://wireframe.cc/2VecRq)

_Profile Page_ 

* [profile desktop]()
* [profile tablet]() 
* [profile mobile]()

### Data Schema 

![lucidchart screenshot](static/images/friendcurate%20chart.png)
[Lucidchart](https://www.lucidchart.com/pages) was for the data schema for Characafe which uses a relational model, as illustrated in the Entity Relationship Diagram (ERD) provided. Above is an Entity Relationship Diagram that shows the key models and their fields.



### User Stories

1. As a visitor to the site, I can create an account so I can comment on images, edit my comments and add images myself.

2. As a user, I can add images that other users can comment on and add to their favourites. 

3. As an admin, I can check images and captions, comments to make sure they are okay and up to date and approved. 

4. As a user, I can add images to my favourites collection and to be able to view my collection. 

5. As a user, I can sign in to the website so that I can access my account and enjoy customized features and contents.

6. As a user, I can sign out of the website when I finished using it for now.

7. As a site owner, I want to encourage visitors to become users of the website. 

### Agile Development 

This project was managed and developed by using the Project Board and Issues section on GitHub - visit the project board [here.](https://github.com/users/acmuckian/projects/4)

## Deployment 

The live deployed application can be found on [Heroku](https://friendcurate-e7f12440f18f.herokuapp.com/).

### 

### Forking 

To fork this repository, follow the below steps:

1. Login to Github.
2. Go to the repository for this project.
3. Click on the grey "fork" button on the repository main page. 
4. This should give you a forked copy in your GitHub account.


### Making a Clone 


The repository can also be cloned for local deployment. To clone the repository:

1. Login to Github.
2. Go to the repository for this project.
3. Click on the green "Code" button on the repository main page and copy the link shown.
4. Open the terminal in the code editor. 
5. Clone the repository.

### Local Deployment 

1. Clone responsitory as detailed above. 

### Heroku Deployment 

1. Log in or create a Heroku account. 
2. On the dashboard, click on the "new" button and then "create new app".
3. Give the app a name which is unique, and select the location for Common Runtime. I selected **Europe** where I am based. 
4. Click create app. 
5. After this, in the Config Vars, click reveal and insert the following variables:

| Key                   | Value                        |
|-----------------------|------------------------------|
| DATABASE_URL          | user's own value             |
| DISABLE_COLLECTSTATIC | _1 (mainly used only during initial setup)_ |
| CLOUDINARY_URL        | user's own value             |
| SECRET_KEY            | user's own value             |

6. Ensure procfile is in the repository as required by Heroku - install with 
`echo web: gunicorn app_name.wsgi > Procfile`

(instead of app_name, put in your own app's name)
7. install dependencies using 
`pip install -r requirements.txt`
8. Select Automatic Deployment from the Heroku app to connect to your repository - alternatively, you can deploy manually via Heroku CLI or GitHub integration. 
9. Manual deployment can be done as follows:
- log in to Heroku from the terminal 
` heroku login -i `
- set the heroku remote (replace app_name with name of your heroku app) 
` heroku git:remote -a app_name `
- add, commit and push changes to github 
``` git add . git commit -m 'commit message'  git push heroku main ```
- deploy to heroku by pushing the code: 
`git push heroku main`


## Testing 

Please refer to the [testing page](TESTING.md) for information about testing and bugs. 

## Credits 

- [Very Academy](https://www.youtube.com/@veryacademy)'s youtube tutorial _Learn Django 3_ has been useful for features like the user profile, and creating a favourites feature.
- [Django](https://www.djangoproject.com/)'s official documentation was also very helpful. 
- [Stack Overflow](https://stackoverflow.com/questions) and Copilot GPT-4.1 in the Visual Studio Code Desktop were both useful for debugging errors. 
- [Code Institute](https://codeinstitute.net/)'s tutorial on setting up a blog using Django was extremely helpful and the basis of my project. 
- For the basis of this website, sites like [Art Fight](https://artfight.net/) and [DeviantArt](https://www.deviantart.com/) were influential. 
- [Unsplash](https://unsplash.com/) was used to source some of the images. 



