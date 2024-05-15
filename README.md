# My Website
## Project Goal
The goal of the Micah Francis is to showcase the web development portfolio of Micah Francis to attract the attention of prospective employers/clients that are in need of his services.
## User Goals
Users should be able to view Micah Francis' Biography, Work History, Skills, Porfolio and contact information.
## Owners Goals
To provide potential clients and employers with the opportunity to view Micah Francis' portfolio.
## User Stories
### Users
 * I want to view a welcoming home screen so that I feel enticed to find out more. ![Home screen](/media/us_home.jpg)
 * I want to view an about me section so that I can understand what his goals and aspirations are. ![About Me screen](/media/us_about.jpg)
 * I want to view Micah Francis' portfolio so I can evidence his skills and attributes. ![Portfolio screen](/media/us_portfolio.jpg) ![web/git](/media)
 * I would like to view a contact form so I can contact Micah Francis. ![Contact screen](/media/us_contact.jpg)
 * I want to know the area Micah Francis is located in so I can measure the distance he may need to travel from. ![Location](/media/us_location.jpg)
 * I want a link to Micah Francis' social media accounts so that I can observe his activity. ![Social media links](/media/us_github.jpg) [Social media links](/media/us_linkedin.jpg)
### Owners
 * I want to be able to login into the site so I can amend the sites content. ![Login](/media/us_signin.jpg)
 * I want to be able to add, update and delete the portfolio section so I ensure the site is kept up to date. ![CRUD port](/media/us_crud_portfolio.jpg)
 * I want to be able to add, update and delete executive summary, education, work experience and additional information/interest so I can ensure the website is kept up to date. ![CRUD w,e,i](/media/us_crud_about.jpg)
 * I want to receive an email when the contact form is completed so can response to any requests. ![email/message](/media/us_contact_test.jpg) ![email/message](/media/us_test_email.jpg)
## Future Features
 * The owner will be able to update the tech skills section.
 * The owner will be able to add up to 7 achievement.
## Typography & Colours
**Fonts**
 * Body text = martel-sans
 * Name-link and title-link = Noto-sans

**Colours**
* Overlay = White
* btt-buton, main text, footer background  = #000028
* Tech skills card = #e6f1ff
* form background = #e6eefa
* h1 and nav hover = #0000286b
* sign-in, sign-out a tag = #9bf2ff
* title page background = rgba(255, 255, 255, 0.6)
## Wireframes
The Template ![Template](/media/wf_template.jpg)
Home page ![Home](/media/wf_home.jpg)
About Me ![About Me](/media/wf_about.jpg)
Portfolio ![Portfolio](/media/wf_portfolio.jpg)
Contact ![Contact](/media/wf_contact.jpg)
Owners Login ![Owners Login](/media/wf_login.jpg)
## Technology
- [GitPod](https://gitpod.io/workspaces) to build the repository.
- [GitHub](https://github.com/Code-Institute-Org/ci-full-template) to push changes to the repository.
- [Heroku](https://id.heroku.com/login) to deploy the application.HTML and CSS code
- [jslint](https://www.jslint.com/) to validate JavaScript code.
- [Balsamiq](https://balsamiq.com/) for creating the wireframe
- [Font Awesome](https://fontawesome.com/v4/) for the icons
- [Google fonts](https://fonts.google.com/) to search for the right fonts for the website
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)  to create forms and buttons.
- Chrome Developer Tools for device testing.
- Pictures of Micah Francis taken on an iPhone by Kara Francis.
## Testing
### Code Validation
### Test Procedures
### Fixed Bugs 
#### Bug 1
I wanted to make a change to the portfolio model as I felt it necessary to include the git hub address as well as the web address. I made the amendment and migrations, then tested it on GitPod. It worked so I deployed my changes to Heroku, or so I thought. I went on the portfolio page and got message "ProgrammingError at /portfolio/". I attempted to migrate my changes again changing the title of the model instance, but this did nothing. I googled "ProgrammingError at /portfolio/" and found on Stack Overflow that  I needed to migrate my changes which I had already done. Finally I typed in "ProgrammingError at /portfolio/" into Slack and found a message from a student called Tony Wilson_5p querying the same thing as me. The answer he got was that he wasn't deploying the database migrations on Heroku. So I login in to Heroku via the terminal and migrated the changes using *"heroku run python manage.py migrate --app micah-francis"* and it worked. ![Bug 1.1](/media/bug_1.1.jpg) ![Bug 1.2](/media/bug_1.2.jpg)
### Browser Tests
## Deployment
### Gitpod
### Heroku

