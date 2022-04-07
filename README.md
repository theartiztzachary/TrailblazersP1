# Trailblazers Project 1 -- Reimbursement Application
## 

## Technologies Used
- Python
- PyCharm
- Pytest (Python Package)
- Flask (Python Package)
- Flask-CORS (Python Package)
- PsycoPG (Python Package)
- Selenium (Python Package)
- Behave (Python Package)
- Gherkin (PyCharm PlugIn)
- Cucumber (PyCharm PlugIn)
- Git
- GitHub
- AWS RDS
- AWS EC2
- DBeaver
- Postgres
- Postman
- Chrome Web Driver

## Features
- Employees can log into the system.
- Employees can view their previous reimbursement requests.
- Employees can submit reimbursement requests.
- Employees can cancel pending reimbursement requests.
- Employees can log out of the system.

## Getting Started
- To Clone:
  - git clone https://github.com/theartiztzachary/TrailblazersP1.git
- Database:
  - Create a local or cloud based Postgres RDS
  - Use your preferred database management software to set up the database.
- To Deploy:
  - Install the necessary Python packages, preferably in a virtual environment.
  - Set up a runtime configuration with environmental variables for database access for main.py.
  - Run main.py using said runtime configuration to start the server. Currently, there is no in-app way to end the application.

## Usage
- Employees can log into the reimbursement portal to manage their reimbursement requests:
  - Employees can view their complete reimbursement history, including approved and pending totals. 
  - Employees can make reimbursement requests, giving an amount, selecting a reason, and typing out a comment.
  - Employees can cancel pending reimbursements in case there was an error that needs to be fixed.