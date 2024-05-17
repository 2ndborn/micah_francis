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
#### HTML Home ![home](/media/html_val.home.png)
#### HTML About![about](/media/html_val.about.png)
#### HTML Portfolio![portfolilo](/media/html_val.portfolio.png)
#### HTML Contact ![contact](/media/html_val.contact.png)
### CSS![CSS](/media/val_css.png)
### JavaScript
#### Reveal Login Button ![contact](/media/val_js_reveal.btn.png)
#### Back To Top Button ![contact](/media/val_js.btt.png)
### Python
#### Home
###### Views.py![views](/media/p_home.views.png)
###### Urls.py![urls](/media/p_home.urls.png)
#### About
###### Views.py![views](/media/p_about.views.png)
###### Urls.py![urls](/media/p_about.urls.png)
###### Models.py![models](/media/p_about.models.png)
###### Forms.py![forms](/media/p_about.forms.png)
###### Admin.py![admin](/media/p_about.admin.png)
#### Portfolio
###### Views.py![views](/media/p_port.views.png)
###### Urls.py![urls](/media/p_port.urls.png)
###### Models.py![models](/media/p_port.models.png)
###### Forms.py![forms](/media/p_port.forms.png)
###### Admin.py![admin](/media/p_port.admin.png)
#### Contact
###### Views.py![views](/media/p_contact.views.png)
###### Urls.py![urls](/media/p_contact.urls.png)
###### Models.py![models](/media/p_contact.models.png)
###### Forms.py![forms](/media/p_contact.forms.png)
###### Admin.py![admin](/media/p_contact.admin.png)
### Test Procedures
#### Navigation
When the logo is selected on the Home page does it refresh the Home page?
*The Home page is refreshed when the logo is selected on the home page* 

When the logo is selected on the About Me, Portfolio or Contact Me pages does it render the Home page?
*The Home page is rendered when the logo is selected from the About Me, Portfolio or Contact Me page*

When the Home button is selected does it render the Home page?
*The home page is rendered when the Home button is selected*

When the About Me button is selected does it render the About Me page?
*The About Me page is rendered when the About Me button is selected*

When the Portfolio button is selected does it render the Portfolio page?
*The Portfolio page is rendered when the Portfolio button is selected*

When the Contact Me button is selected does it render the Contact Me page?
*The Contact Me page is rendered when the Contact Me button is selected*
#### Home Page
When the LinkedIn/GitHub icons are selected does it render a new window with the owners LinkedIn/GitHub profiles?
*A new window with the owners LinkedIn/GitHub profiles are rendered when the LinkedIn/GitHub icons are selected*

When the learn more button is selected does it render the About Me page?
*The About Me page is rendered when the learn more button is selected*

When "Micah Francis" is clicked 3 times on the Home page, is the footer with the padlock sign-in icon revealed?
*The footer with the padlock icon is revealed when "Micah Francis" on the Home page is clicked 3 times*

#### About Me Page
When the Education, Techical Skills, Work Experience and Interests headers are selected does  it reveal hidden content?
*Hidden content is revealed when the Education, Techical Skills, Work Experience and Interests headers are selected*

When the Portfolio button is selected does is render the Portfolio page?
*The Portfolio page is rendered when the Portfolio button is selected*

#### Portfolio Page
When the website link is selected does it render a new window with the website?
*A new window with the website is rendered when the website link is selected*

When the GitHub link is selected does it render a new window with the GitHub site?
*A new window with the GitHub site is rendered when the GitHub link is selected*

When the website image is selected does it render a new window with the website?
*A new window with the website is rendered when the website image is selected*

When the Contact Me button is selected does it render the Contact Me page?
*The Contact Me page is rendered when the Contact Me button is selected*

#### Contact Me
When the contact me form is submitted does the user receive the message "Your message has been sent"?
*The user received the message "Your message has been sent" when the contact form has been submitted*

When the contact me form is submitted does the owner receive the message is their inbox?
*The owner receives the message is their inbox when the user submits the contact me form*

#### Owners Options
##### Sign-in/Sign-out/Forgotten Password
When the padlock icon on the footer is selected does it render the sign-in page?
*The sign-in page is rendered when the padlock icon on the footer is selected*

When the owner signs in does the owner receive the message "Successfully signed in as 'owners name'"?
*The owner receives the message "Successfully signed in as 'owners name'"is when the owner signs in*

When the unlocked padlock icon on the footer is selected does it render the sign out page?
*The sign out page is rendered when the unlocked  padlock icon on the footer is selected*

When the owner signs out does the owner receive the message "Successfully signed out"?
*The owner receives the message "Successfully signed out" when the owner signs out*

When the forgotten password link is selected does the owner receive the message is their inbox to reset their password?
*The owner receives the message is their inbox to reset their password when the forgotten password link is selected*

##### About Me
When the About Me page is rendered and there are no entries does it display edit and delete and add buttons?
*The edit and delete buttons are not visible when the About Me page is rendered without any entries but the add buttons are*

When an add form is submitted does it display the message "Executive Summary/Education/Work Experience/Interests added"
*The message "Executive Summary/Education/Work Experience/Interests added" is displayed when an add form is submitted*

When the About Me page is rendered with entries are the edit and delete buttons visible?
*The edit and delete buttons are visible for each entry when the About Me page is rendered*

When the Executive Summary has an entry is the add button hidden?
*The add button is not visible when the Executive Summary has an entry* 

When the add Executive Summary/Education/Work Experience/Interests form button is selected on the About Me page does is render the add Executive Summary/Education/Work Experience/Interests form?
*The add Executive Summary/Education/Work Experience/Interests form is rendered when the add button is selected* 

When an add form is submitted does it display the message "Executive Summary/Education/Work Experience/Interests added"
*The message "Executive Summary/Education/Work Experience/Interests added" is displayed when an add form is submitted*

When the edit Executive Summary/Education/Work Experience/Interests form button is selected on the About Me page does is render the Edit Executive Summary/Education/Work Experience/Interests form?
*The edit Executive Summary/Education/Work Experience/Interests form is rendered when the Edit buttons is selected*

When an edit form is submitted does it display the message "Executive Summary/Education/Work Experience/Interests updated"
*The message "Executive Summary/Education/Work Experience/Interests updated" is displayed when an edit form is submitted*

When the delete Executive Summary/Education/Work Experience/Interests form button is selected on the About Me page does it delete Executive Summary/Education/Work Experience/Interests entry?
*The Executive Summary/Education/Work Experience/Interests entry is deleted when the delete buttons is selected*

When the delete button is selected does it display the message "Executive Summary/Education/Work Experience/Interests deleted"
*The message "Executive Summary/Education/Work Experience/Interests deleted" is displayed when an delete button is selected*

##### Portfolio
When the add Portfolio button is selected on the Portfolio page does is render the add Portfolio form?
*The add Portfolio form is rendered when the add Portfolio buttons is selected* 

When the add Portfolio form is submitted does it display the message "Portfolio added"
*The message "Portfolio added" is displayed when the add Portfolio form is submitted*

When the Edit Portfolio form button is selected on the Portfolio page does is render the Edit Portfolio form?
*The Edit Portfolio form is rendered when the Edit Portfolio buttons is selected*

When the edit Portfolio form is submitted does it display the message "Portfolio updated"
*The message "Portfolio updated" is displayed when the edit Portfolio form is submitted*

When the delete Portfolio is selected on the Portfolio page does it delete Portfolio entry?
*The Portfolio entry is deleted when the delete Portfolio buttons is selected*

When the delete button is selected does it display the message "Portfolio deleted"
*The message "Portfolio deleted" is displayed when the Portfolio delete button is selected*

### Device Testing
#### 1024
![1024](/media/1024.png)
#### 1024
![912](/media/912.png)
#### 820
![820](/media/820.png)
#### 768
![768](/media/768.png)
#### 540
![540](/media/540.png)
#### 430
![430](/media/430.png)
#### 390
![390](/media/390.png)
#### 344
![280](/media/344.png)
### Fixed Bugs 
#### Bug 1
I wanted to make a change to the portfolio model as I felt it necessary to include the git hub address as well as the web address. I made the amendment and migrations, then tested it on GitPod. It worked so I deployed my changes to Heroku, or so I thought. I went on the portfolio page and got message "ProgrammingError at /portfolio/". I attempted to migrate my changes again changing the title of the model instance, but this did nothing. I googled "ProgrammingError at /portfolio/" and found on Stack Overflow that  I needed to migrate my changes which I had already done. Finally I typed in "ProgrammingError at /portfolio/" into Slack and found a message from a student called Tony Wilson_5p querying the same thing as me. The answer he got was that he wasn't deploying the database migrations on Heroku. So I login in to Heroku via the terminal and migrated the changes using *"heroku run python manage.py migrate --app micah-francis"* and it worked. ![Bug 1.1](/media/bug_1.1.jpg) ![Bug 1.2](/media/bug_1.2.jpg)
### Browser Tests
#### Chrome
##### Home ![Home](/media/chrome_home.png)
##### About ![About](/media/chrome_about.png)
##### Portfolio ![Portfolio](/media/chrome_portfolio.png)
##### Contact ![Contact](/media/chrome_contact.png)
#### Edge
##### Home ![Home](/media/edge_home.png)
##### About ![About](/media/edge_about.png)
##### Portfolio ![Portfolio](/media/edge_portfolio.png)
##### Contact ![Contact](/media/edge_contact.png)
#### FireFox
##### Home ![Home](/media/ff_home.png)
##### About ![About](/media/ff_about.png)
##### Portfolio ![Portfolio](/media/ff_portfolio.png)
##### Contact ![Contact](/media/ff_contact.png)
#### Opera
##### Home ![Home](/media/op_home.png)
##### About ![About](/media/op_about.png)
##### Portfolio ![Portfolio](/media/op_portfolio.png)
##### Contact ![Contact](/media/op_contact.png)
## Deployment
### Gitpod
1. Go to [https://gitpod.io/](https://gitpod.io/)
 2. In the Workspaces section click on “https://gitpod.io/start/#2ndborn-micahfrancis-hhjghrrn4qgj”. 
![Workspace](/media/gitpod_workspace.png)
 3. Once the page is loaded open a new terminal and type “python3 manage.py runserver”. Then press Enter.
![Terminal](/media/gitpod_terminal.png)
 4. Options to open the preview page or the browser will be shown. Click on the browser.
![Port Options](/media/gitpod_brow.options.png)
 5. The browser will open.
![webpage](/media/gitpod_website.png)
### Heroku
1. Go to [Heroku.com ](https://id.heroku.com/login)
![heroku_webpage](/media/hero0.jpg)
2. From the home page find the application "micah-francis" and click on it.
![heroku_homepage](/media/hero_dash.png)
3.	Click on the deploy tab.
![deploy_tab](/media/hero_deploy.png)
4. Scroll down to deployment method, click on GitHub, search for your repository profile, key in the name of the repository and then press search. ![heroku_install](/media/hero_github.png)
5. Once the repository has been found click on connect. This will initially the install process.![heroku_install](/media/hero_connect.png)
6. Once installation has been completed, press enable automatic deploy.
![heroku_enable](/media/hero_auto.png)
7. Press deploy.
![heroku_press_deloy](/media/hero6.jpg)
8. Finally, click on the Open App button at the top of the page.
![heroku_open_app](/media/hero7.jpg)
