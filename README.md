# Contents

[Tank Mileage Tracker](#tank-mileage-tracker)

tutorial link https://www.youtube.com/watch?v=_vCT42vDfgw&t=962s

link to the oryginal repository https://github.com/bobby-didcoding/did_django_google_api_tutorial

[UX](#ux)
+ [User Stories](#user-stories)
+ [Wireframes](#wireframes)

[Existing Features](#existing-features)
+ [Navbar](#navbar)
+ [Home Page](#home-page)
+ [Results Page](#results-page)
+ [Contact Page](#contact-page)

[Future Features](#future-features)

[Technologies Used](#technologies-used)
+ [Languages Used](#languages-used)
+ [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

[Code Validation](#code-validation)
+ [Automated Tests](#automated-tests)

[Project Bugs and Solutions](#project-bugs-and-solutions)

[Deployment](#deployment)
+ [Forking the GitHub Respository](#forking-the-github-repository)
+ [Making a Local Clone](#making-a-local-clone)


[Credits](#credits)
+ [Content](#content)
+ [Media](#media)

# Tank Mileage Tracker

[![showpiece](??? img location)](??? link to live website)

Click [here](???) to live site.  

## UX

### User Stories

+ As a user, I would like to be able to …



1.  the information to be clear and informative;
2.  the website be easy to navigate;


### Wireframes 

Wireframes created with Balsamiq. The project was developed from initial wireframes and some modifications were made during the development process to assure better usability. 

[Wireframes](???)

## Existing Features 

### Navbar and Footer

+ Navbar and footer has been copied from Bootstrap components and adjusted to the needs of the project
+ Navbar collapses into a hamburger button for easy navigation on mobile devices.
+ 

### Home page 

Traffic alert design - I've chosen a simple card design from bootstrap. I have also chosen to stack up the cards for larger screens to see two beside each other.
Since this is an app for driver I have taken the mobile first aproach. This app needs to be comfortable to use by someone that is using mobile phone only. This led to a decision to display only maximum of 4 messages per page. This way the mobile phone user will not have to scroll down too much, but there is an option to go to the next page.

### Contact Page



## Future Features 



## Technologies Used

### Languages Used

   + HTML5
   + CSS3
   + JavaScript

 ### Frameworks Libraries and Programs Used

+ Balsamiq:
    Balsamiq was used to create the wireframes during the design process.
+ Bootstrap 5:
    Bootstrap was used to add style to the website.
+ Git
    Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
+ GitHub:
    GitHub is used to store the project's code after being pushed from Git.


## Code Validation

### Automated tests

+ HTML

  Passing the HTML from all templates and base into the W3C Markup Validator no errors or warnings have been found [W3C validator](https://validator.w3.org/).


+ CSS

No errors were found when passing through the official [W3C validator](https://jigsaw.w3.org/css-validator/). 
        

+ JavaScript

Javascript files were tested with the jshint and no errors were been found. 

+ Python


## Project Bugs and Solutions:


### Unable to add "likes" to "cleared"
User is supposed to have possiblity to marked message as Road clear by clicking "cleared" icon on the traffic alert details view. The function returns error:

'ManyRelatedManager' object has no attribute 'cleared'

The cleared was created 

### requests==2.25.1

requests==2.25.1 was installed and returned error during instalation. Need to check if it affects app in any way. 
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
dj3-cloudinary-storage 0.0.6 requires requests>=2.26.0, but you have requests 2.25.1 which is incompatible.

### Link to Google Maps opens with no coordinates

when user sees the preview map, he can click bottom left corner "google" to be transferred to google app (on mobile) or google maps website (on desctop computer), unfortunately at the minute the google app/website opens with no coordinates.

read more:
https://developers.google.com/maps/documentation/urls/get-started

example url

https://www.google.com/maps/place/47%C2%B035'42.6%22N+122%C2%B019'53.9%22W/@47.5951518,-122.3316393,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0xca3d37fe916595c3!8m2!3d47.5951518!4d-122.3316393

this url opens directions

core:

https://www.google.com/maps/dir/?api=1

&origin=

latitute
%2C
longtitute

&destination=

latitute
%2C
longtitute

https://www.google.com/maps/dir/?api=1&origin=51.8630529%2C0.1755065&destination=52.5000791%2C-0.7110285





## Deployment

 The site was deployed to GitHub pages. 
 
 * The steps to deploy are as follows: 

  - In the GitHub repository, navigate to the Settings tab; 
  - From the source section drop-down menu, select the Master Branch;
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found [here](https://jogorska.github.io/garage-bootstrap/).

### Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JoGorska/garage-bootstrap)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JoGorska/garage-bootstrap)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/JoGorska/garage-bootstrap
```

7. Press Enter. Your local clone will be created.




## Credits 
* [Icons8](https://icons8.com/)
* [unsplash](https://unsplash.com/)
* [Fontawsome](https://fontawesome.com/)
* [Bootstrap 5]()
* [I Think Therefore I Blog]()
* [Django Google API]()

@igor_ci
I used Crispy Forms in my MS4 and they worked nicely (except for a few HTML code validator errors that didn’t affect display in any way).
But if you want to still use Django Bootstrap like in the videos, you need to
pip3 install django-forms-bootstrap
add "django_forms_bootstrap" to INSTALLED_APPS in settings.py
add the tag {% load bootstrap_tags %} to the top of every template you want to use Django Bootstrap forms in.
add the tag |as_bootstrap to every form you want to be styled with Django Bootstrap.

)

 
 icon for tank (simple)
https://www.iconfinder.com/search?q=tank&price=free
 Ilham Albab
 license free to share https://creativecommons.org/licenses/by/3.0/

 icon for thumbs up from fonawsome
 https://github.com/FortAwesome/Font-Awesome/tree/master/svgs/regular


 crispy forms
 commenting part 1 in Authorisation, Commenting and Likes 


google maps API + javascript map API

Visits app is making API calls to get distance and lenght of the journey and displays a map. This was created by following tutorial [Python Django application walkthrough tutorial for Google maps](https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s) Bobby did coding. For more details the repository is located [here](https://github.com/bobby-didcoding/did_django_google_maps_api).





### Content
