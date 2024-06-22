# Doctor | +


![Doctor +](/static/image/responsiv1.PNG)

Portfolio 4 project as part of the Diploma in Full Stack Software Development by Code Institute.
___

Doctor +  is a blog, mainly for experted,For expert doctor in my country, this blog is designed for those who have not information about doctor and they are new in my country. That blog will help user to find doctor get information about the doctor and find the location. Moreover, they can contact doctor for opponent and further follow up.

It is a fullstack blog site that allows users to read blog posts, create an account and comment on the posts.

Link to live site - [https://doctor-plus-7e2178eca57a.herokuapp.com/](https://doctor-plus-7e2178eca57a.herokuapp.com/)

## CONTENTS

- [Doctor | +](#Doctor-Plus)
- [CONTENTS](#contents)
- [User Experience/UX](#user-experienceux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
    - [New Users Goals](#new-visitor-goals)
    - [Existing Users Goals](#existing-visitor-goals)
  - [Wireframes](#wireframes)
  - [Flow Diagram](#flow-diagram)
   - [Database Plan](#database-plan)
- [Features](#features)
  - [Registration](#registration)
  - [Future Features](#future-features)
  - [Features Not Included](#features-not-included)
- [Technologies Used](#technologies-used)
- [Programming Languages, Frameworks and Libraries Used](#programming-languages-frameworks-and-libraries-used)
- [Agile](#agile)
- [Testing](#testing)
  - [Python Testing](#python-testing)
  - [Deployment](#deployment)
    - [Github Deployment](#github-deployment)
    - [Repository deployment via Heroku](#repository-deployment-via-heroku)
  - [Credits](#credits)
  - [Media](#media)
  - [Acknowledgments and Thanks](#acknowledgments-and-thanks)

___


# User Experience/UX

## Target Audience

- Users that are looking for expert doctors,they can easily find information about doctor and read patient feedback.

## User Stories

### New User Goals

- To understand what the site and content is about.
- How to use the site.
- Create an account and leave comment at the doctor post.

### Existing Users Goals

- Log in and Log out of their account.
- Read blog posts and comments on each post.
- Add their own comments on blog posts can delete and update the comment.

___
### _User Stories_

## __User Experience (UX)__
* **As a Site Admin**


1.Post Management: As a site Admin I can create, read posts in front-end so that I can manage post content easily.
2. View comments: As a Site Admin I can view the number of comments on each post.
3. As a Site Admin I can view comments on an individual post so that I can read the conversation.
4. Approve comments: As a Site Admin I can approve or delete comments so that I can filter out bad comments.




* **As a Site User**


1. View doctor List: As a Site User I can view a list of doctor so that I can select one doctor and read information about him/her. and how to contact.
2. View Comments: As a Site User I can view comments on an individual doctor so that I can read the conversation and patient feedback about doctor treatment.
3. Account Registration: As a Site User I can register an account so that I can comment on a post.
4. Category: As a Site User I can slecte doctor based on category from various category on the page.
5. Open News Posts: As a Site User I can click on a post so that I can read the full article.
6. Site Pagination: As a Site User I can view a paginated list of doctor, so that select a news post I want to view.
7. Comment on Doctor Posts: As a Site User I can leave comments on a doctor post so that I can share my thoughts about a doctor.
8. Number of comments: Number of As a Site User I can view the number of comments on each post so that I can see which doctor is the most expert.



## Wireframes
I created Wireframes to visualize the site's design and act as a template to use when developing the site.

**Home Page**

![Doctor+ Home page](/static/image/1.PNG)


**Post Page**

![doctor+ posts](/static/image/2.PNG)

**Post Page**

![doctor+ posts user login](/static/image/6.PNG)


**Sign up page Page**

![doctor+ Sign Up](/static/image/3.PNG)



**Sign In page Page**

![doctor+ Sign In](/static/image/9.PNG)

 **Sign In page Page**

![doctor+ admin page](/static/image/11.PNG)




## Flow Diagram

Here is a diagram showing  flow through the site. There are 2 sections shown here. On is for user and one for admin of page.

![Site Flow Diagram user](/static/image/userflow.PNG)
![Site Flow Diagram admin](/static/image/admin_flow.PNG)


## Database Plan

### _ERD (Entity Relationship Diagram)_
The database plan is  simple, but it shows the information that is stored within the database, the type of data and if it is logged as a Primary or Foreign key.


** Post Data Model**

![NewsTime News\\ Post Data Model](/static/image/Post.PNG)

**User Comments Data Model**

![Comments Data Model](/static/image/comment.PNG)

**Categories Data Model**

![Categories Data Model](/static/image/category.PNG)

**News Categories Data Model**

![about Data Model](/static/image/abooutmodel.PNG)

**Contact Data Model**

Note: I created a contact model. I'll use for contact with doctor for future implementations.

![contact Data Model](/static/image/contact.PNG)



## __Features__

### _Existing Features_

* **Navigation Bar**

Every page has a fully responsive navigation bar that makes it simple to move between pages on all types of devices. Standard users only have limited access, whereas administrators have separate access.
    The logo is located on the left side and may be used as a navigation link to the home page, as well as to Add Doctor, About, Sign Up, Sign In, and Sign Out.

**Site Nav for Admins**

  ![doctor+ Navbar for Admins](/static/image/navbar.PNG)
    
**Site Nav for First time user** 

  ![doctor+ Navbar](/static/image/usernav.PNG)



* **Home Page**

The user's initial call port, the home page, consists of a collection of doctor list. The feature of this page is the links to the doctor detail items and their information, which include the name, content,  category, and published date. There's also an attention-grabbing image of the news that encourages people to click on the links and read the information. Users are able to contact with the doctor they select.

  ![doctor+ Home page](/static/image/home.PNG)


* **post detail Page**

    The users can read the detail about the doctor by clicking on the title of the doctor post.

    ![doctor+ detail page](/static/image/doctor_detaliis.PNG)


* **about Page**

    The users can read about the doctor + app .

    ![doctor+ abouty page](/static/image/aboutpage.PNG)


* **Comment**

    For those who are  registered in Doctor +, Can only read the comments and leave comment on the apost page, user that registered can edit and delete their comments..
    
    ![Doctor + Comment list](/static/image/comments.PNG)

* **Sign Up Page**

    ![Doctor + Sign Up Page](/static/image/sgnuppage.PNG)

* **Log In Page**

    ![Doctor + Sign Up Page](/static/image/sginin.PNG)

* **Log Out page**

    ![Doctor + Sign Up Page](/static/image/logoutpage.PNG)

* **Footer**

    The footer section is consistent on all pages and includes links to the relevant social media sites, and appears in the same format on all pages

    ![Doctor +  footer page](/static/image/footer.PNG)





* **Admin Home Page**

    The Admin page is only available for Admin users specifically. This page informs the superuser how to add new doctor.


    * **Add Post - Admin page**

        The Add doctor page is only accessible for Admin. This page consists of a form to be completed in order to add a new doctor post..
        The Add New Doctor Post form is fully responsive across all devices.

    ![Doctor + Admin Add New Doctor page](/static/image/add.PNG)
        




### _Future Implementations_

* Contact Form
___

# Technologies Used

Here are the technologies used for this project:

- [Gitpod](https://gitpod.io/) To build and create this project
- [Github](https://github.com) To host and store the data for the site..
- [PEP8 Validator](https://pep8ci.herokuapp.com/) Used to check python code for errors
- [ElephandSQL](https://www.elephantsql.com/) Used to store PostgreSQL database.
- [Cloudinary](https://cloudinary.com/) Used as cloud storage for images uploaded as part of the blog posts
- [Heroku](https://id.heroku.com/) Used to deploy the project

# Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)


## Testng
The portal has been well tested and the results can be viewed
[here - Manual Testing](https://github.com/LimaZurmati/doctor_plus/blob/main/TESTING.md)
### CI Python Linter 

## Python Testing
Python Files Tested:

- models
- forms
- views
- urls

___
All code passed without errors.

* **CI Python Linter blog/admin.py** 

![admin.p/blog](/static/image/admin.py_bolg.PNG)

* **CI Python Linter blog/views.py** 

![views.py](/static/image/view.py.PNG)

* **CI Python Linter blog/model.py**

![model.py](/static/image/model_blog.PNG)

* **CI Python Linter blog/foems.py** 

![views.py](/static/image/forms_blog.PNG)

* **CI Python Linter about/views.py.py** 

![about/model.py](/static/image/model_about.PNG)

* **CI Python Linter about/admin.py** 

![admin.py](/static/image/admin_about.PNG)

* **CI Python Linter about/views.py** 

![views.py](/static/image/view_about.PNG)



(*) See Bugs below

## Bugs

I created model for language but it did not shows at database so, I deleted and I will work on it after.




## Deployment

### Github Deployment

## __Deployment__

### **Create a Database**
These steps will create a PostgreSQL database:
1. Log in to ElephantSQL.com to access your dashboard
2. Click "Create New Instance"
3. Set up your plan
4. Select "Select Region"
5. Select a data center near you
6. Then click "Review"
7. Check your details are correct and then click "Create instance"
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, click the copy icon to copy the database URL


After each addition, change or removal of code, in the terminal within your IDE (I used gitpod for this project) type:

- git add .
- git commit -m "meaningful commit message"
- git push

The files are now available to view within my github repository.


### Repository deployment via Heroku

### **Heroku**

Steps for deployment:
1. Click "New" and select "Create new app".
2. Input a meaningful name for your app and choose the region best suited to your location.
3. Select "Settings" from the tabs.
4. Add the config vars:
    * Database URL (your DB URL)
    * Secret Key (Example: Any secret-key)
    * Port (In my case is 8000)

5. Select "Deploy" from the tabs.
6. Link the Heroku app to the respository.
7. Select "GitHub - Connect to GitHub" from deployment methods.
8. Search for the GitHub repository by name.
9. Either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually.
 Manually deployed branches will need re-deploying each time the repo is updated.
10. Click on Deploy.
11. Click View button to view the deployed site.

- Cloudinary URL
- Postgres Database URL
- Port (8000)


## Credits

I have to Acknowledgement that the Code Institute LMS, in particular the CI I Think Therefore I Blog Walkthrough. From this base I used a lot of the desighn and styling with Bootstrap and custom CSS.it was the main and big guide for me during devloping the site. I followed this project step by step and applied the steps in my project development journey. also I used same django code as walkthrough for upadte and delete comment.
2. Django Documentation
3. Stack Overflow
4. W3Schools
5. for doctor information it need research to find expert doctor.In addition, I take this informaton from this site (https://www.amc.com.af/doctor/manizha-qarizada-amc)

for add doctor I watched[youtube](https://www.youtube.com)

The Readme layout was based on the example by [Sideqa - Readme Examples](https://github.com/sediqa01/News-Aggregator/blob/main/README.md) and [Markdaine - Readme](https://github.com/markdaniel1982/MD82-P4/blob/main/README.md)

The wireframe mockups were created using [Balsmiq](https://balsamiq.cloud/syn7g2q/projects)


___

## Media

All other images are taken from Amiry Hosptal my own.

___

## Acknowledgments and Thanks

 1. [Our CI Tutor Support team:](https://learn.codeinstitute.net/ci_support/diplomainfullstacksoftwarecommoncurriculum/tutor) a heartful thanks for always being there for us!:
- Sarah
- Holy
 and salck community (https://app.slack.com) 
