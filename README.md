# Employee Management App

## Description
develop an Frappe Employee Management App that encompasses various features for managing companies, departments, and employees. 
The system will allow users to create, read, update, and delete (CRUD) records for each of these entities

## Features

- Create, Read, Update, and Delete (CRUD) operations for companies and employees.
- RESTful API endpoints.
-  API Workflow for approve and reject Job Applicant and anthor actions 


## Prerequisites

- Python 3.12
- ERPNEXT 15
- Frappe 15 

  ## Installation

1. Clone the repository:

```
git clone https://github.com/EslamQadri/Employee-Management-App.git

```

2.install app in your site :
```
bench install-app emp_app
```


4. Migrate bench  :

```
bench migrate
```

## End Points 
### i set variable root to : http://127.0.0.1:8000/api/method/  
### Company 

- Get company list

*GET* : {{root}}emp_app.company.doctype.company.api.company_api.get_companies

- Create Company
  
*POST* : http://127.0.0.1:8000/api/resource/Company

- Get single Company

*GET* :{{root}}emp_app.company.doctype.company.api.company_api.get_company_details

# i add postman collection of all examples 
