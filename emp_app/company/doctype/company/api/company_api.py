import emp_app.queries
import frappe, iam, emp_app
from iam.utils.validate.user import is_user_not_logged_in, is_user_logged_in


# old APIs

# @frappe.whitelist(allow_guest=True, methods=["GET"])
# def get_company_details(pk):
#     # get company details by id
#     if frappe.db.exists("Company", pk):
#         return frappe.db.get("Company", pk)
#     else:
#         return f"the name {pk} is not in database"


# @frappe.whitelist(allow_guest=True, methods=["GET"])
# def get_companys():
#     return frappe.get_list("Company")


# New APIs
@frappe.whitelist(allow_guest=True)
def get_companies():
    try:
        is_user_not_logged_in()

        companies = iam.db.get(**emp_app.queries.GET_COMPANIES)
    except Exception as error:
        iam.handle_api_exception(error)
    else:
        frappe.response.message = "Companies Retrieved Successfully"
        frappe.response.companies = companies
        frappe.response.count = len(companies)


@frappe.whitelist(allow_guest=True)
def get_company_details(id):
    try:
        is_user_not_logged_in()
        company = iam.db.get(company_id=id, **emp_app.queries.GET_COMPANIY_DETAILS)
    except Exception as error:
        iam.handle_api_exception(error)

    else:
        frappe.response.message = "Company Data Retrieved Successfully"
        frappe.response.company = company


# GET_COMPANIES = {
#     "doctype": "Company",
#     "select_fields": {"Company": [("name", "id"), ("company_name", "name")]},
#     "translatable_fields": ["name"],
# }


# def unpacking(**kwargs):
#     s = ""
#     for key, value in kwargs.items():
#         s += f"dict has key '{key}' and value is '{value}', "

#     s += "this is the end"
#     return s
