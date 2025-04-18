# Blog
A blogging platform built with the Django framework is a technology-focused web application designed for creating, publishing, and managing blog posts. It offers a user-friendly content management system for bloggers. Users can sign up to follow authors they find interesting, and if inspired, they can start posting their own new tech content on the platform.

## Features
- Sign Up
- Log In
- Manage Posts
- Follow (or) Unfollow Authors
- Update Profile
- Change Password
- Change Email Address
- Two Factor Authentication

## Installing
### Clone the project

```bash
git clone https://github.com/shivatejaburle/blog-102
cd blog-102
```

### Setup your Virtual Environment
```bash
pip install virtualenv
virtualenv venv
# For Windows
venv\Scripts\activate   
# For Mac
source venv/bin/activate 
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Environment Settings

Create `blog-102/.env` to store Email Configurations.

```bash
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '<YOUR_SMTP_HOST>'
EMAIL_PORT = <YOUR_PORT_NUMBER>
EMAIL_USE_TLS = <True_OR_False>
EMAIL_HOST_USER = '<YOUR_EMAIL_ADDRESS>'
EMAIL_HOST_PASSWORD = '<YOUR_PASSWORD>'
```

### Collect static files (only on a Production Server)

```bash
python manage.py collectstatic
```

### Running a Development Server

Just run this command:

```bash
python manage.py runserver
```
Your application will be available @ http://127.0.0.1:8000/

### Login Information
- **Test User**: 
    - Username : testuser
    - Password : test_12345

## Screenshots
### Home Page
![Home Page](screenshots/01-Home-Page.jpg)
### Blog
![Blog](screenshots/02-Blog.jpg)
### Sign Up
![SignUp](screenshots/03-SignUp.jpg)
### Login
![SignIn](screenshots/04-Login.jpg)
![TFA](screenshots/05-2FA.jpg)
![MyPosts](screenshots/06-MyPosts.jpg)
![ManagePost](screenshots/07-Manage-Post.jpg)
![MyFollowers](screenshots/08-MyFollowers.jpg)
![Follow-or-Unfollow](screenshots/09-Follow-or-Unfollow.jpg)
![AuthorProfile](screenshots/10-Author-Profile.jpg)
![ChangePassword](screenshots/11-change-password.jpg)
![ManageEmail](screenshots/12-add-or-remove-email.jpg)
![Manage-2FA](screenshots/13-Manage-2FA.jpg)
![LoginSessions](screenshots/14-login-sessions.jpg)
### Mobile View
&emsp;![Home Page](screenshots/M1-Home.png)&emsp;&emsp;&emsp;![Posts](screenshots/M2-Posts.png)

&emsp;![ViewPost](screenshots/M3-View-Post.png)&emsp;&emsp;&emsp;![Profile](screenshots/M4-Profile.png)

**Note:** All pages are responsive with small, medium and large devices.
