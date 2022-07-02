Readme
Table of contents:
Theme, Epic and User Stories
Design and UX
Wireframes
Database model
Features
Future Features
SEO and Marketing
Technologies
Testing
Code Validation
Browser Compatibility
Accessibility Testing
Performance Testing
Manual Testing
User Stories Testing
Debugging and known bugs
Deployment
Credits
Resources
Acknowledgements

Name: Winnifrederico's Wondrous World of Wizards (WWWW)

Live link: https://w-w-w-w.herokuapp.com/

Screenshot:

### Theme, Epic and User Stories

#### Theme

To sell interesting wizard hats (and other wizard associated clothing items) online.

#### Epic

This website will provide the user with an array of wizardly hats and other clothing items, products both expected and unexpected. The website will be simple and easy to use; a good experience for the user that will make their time in the shop, so to speak, welcoming. Each product will have Dungeons and Dragons style stats (link) which will be calculated and presented at checkout along with a randomly generated name (link) to ‘create’ a wizard based on these products. The user can choose to accept the generated wizard name and stats, or keep shopping to get a different wizard.

#### User stories

#### User

As a user, I can clearly see the purpose of the site when I land on the home page so that I stay on the site.

As a user, I can clearly understand the products I am considering purchasing. so that I can make informed decisions.

As a user, I have the option to create a custom made hat so that I can have something that better suits me.

As a user, I can get an instant quote for a custom hat so that I know how much I will be spending.

As a user, I can complete the payment process quickly and easily so that I don’t get distracted/dissuaded and leave.

As a user, I will be notified by email when my order has been placed successfully, so that I have trust in the website and I have the order details in a convenient place.

As a user, I have the option for my information to be saved for future purchases so that I can save time on future purchases.

As a user, I can edit or delete my user information so that I can have the correct information.

As a user, I can easily find the site terms and conditions so that I can use the site knowing I am protected.

As a user, I can see the stats of each item, so that I can have an experience outside of the standard online shopping experience.

As a user, I can see the final stats of my outfit, so that I can have an experience outside of the standard online shopping experience.

As a **user** I can **see the shopping bag** so that **I can keep track of my shopping while I browse the site**.

As a **user** I can **view my order history** so that **I know what I have already ordered**.

#### Owner/staff member

As a staff member, I can add products to my shop so that users can see the products I have available.

staff edit and delete

As a staff member, I can control stock levels so that I do not accidentally over or undersell a product.

As a staff member, I will be notified by email if an order comes in so that I can action the sale.

As a staff member, I can view my orders and see the current order status so that I know if there is an order I have to process.

As a staff member, I can easily provide the site terms and conditions so that I can communicate with users and increase the legitimacy of my website.

Clear design

Ts and Cs prominent in footer

As a staff member, I can use web marketing to increase traffic to my site.

As a staff member, I will be provided with search engine optimisation for my site so that I can receive increased traffic and sales.

User/Owner

As a user/staff member, I can sign in and out intuitively so that I can use the website easily.

As a user/staff member, I can navigate the website easily and intuitively.


### Design and UX

### Wireframes

Home page

Shop page

Shopping bag view

Checkout view

Standard hat product detail

Custom hat page

User profile page

About Us page (related links)

Database model

Made in Lucidchart.

### Features


### Future Features


### SEO and Marketing

[Link to Readme documention for SEO and marketing](/SEO_MKTG_README.md)


### Technologies

Languages used:
Python 3
HTML5
CSS
Javascript
Frameworks, Libraries and Programs Used:
Django/allauth - Python framework
Bootstrap - CSS package
AWS - for hosting the images
SQLite (default Django database)
EmailJS/Django email - for sending the personalised/automated emails
GitHub - for hosting the site
Heroku - for the deployment of the site
Gitpod - for editing the files

### Testing

#### Code Validation

Python validator

Javascript validator

HTML validator

CSS validator

#### Browser Compatibility

Browser Compatibility checks were run using BrowserStack and my computer. The results are:

Firefox - 

Chrome - 

Opera - 

Microsoft Edge - 

Due to Bootstrap the styling is not ideal on some browser/OS combinations - this is as per the Bootstrap documentation below. All systems still function as needed on all combinations. Bootstrap Browser Compatibility

#### Accessibility Testing

Accessibility testing was conducted using Accessibility Test.org. The results are:

#### Performance Testing

Performance testing was conducted using Lighthouse. The results are:

#### Manual Testing

I sent the live link to friends and family members for testing and feedback. The site was received positively; design and usability suggestions were considered and acted on. The site was also put up in the Code Institute Slack community for feedback.

### Debugging and known bugs


### Deployment

#### Publishing
The project was deployed using Heroku. The process is as follows:

Once you have signed up to Heroku, on the top right of the dashboard there is a button labelled 'New'. This will open a dropdown; please select 'Create new app'. On the next page you can choose your region and a name for the project. Then click 'Create app'.

On the next page there is a menu along the top. Navigate to 'Settings', where you will find the config vars. Scroll down to the section named 'Config vars' and click on the button labelled 'Reveal config vars'. Cloudinary (AWS?) and Postgres will both need config vars as per your own details. You will also need to set a secret key. Once the config vars are saved, back in Gitpod save them in an env.py file. Make sure to add env.py to your .gitignore list so that your config vars do not become publically available on Github.

If you scroll back to the top of the page you will find the 'Deploy' tab, which has multiple options for deployment. I used Github for this project. When you click on the Github button a bar will come up for you to search for the repo you wish to connect to.

Once you have connected, you have the option to deploy automatically (the app will update every time you push) or manually (update only when you choose). I chose automatic but you can do what suits you.

After the first push/update, your app will be ready to go!

#### Forking and Cloning

To save a copy of the code and work on it yourself, here are the steps for forking and cloning using Github:
In the repository, click the 'Fork' button, which is on the top right-hand side, next to 'Star'.

Github will automatically create a new repo, which is forked from the original. If you would like to clone it you have two options:
Within the repository, click the 'Code' dropdown, which is located next to 'Add File' on the right (underneath the Settings tab); there is an option to download all files and save a copy locally.

In the same 'Code' dropdown, you can opt to open the code with GitHub Desktop and work from there.

### Resources

Django 3.2 documentation

Bootstrap documentation

Cloudinary/Django documentation/AWS

EmailJS documentation

Guidance with updating and deleting Page instances from GeeksforGeeks.

Photo editing from Pixlr.

Favicon generated from Favicon.io

ERD made with Lucidchart

Wireframes made with Balsamiq.

Privacy Policy generated from (Privacy Policy Generator)[https://www.privacypolicygenerator.info].

### Credits

All images from Pexels.

In code credits as marked.

### Acknowledgements