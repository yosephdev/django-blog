![Responsive Design](#)

[View the deployed site on Heroku](https://code-ninja-6985a427438a.herokuapp.com/)

# Project Name

CodeStar Django Blog

## Table Of Contents:

1. [Design & Planning](#design--planning)
    * [User Stories](#user-stories)  
2. [Project Overview](#project-overview)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [Credits](#credits)

## Design & Planning

### User Stories

User Story 1: **As a Site User,**  
**I can click on a post so that I can read the full text.**  
> **AC1:** When a blog post title is clicked on, a detailed view of the post is seen.

User Story 2: **As a Site User / Admin,**  
**I can view comments on an individual post so that I can read the conversation.**  
> **AC1:** Given one or more user comments, the admin can view them.  
> **AC2:** Then a site user can click on the comment thread to read the conversation.

User Story 3: **As a Site User,**  
**I can register an account so that I can comment on a post.**  
> **AC1:** Given an email, a user can register an account.  
> **AC2:** Then the user can log in.  
> **AC3:** When the user is logged in, they can comment.

User Story 4: **As a Site User,**  
**I can leave comments on a post so that I can be involved in the conversation.**  
> **AC1:** When a user comment is approved.  
> **AC2:** Then a user can reply.  
> **AC3:** Given more than one comment, there is a conversation thread.

User Story 5: **As a Site User,**  
**I can modify or delete my comment on a post so that I can be involved in the conversation.**  
> **AC1:** Given a logged-in user, they can modify their comment.  
> **AC2:** Given a logged-in user, they can delete their comment.

User Story 6: **As a Site Admin,**  
**I can create, read, update, and delete posts so that I can manage my blog content.**  
> **AC1:** Given a logged-in user, they can create a blog post.  
> **AC2:** Given a logged-in user, they can read a blog post.  
> **AC3:** Given a logged-in user, they can update a blog post.  
> **AC4:** Given a logged-in user, they can delete a blog post.

User Story 7: **As a Site Admin,**  
**I can create draft posts so that I can finish writing the content later.**  
> **AC1:** Given a logged-in user, they can save a draft blog post.  
> **AC2:** Then they can finish the content at a later time.

User Story 8: **As a Site Admin,**  
**I can approve or disapprove comments so that I can filter out objectionable comments.**  
> **AC1:** Given a logged-in user, they can approve a comment.  
> **AC2:** Given a logged-in user, they can disapprove a comment.

User Story 9: **As a Site User,**  
**I can view a paginated list of posts so that I can select which post I want to view.**  
> **AC1:** Given more than one post in the database, these multiple posts are listed.  
> **AC2:** When a user opens the main page, a list of posts is seen.  
> **AC3:** Then the user sees all post titles with pagination to choose what to read.

User Story 10: **As a Potential Collaborator,**  
**I can fill in a contact form so that I can submit a request for collaboration.**  
> **AC1:** The contact form includes fields for name, email, and message. 
> **AC2:** Upon submission of the form, the data is saved as a collaboration request.
> **AC3:** After submitting the form, a confirmation message is displayed to the user.

User Story 11: **As a Site Admin,**  
**I can store collaboration requests in the database so that I can review them.**  
> **AC1:** Collaboration requests are stored in the database upon submission.  
> **AC2:** The admin can mark collaboration requests as "read" after reviewing them.
> **AC3:** There is a visible indicator or counter for unread collaboration requests in the admin interface.

## Project Overview

This project is a full-featured Django blog application designed to showcase various aspects of web development, including database-backed projects, deployment to Heroku, hosting uploaded images on a Cloud provider, creating function-based views, utilizing Django generic views, adding authentication, creating custom models, and adding interactivity using JavaScript. The principles and mechanics of Django design learned throughout this project can be applied to other projects as well.

## Features

- Create a database-backed Django project and deploy it to Heroku.
- Host uploaded images on a Cloud provider.
- Create function-based views in a Django project.
- Utilize Django generic views.
- Add authentication.
- Create custom models.
- Add interactivity using JavaScript.

## Technologies Used

- Django
- Heroku
- ElephantSQL
- Cloudinary

## Setup and Installation

To set up and install the project locally, follow these steps:

1. **Clone the Repository:**
   - Clone the project repository from GitHub to your local machine using the following command:
     ```
     git clone <repository_url>
     ```

2. **Navigate to the Project Directory:**
   - Change directory to the cloned project folder:
     ```
     cd <project_folder_name>
     ```

3. **Create a Virtual Environment:**
   - Set up a virtual environment for the project to isolate dependencies:
     ```
     python -m venv venv
     ```

4. **Activate the Virtual Environment:**
   - Activate the virtual environment based on your operating system:
     - **Windows:**
       ```
       venv\Scripts\activate
       ```
     - **macOS/Linux:**
       ```
       source venv/bin/activate
       ```

5. **Install Dependencies:**
   - Install the required dependencies for the project using pip:
     ```
     pip install -r requirements.txt
     ```

6. **Set Up Database:**
   - Create a PostgreSQL database for the project and configure the database settings in the `settings.py` file accordingly.

7. **Run Migrations:**
   - Apply database migrations to create the necessary database tables:
     ```
     python manage.py migrate
     ```

8. **Create Superuser (Optional):**
   - Optionally, create a superuser account to access the Django admin interface:
     ```
     python manage.py createsuperuser
     ```

9. **Run the Development Server:**
   - Start the Django development server to run the project locally:
     ```
     python manage.py runserver
     ```

10. **Access the Project:**
    - Once the server is running, access the project in your web browser at:
      ```
      http://localhost:8000/
      ```

## Usage

1. **Viewing Blog Posts:**
   - Upon accessing the deployed site, users can browse through the list of blog posts displayed on the main page.
   - Click on a post title to view its full content.

2. **Commenting on Posts:**
   - To leave a comment on a post, users need to register an account and log in.
   - Once logged in, users can navigate to the desired blog post and submit their comments via the provided form.

3. **Managing Blog Content (Admin Users Only):**
   - Admin users have additional privileges to manage blog content, including creating, updating, and deleting posts.
   - To access admin functionalities, log in with admin credentials and navigate to the admin dashboard.
   - From the dashboard, admin users can perform various actions such as creating new posts, editing existing ones, and managing user comments.

4. **Drafting Blog Posts:**
   - Admin users can also save draft posts for future editing and publishing.
   - To create a draft post, navigate to the post creation page and select the "Save Draft" option instead of publishing immediately.

5. **Approving/Disapproving Comments:**
   - Admin users can review and moderate comments left by site users.
   - Comments can be approved or disapproved based on their content and relevance to the blog post.

6. **Collaboration Requests:**
   - Users interested in collaboration opportunities can submit requests via the contact form provided on the site.
   - Upon submission, collaboration requests are stored in the database for review by admin users.

7. **Pagination:**
   - To navigate through multiple blog posts efficiently, pagination is implemented, allowing users to browse through a paginated list of posts.
   - Pagination controls are available at the bottom of the main page to navigate between pages.

8. **Accessibility Features:**
   - The site includes accessibility features such as aria attributes and semantic HTML to ensure compatibility with assistive technologies like screen readers.
   - Users with disabilities can navigate and interact with the site comfortably, ensuring a positive user experience for all.

## Testing

This section provides information about the testing procedures and tools used in the project. For detailed instructions and examples, please refer to the project documentation.

### Overview

Testing is an essential aspect of ensuring the reliability and functionality of the project. By writing and running tests, I verify that each component behaves as expected and meets the specified requirements.

### Procedures

The testing procedures in this project involve:

1. **Unit Tests**: Unit tests focus on testing individual components, such as functions, methods, and classes, to ensure they perform as intended.

2. **Integration Tests**: Integration tests verify that different parts of the system work together correctly. These tests ensure that the interactions between components produce the expected outcomes.

3. **End-to-End Tests**: End-to-end tests simulate user interactions with the application to validate its behavior from start to finish. These tests ensure that the application functions correctly from the user's perspective.

### Tools Used

The project utilizes the following tools for testing:

- **Django Test Framework**: Django provides a built-in testing framework that simplifies the process of writing and running tests for Django applications. It includes tools for creating test cases, assertions, and managing test databases.

## Deployment

### Step 1: Set up your Heroku account

If you haven't already, sign up for a [Heroku account](https://www.heroku.com/) and verify your account via email.

### Step 2: Install Heroku CLI

Download and install the [Heroku Command Line Interface (CLI)](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

### Step 3: Log in to Heroku CLI

Open your terminal or command prompt and log in to Heroku CLI using the command:

heroku login

Follow the prompts to log in with your Heroku account credentials.

### Step 4: Prepare your Django project for deployment

Make sure your Django project is ready for deployment:

- Ensure all necessary dependencies are listed in your `requirements.txt` file.
- Confirm that your project is using a supported database for Heroku, such as PostgreSQL.
- Adjust your project settings to handle static files and media files properly in production.

### Step 5: Initialize Git repository and commit changes

Navigate to your project directory in the terminal and initialize a Git repository if you haven't already:

git init

Add all files to the Git repository and commit your changes:

git add .
git commit -m "Initial commit"

### Step 6: Create a new Heroku app

Create a new Heroku app using the Heroku CLI:

heroku create <your-app-name>

Replace `<your-app-name>` with your desired Heroku app name. If you omit the app name, Heroku will generate a random one for you.

### Step 7: Add a PostgreSQL database to your Heroku app

Add a PostgreSQL database to your Heroku app by running:

heroku addons:create heroku-postgresql:hobby-dev

This command will add a free Hobby Dev plan PostgreSQL database to your Heroku app.

### Step 8: Configure Django settings for production

Update your Django project settings to use environment variables for sensitive information and configure settings for the production environment, such as database connection settings and security settings.

### Step 9: Configure static files handling

Configure your Django project to handle static files properly in production. You can use [WhiteNoise](http://whitenoise.evans.io/en/stable/) or [django-heroku](https://github.com/heroku/django-heroku) to simplify this process.

### Step 10: Deploy your Django project to Heroku

Deploy your Django project to Heroku by pushing your code to the Heroku remote repository:

git push heroku master

This command will push your code to Heroku and trigger the deployment process.

### Step 11: Run database migrations

After deploying your project, run database migrations on the Heroku server:

heroku run python manage.py migrate

This command will execute database migrations on your Heroku app.

### Step 12: Set up Heroku environment variables

Set any necessary environment variables for your Heroku app using the Heroku CLI:

heroku config:set ENV_VARIABLE=value

Replace `ENV_VARIABLE` with the name of your environment variable and `value` with its value.

### Step 13: Open your deployed app

Once the deployment process is complete, open your deployed app using the following command:

heroku open

This will open your app in a web browser, allowing you to verify that it's running correctly.

Congratulations! You've successfully deployed your Django project to Heroku. You can now share the URL of your deployed app with others.

## Credits

- [Niel McEwen](https://github.com/NielMc)
- [Matt Rudge](https://github.com/lechien73)