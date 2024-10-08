import frappe, iam, emp_app
import emp_app.queries as emp_queries
from iam.utils.validate.user import is_user_not_logged_in, is_user_logged_in


# Old APIs
# @frappe.whitelist(allow_guest=True, methods=["POST"])
# def get_department_details(pk):
#     # get department details by id
#     if frappe.db.exists("Department", pk):
#         return frappe.db.get("Department", pk)
#     else:
#         return f"the department {pk} is not in database"


# @frappe.whitelist(allow_guest=True, methods=["GET"])
# def get_department():
#     return frappe.get_list("Department", fields="*")


# New APIs
@frappe.whitelist(allow_guest=True, methods=["GET"])
def get_departments():
    try:
        is_user_not_logged_in()
        departments = iam.db.get(**emp_queries.GET_DEPARTMENTS)
    except Exception as e:
        iam.handle_api_exception(e)
    else:
        frappe.response.message = "Departments Retrieved Successfully"
        frappe.response.departments = departments
        frappe.response.count = len(departments)


@frappe.whitelist(allow_guest=True, methods=["GET"])
def get_department_details(id):
    try:
        is_user_not_logged_in()
        department = iam.db.get(department_id=id,**emp_queries.GET_DEPARTMENTS_DETAILS)
    except Exception as e:
        iam.handle_api_exception(e)
    else:
        frappe.response.message = "Department Retrieved Successfully"
        frappe.response.department = department
     
