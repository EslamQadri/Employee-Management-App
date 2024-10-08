########################### Companys Queries ######################################

GET_COMPANIES = {
    "doctype": "Company",
    "select_fields": {"Company": [("name", "id"), ("company_name", "name")]},
    "translatable_fields": ["name"],
}
GET_COMPANIY_DETAILS = {
    "doctype": "Company",
    "select_fields": {
        "Company": [
            ("name", "id"),
            ("company_name", "name"),
            ("number_of_department", "number_of_department"),
            ("number_of_employee", "number_of_employee"),
        ]
    },
    "conditions": {
        "company_id": {"doctype": "Company", "field": "name", "operator": "=="},
    },
}

########################### Departments Queries ######################################

GET_DEPARTMENTS = {
    "doctype": "Department",
    "select_fields": {
        "Department": [
            ("name", "id"),
            ("company", "company"),
            ("department_name", "department_name"),
        ]
    },
}

GET_DEPARTMENTS_DETAILS = {
    "doctype": "Department",
    "select_fields": {
        "Department": [
            ("name", "id"),
            ("company", "company"),
            ("department_name", "department_name"),
            ("number_of_employee", "number_of_employee"),
        ]
    },
    "conditions": {
        "department_id": {"doctype": "Department", "field": "name", "operator": "=="},
    },
}

########################### Employees Queries ######################################

GET_EMPLOYEES = {
    "doctype": "Employee DocType",
    "select_fields": {
        "Employee DocType": [
            ("name", "id"),
            ("employee_name", "name"),
            ("designation", "title"),
        ]
    },
}

GET_EMPLOYEES_DETAILS = {
    "doctype": "Employee DocType",
    "select_fields": {
        "Employee DocType": [
            ("name", "id"),
            ("company", "company_id"),
            ("department", "department_id"),
            ("employee_name", "name"),
            ("employee_status", "employee_status"),
            ("designation", "title"),
            ("email_address", "email_address"),
            ("mobile_number", "mobile_number"),
            ("address", "address"),
            ("hired_on", "hired_on"),
            # ("days_employed", "days_employed"),
            # don't return because it's a Virtual ?
            ("left_on", "left_on"),
        ],
        "Department": [("department_name", "department_name")],
        "Company": [("company_name", "company_name")],
    },
    "join_doctypes": {
        "Department": ("name", "Employee DocType", "department"),
        "Company": ("name", "Employee DocType", "company"),
    },
    "conditions": {
        "emp_id": {"doctype": "Employee DocType", "field": "name", "operator": "=="},
    },
}

CREATE_EMPLOYEE = {
    "expected_parameters": [
        "company",
        "department",
        "employee_name",
        "designation",
        "email_address",
        "mobile_number",
        "address",
    ],
    "required_parameters": [
        "company",
        "department",
        "employee_name",
        "designation",
        "email_address",
        "mobile_number",
    ],
}
UPDATE_EMPLOYEE = {
    "expected_parameters": [
        "employee_id",
        "company",
        "department",
        "employee_name",
        "designation",
        "email_address",
        "mobile_number",
        "address",
    ],
    "required_parameters": ["employee_id"],
}
DELETE_EMPLOYEE = {
    "expected_parameters": [
        "employee_id",
        "company",
        "department",
        "employee_name",
        "designation",
        "email_address",
        "mobile_number",
        "address",
    ],
    "required_parameters": ["employee_id"],
}

########################### Employees status ######################################
CHANGE_STATUS = {
    "expected_parameters": [
        "employee_id",
        "company",
        "department",
        "employee_name",
        "designation",
        "email_address",
        "mobile_number",
        "address",
        "employee_status",
        "action",
    ],
    "required_parameters": ["employee_id", "action"],
}
STATUS = {
    "available_status": [
        "Application Received",
        "Interview Scheduled",
        "Hired",
        "Not Accepted",
        "Left",
    ],
    "available_action": ["Approve", "Reject"],
}
