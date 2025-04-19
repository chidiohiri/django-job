# Django Job

Django job is a role-based job board web application developed with Django, crafted to seamlessly connect recruiters and candidates within a structured, secure, and scalable digital environment. It provides an end-to-end recruitment solution, enabling recruiters to post and manage job listings while giving candidates the tools to discover, save, and apply for opportunities that match their career goals. The platform emphasizes accountability and control through wallet-based restrictions on job postings, ensuring only verified and committed recruiters can publish listings. With a clean user interface, robust filtering, and built-in application tracking, the system is tailored to simplify and optimize the hiring and job search process from both ends.

### Getting Started

These instructions will guide you through setting up Django Job on your local machine for development and testing purposes. This guide assumes you are working on a Windows environment. Mac and Linux users can adapt the commands accordingly.

### Prerequisites

Below are the dependencies for the project. For quicker installation, please refer to the [requirements.txt](requirements.txt) file.
- [Python](https://www.python.org/downloads/) - The programming language used to build the backend of the application.
- [Django](https://www.djangoproject.com/download/) - The web framework that powers the server-side logic, database models, and URL routing.
- [Visual Studio Code](https://code.visualstudio.com/) -  A lightweight, flexible code editor recommended for writing and managing the project code.
- [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) - A Django template tag library used to customize form fields directly in templates.
- [Django Filter](https://pypi.org/project/django-filter/) - Adds filtering capabilities to Django views, making it easy to implement search and filter functionality.
- [Requests](https://pypi.org/project/requests/) - A simple and elegant HTTP library for Python, used to send HTTP/1.1 requests with methods like GET and POST. It simplifies interacting with external APIs.

### Installing

Create and initialize a virtual environment (optional)

    pip install virtualenv
    virtualenv job_env
    cd job_env
    Scripts\activate

Clone the Repository

    clone https://github.com/chidiohiri/django-job.git
    cd django-job

Move the project into the virtual environment, then install dependencies. The project dependencies can found in [requirements.txt](requirements.txt)

    pip install -r requirements.txt

Migrate all tables to the Sqlite3 DB

    python manage.py makemigrations
    python manage.py migrate

Create a super user. This account will be used to access the admin dashboard and verify objects.

    python manage.py createsuperuser

Run server on your terminal (cmd or powershell). Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

    python manage.py runserver

### Core Features

- Job Posting: Recruiters can easily create and manage job listings. Job posts are subject to wallet-based restrictions, ensuring only recruiters with sufficient balance can publish positions.

- Application Tracking: Recruiters can view and track applications for each job they post, with the ability to filter and manage applicants efficiently.

- Saved Jobs: Candidates can save job listings they are interested in, providing a convenient way to revisit opportunities later.

- Role-Based Access Control: The platform features role-based access, allowing recruiters to manage job posts and applications, while candidates can apply for jobs, save listings, and track their applications.

- Paystack Wallet Integration: Recruiters must maintain a minimum wallet balance to post jobs. Wallet integration handles the payment and balance management seamlessly.

- Advanced Filtering & Pagination: Both job listings and applications can be filtered using customizable filters, and pagination ensures a smooth user experience even with large data sets.

- Email Notifications: Candidates receive automatic email confirmations when their job applications are successfully submitted, keeping them informed about the process.

### Deployment

For production deployment, you will need to configure your application with a production-grade database (such as PostgreSQL), static file handling, and secure hosting. You may refer to the official [Django Documentation](https://docs.djangoproject.com/en/5.1/howto/deployment/) on deployment

### Authors

  - **Chidi Ohiri** - *For updates, networking, or feedback, feel free to connect:* -
    [Linkedin](https://www.linkedin.com/in/chidiebere-ohiri/)

### License

This project is licensed under the [MIT LICENSE](LICENSE.md), which permits reuse, modification, and distribution with proper attribution.

### Acknowledgments

  - Guido van Rossum, the creator of Python
  - The Django core team and community for building and maintaining such a robust framework
  - Developers and open-source contributors whose work inspired or supported the development of this project

