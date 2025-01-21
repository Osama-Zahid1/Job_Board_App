# JobBoard Django Application

## Overview
The JobBoard application is a Django-based platform that connects recruiters and job seekers. It allows recruiters to post job listings and manage applications while providing job seekers the ability to browse jobs, apply for positions, and manage their profiles.

---

## Features

### General
- User registration with two types of accounts: Recruiter and Seeker.
- Login functionality with custom redirections based on user type.

### Recruiter Features
- Post and manage job listings.
- View applications submitted by job seekers.
- Update recruiter profiles.

### Seeker Features
- Browse available job listings.
- Apply for jobs, including uploading resumes.
- Update seeker profiles.

---

## Installation

### Prerequisites
- Python 3.11 or higher
- Django 4.0 or higher
- PostgreSQL database

## Key Components

### Models
- **Seekermodel**: Stores seeker information.
- **Recruitermodel**: Stores recruiter information.
- **Jobmodel**: Represents job listings.
- **Application**: Handles job applications by seekers.

### Forms
- **RegistrationTypeForm**: Handles user type selection.
- **Seekeregform & Recruiterregform**: Forms for seeker and recruiter registration.
- **LoginForm**: Manages user authentication.
- **ApplicationForm**: Allows seekers to apply for jobs.
- **seekerupform & recruiterupform**: Profile update forms for seekers and recruiters.

### Views
#### Recruiter Views
- `jform`: Handles job posting.
- `jobboard`: Displays all job listings.
- `recruitview`: Shows recruiter dashboard and applications.
- `rupdate`: Updates recruiter profile.

#### Seeker Views
- `registrationview`: Handles registration for seekers and recruiters.
- `loginview`: Manages user login.
- `dashview`: Displays the seeker dashboard.
- `supdate`: Updates seeker profile.
- `apply_for_job`: Enables seekers to apply for jobs.

---

## Usage

### Register as a User
1. Visit the registration page.
2. Choose the user type (Seeker or Recruiter).
3. Fill in the respective form and submit.

### Login
1. Navigate to the login page.
2. Enter your credentials.
3. Based on user type:
   - **Seeker**: Redirected to the dashboard to browse jobs and manage applications.
   - **Recruiter**: Redirected to the recruiter dashboard to post jobs and view applications.

### Post a Job (Recruiter)
1. Access the job posting form.
2. Fill in the job details.
3. Submit the form to publish the job.

### Apply for a Job (Seeker)
1. Browse job listings.
2. Select a job and click "Apply".
3. Fill in the application form and upload a resume if required.

---

## Future Enhancements
- Add search and filter functionality for job listings.
- Enable email notifications for job applications and status updates.
- Implement a more advanced admin panel for managing users and jobs.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it for your needs.

---

## Contributions
Contributions are welcome! If you'd like to contribute, please fork the repository, create a feature branch, and submit a pull request.

