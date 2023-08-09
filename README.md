# Prevail Weight loss Group

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

![blog page](/docs/readme/home.png)
</details>

#### Footer Wireframe

<details>
<summary>Click to View the Footer wireframes</summary>

![blog page](/docs/readme/footer.png)
</details>

#### Products Shop Page Wireframe

<details>
<summary>Click to View Shop wireframes</summary>

![blog page](/docs/readme/products.png)
</details>

#### Product Detail Page Wireframe

<details>
<summary>Click to View Product Detail wireframes</summary>

![blog page](/docs/readme/product_detail.png)
</details>

#### Basket Page Wireframe

<details>
<summary>Click to View Basket wireframes</summary>

![blog page](/docs/readme/basket.png)
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

### Models

- **Allauth User Model**
    - The User model was built using [Django's Allauth library](https://django-allauth.readthedocs.io/en/latest/overview.html)
    - When a user is created, they're automatically assigned a profile through the Profile model.

- **UserProfile**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | user | OneToOne | FK to **User** model |
    | | default_phone_number | CharField | |
    | | default_street_address1 | CharField | |
    | | default_street_address2 | CharField | |
    | | default_town_or_city | CharField | |
    | | default_county | CharField | |
    | | default_postcode | CharField | |
    | | default_country | CountryField | |

- **Category**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | | name | CharField | |
    | | friendly_name | CharField | |


- **Order**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | | order_number | CharField | |
    | **FK** | user_profile | ForeignKey | FK to **UserProfile** model |
    | | full_name | CharField | |
    | | email | EmailField | |
    | | phone_number | CharField | |
    | | country | CountryField | |
    | | postcode | CharField | |
    | | town_or_city | CharField | |
    | | street_address1 | CharField | |
    | | street_address2 | CharField | |
    | | county | CharField | |
    | | discount | DecimalField | |
    | | delivery_cost | DecimalField | |
    | | order_total | DecimalField | |
    | | grand_total | DecimalField | |
    | | original_basket | TextField | |
    | | stripe_pid | CharField | |

- **OrderLineItem**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | order | ForeignKey | FK to **Order** model |
    | **FK** | product | ForeignKey | FK to **Product** model |
    | | quantity | IntegerField | |
    | | lineitem_total | DecimalField | |


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
### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

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

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:
- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/AngMaher/prevail-pp5) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/AngMaher/prevail-pp5.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/AngMaher/prevail-pp5)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/AngMaher/prevail-pp5)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

To my knowledge there are no differences between the local and deployed versions of this site.

[Back to top &uarr;](#content)

### AWS S3 Bucket Creation

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `group-prevail-weight-lodd` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Suggested Name: `policy-prevail-weight-loss` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for prevail-weight-loss static files."
	- Click **Create Policy**.
- From **User Groups**, click your "group-prevail-weight-loss.
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-prevail-weight-loss") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `user-prevail-weight-loss` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-prevail-weight-loss`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://retro-reboot.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/users/AngMaher/projects/12) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

![screenshot](documentation/gh-projects-board.png)

### GitHub Issues

[GitHub Issues](https://github.com/AngMaher/Prevail-pp5/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped to keep on top of my [milestones](https://github.com/AngMaher/Prevail-pp5/milestones) for the project.

- [Open Issues]()

    ![screenshot]()

- [Closed Issues]()

    ![screenshot]()

    ![screenshot]()

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Ecommerce Business Model

This site sells goods to individual customers, and therefore follows a `Business to Customer` model.
It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything
such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users.
For example, what items are on special offer, new items in stock,
updates to business hours, notifications of events, and much more!

## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users
when searching online to find my page easily from a search engine.
This included a series of the following keyword types

- Short-tail (head terms) keywords
- Long-tail keywords

I also used [Word Tracker](https://www.wordtracker.com)
to check the frequency of some of my site's primary keywords.

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file.
This was generated using my deployed site URL: Sitemap: https://prevail-weight-loss-fa257f0d4d7b.herokuapp.com

After it finished crawling the entire site, it created a
[sitemap.xml](sitemap.xml) which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the default settings:

```
User-agent: *
Disallow:
Sitemap: https://prevail-weight-loss-fa257f0d4d7b.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales.
Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account using facebook, here is a link to the page.
[facebook page](https://www.facebook.com/profile.php?id=100095513502528)

Here are some screenshots of the page.
![screenshot]()
![screenshot]()
![screenshot]()

### Newsletter Marketing

I have incorporate a newsletter sign-up form on my application, to allow users to supply their
email address if they are interested in learning more about what the business has to offer.



I set the email address to be unique to avoid users signing up multiple times with the same email address. If a user tries to sign up twice with the same address they will be shown a message letting them know they've already signed up.

Once a user signs up, I used the `send_mail()` functionality in the `webhook_handler.py` file to trigger a welcome email for the user to acknowledge that they've successfully signed up for the newsletter.

In this welcome newsletter, I've included a special discount code to entice sign ups to purchase on the site.

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://prevail-weight-loss-fa257f0d4d7b.herokuapp.com/).

## References and Credits