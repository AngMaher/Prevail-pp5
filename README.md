# Prevail Weightloss Group

# Contents

  - [User Experience](#user-experience)

    - [Wireframes](#wireframes)

    - [Colour Scheme](#colour-scheme)

  - [Agile](#agile)

    - [The Ideal User Persona](#the-ideal-userpersona)

    - [User Goals](#user-goals)

    - [Developer Goals](#developer-goals)

    - [Goals not completed](#goals-not-completed)

  - [Logic and Features](#logic-and-features)

    - [Logic](#logic)
      
      - [Data Models](#data-model)

    - [Features](#features)

      

  - [Tools and Technology](#tools-and-technology)

  - [Testing](#testing)

  - [Deployment](#deployment)

    - [ElephantSQL Database](#elephantsql-database)

    - [Cloudinary API](#cloudinary-api)

    - [Heroku Deployment](#heroku-deployment)

    - [Local Deployment](#local-deployment)

    - [Cloning](#cloning)

    - [Forking](#forking)

  - [Future Development](#future-development)

  - [Credits](#credits)

  - [Acknowledgements](#acknowledgements)

## Purpose and Goal

## Target Audience

### Demographics
Gender: Female
Age range: 30-60

### Persona of typical User.
- I believe the persona of the user of this site is mainly female with an age range of approximately 30 to 60 years of age. 
- They are looking to get healthier and want to have support, inspiration and guidance while doing so.
- They want a physical class or online class but an easy way of paying for it.
- They want to be able to purchase the merchandise from the class online.


## Business and Customer Goals

## UI/UX Desgin

### Wireframes

#### Home Page Wireframe

<details>
<summary>Click to View Home Page wireframes</summary>

![blog page](/docs/readme/HomeWF.png)
</details>

#### Home Page Wireframe

<details>
<summary>Click to View the Footer wireframes</summary>

![blog page](/docs/readme/footerWF.png)
</details>

#### Home Page Wireframe

<details>
<summary>Click to View Shop wireframes</summary>

![blog page](/docs/readme/ProductWF.png)
</details>

#### Home Page Wireframe

<details>
<summary>Click to View Product Detail wireframes</summary>

![blog page](/docs/readme/Detail-ProductWF.png)
</details>

#### Home Page Wireframe

<details>
<summary>Click to View Basket wireframes</summary>

![blog page](/docs/readme/BasketWF.png)
</details>



### Color Scheme

I decided to keep the website bright with a main colour of blue throughout the site. 

  - #d5a6bd - Pink Lavender as the contrasting headings and boxes to break up the page.
  - #343434 - Jet, this colour is used a on the majority of the text throughout the site, and the footer, Navbar, Buttons.
  - #FFF - white, this is used as the main background colour of the site to keep things clean


![colours used](/docs/readme/Project-5-Colours.png)

I used [coolors.co](https://coolors.co/343434-5799e1-fdf8f4-e64141) to pick my colours.

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    --main-pink: #d5a6bd;
    --dark-gray: #333333;
    --background-colour: #fff;
    --messages: rgb(53,152, 139, 0.6);
}
```
[Back to top &uarr;](#contents)

### Typography 

## Database Design

### Entity Relationship Diagram (ERD)


## User Stories

To help with the development of this project, I created user stories to map out tasks I needed to achieve in order to build the website to a good standard. I further split these user stories into epics in order to take an agile approach to its development.

View a full list of user stories [here](https://github.com/AngMaher/Prevail-pp5/issues).

### EPIC 1: General Site Functionality

    - As a Site User - for the first time I can see what the site's purpose is so that I can decide whether or not to continue on the site. `(MUST HAVE)`
    - As a Site User I can easily see the options to navigate around the site so that I can find what I want with ease. `(MUST HAVE)`

### EPIC 2: Shop and Products

    - As a Site User I can view a list of all products so that I can browse through all products. `(MUST HAVE)`
    - As a Site User I can see a detailed view of the product so that I can get more details before I add to cart. `(MUST HAVE)`
    - As a Site User I can change the quantity of the product so that I can buy multiple at the same time.`(MUST HAVE)`
    - As a Site User I can easily filter products into different categories so that I can just look at what I'm interested in. `(SHOULD HAVE)`


### EPIC 3: Checkout Bag

    -As a Site User I can delete on item from the checkout bag so that I have an option to change my mind.  `(MUST HAVE)`
    -As a Site User I can see a breakdown of price so that I can see how much shipping will be before I buy. `(SHOULD HAVE)`
    - As a Sit User I can see a summary of what I'm buying when I fill in my details so that I can check everything is correct before I commit. `(SHOULD HAVE)`
    - As a site user I want to be able to receive an order confirmation email after I purchase from the shop so that I can have a record of what I've purchased in my email inbox  `(MUST HAVE)`


### EPIC 4: Subscriptions and Payment

    - As a Site User I can become a Prevail member with ease so that I can quickly sign up without going through the whole website. `(MUST HAVE)`


### EPIC 5: Site User Account

    - As a site user I want to be able to create an account on the site so that I can save my billing and shipping details and see a history of my purchases on my account `(MUST HAVE)`
    - As a registered user I want to be able to edit the details saved to my account so that I can keep my details up to date `(COULD HAVE)`


### EPIC 6: Site Admin and Prevail Management

    - As a site admin I want to be able to create new products from the front end so that I can easily add new products to the site `(MUST HAVE)`
    - As a site admin - Prevail management I want to be able to edit existing products so that I can ensure that all product listings are up to date and accurate `(MUST HAVE)`
    - As a site admin - Prevail Management I want to be able to delete products from the site so that I can remove any products that are no longer being supplied by the site `(MUST HAVE)`
 

### EPIC 7: Class Updates

    - As a prevail member I want to be able to view class on the website so that I can feel part of the community and see how other classes are doing. `(SHOULD HAVE)`
    - As a Site admin - Prevail Manager I can display a post on the logged-in page of members so that I can display how each class is doing each week. `(SHOULD HAVE)`
    - As a site admin -prevail manager I want to be able to edit existing updates so that I can fix an error without having to delete and re-do `(COULD HAVE)`
    - As a site admin - prevail manager I want to be able to delete existing updates so that I can delete them when they get too old. `(SHOULD HAVE)`

### EPIC 8: Success Stories

    - As a Site admin/prevail manager I can display success stories of members so that I can show Site Users how successful our group can be and encourage them to join. `(COULD HAVE)`


### EPIC 9: SEO and Marketing

    - As a site user I want to be able to sign up for the site's mailing list so that I can receive offers and news in my inbox `(SHOULD HAVE)`
    - As a site admin I want to be able to set appropriate keywords on site pages so that I can increase the chances potential customers will find the site when searching to purchase records on Google `(MUST HAVE)`

## Tools & Technologies & Libraries Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.



***
## Deployment and Procedures

The live deployed application can be found deployed on [Heroku]().

***
### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: tribe).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

[Back to top &uarr;](#content)

***
### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store docs assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable docs for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

[Back to top &uarr;](#content)

***
### Heroku Deployment

[Setting up basic Django Project and Deploying to Heroku CI Doc](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

1. Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
1. Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
1. Further down, to support dependencies, select *Add Buildpack*.
1. The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)
1. From the new app *Settings*, click *Reveal Config Vars*, and set your environment variables.

    
    - CLOUNDINARY_URL: (Enter Cloudinary API URL)
    - DATABASE_URL: (Enter the database URL from ElephantSQL)
    - PORT: 8000
    - DISABLE_COLLECTSTATIC: 1 (must be removed before final deployment)
    - SECRET_KEY: (Enter your secret key)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's *requirements* (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The *Procfile* can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace *app_name* with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select *Automatic Deployment* from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

[Back to top &uarr;](#content)

***
### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "insert your own Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

[Back to top &uarr;](#contents)


***
#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/AngMaher/PP4-Where-Next) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/AngMaher/Prevail-pp5`
7. Press Enter to create your local clone.


[Back to top &uarr;](#content)

***
#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
To make a copy or ‘fork’ the repository - 

1. Log into GitHub and locate the repository  
2. On the right-hand side of the page select the ‘fork’ option to create and copy the original

Alternatively, if using Gitpod, you can click below to create your workspace using this repository

[Back to top &uarr;](#content)

### AWS S3 Bucket Creation

### Stripe Configuration

## References and Credits