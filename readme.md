# Task
Create a Restful API for Registration, Login & getUserList, along with an authentication system to secure the getUserList endpoint.

# Tech Stack
 - Programming Language: Python
 - Backend Framework: Django
 - Authenticaton Protocol: JSON Web Tokens (JWT)
 - Frontend Technologies: Twitter Bootstrap, HTML, CSS, JQuery
 - Database: SQLite3

# File Structure
 - requirements.txt: contains the Python packages used
 - antarctica_project: this folder contains the entire project's configurations
 - user_auth: this folder contains the core business logic of the registration, login, logout,       UserList and the authentication flows
 - user_auth/templates: contains the HTML files
 - user_auth/static: contains the CSS and JavaScript files along with images used in the application
 - models.py: this file contains the schema of the database table that stores employee details

 # Database Schema
The project contains the following database tables to store the user data
 - auth_user: an inbuilt django model that stores the user information; used to maintain sessions
 - Employee: stores the employee details like user_id, first_name, last_name, email, employee_id, organisation, created_at. This is used to display the userList table.

# API Endpoints
The following are the API endpoints:
 - login/ -  to login a registered user with a username and password
 - logout/ -  logout a user
 - dashboard/ - it provides a form that captures the employee details from the user
 - registration/ -  to register a new user based on a unique email id and password
 - userlist/ -  a list of all the users displayed to the authenticated person

# Flows
 - Session Management
    - The session management flows provides the users the functionalities to register, login and  logout in the application.
    ![alt text](https://github.com/ZainebPenwala/user_management_system/blob/main/images/image%20(44).png)

