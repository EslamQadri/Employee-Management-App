import frappe, iam, emp_app
import emp_app.queries as emp_queries
from iam.utils.validate.user import is_user_not_logged_in, is_user_logged_in
from iam.utils.validate.api import validate_required_parameters
from emp_app.employee.doctype.employee_doctype.api.utils import (
    insert_employee,
    validate_employee_is_exists,
    delete_employee,
    apply_action,
)
from frappe import _

# emp_app/emp_app/employee/doctype/employee_doctype/api/api.py


# @frappe.whitelist(allow_guest=True, methods={"GET"})
# def get_list_of_employee():
#     return frappe.get_list("Employee DocType")


# @frappe.whitelist(allow_guest=True, methods={"POST"})
# def get_employee_details(pk):
#     if frappe.db.exists("Employee DocType", pk):
#         return frappe.db.get("Employee DocType", pk)
#     else:
#         return f" The Employee ID is not Exist"
frappe.qb.DocType


# def returned_message(success: bool, message: str, data: None):
#     return {
#         "success": success,
#         "message": _(message),
#         "data": data,
#     }


# @frappe.whitelist(allow_guest=True, methods=["GET"])
# def get_employee_details_or_list_of_employee(pk=None):
#     if pk:
#         if frappe.db.exists("Employee DocType", pk):

#             return returned_message(
#                 True,
#                 "successfully Get",
#                 frappe.db.get_value(
#                     "Employee DocType",
#                     pk,
#                     ["department", "department.department_name", "company"],
#                     as_dict=True,
#                 ),
#             )

#         else:

#             frappe.response.update(
#                 returned_message(False, " The Employee ID is not Exist", "no data")
#             )
#     else:
#         frappe.response.update(
#             returned_message(
#                 True,
#                 "successfully Get",
#                 frappe.get_list(
#                     "Employee DocType",
#                     fields="employee_name, department.department_name as department, company, company.number_of_department as sdf",
#                 ),
#             )
#         )


@frappe.whitelist(allow_guest=True, methods=["GET"])
def get_list_of_employee():
    try:
        is_user_not_logged_in()
        employees = iam.db.get(**emp_queries.GET_EMPLOYEES)
    except Exception as e:
        iam.handle_api_exception(e)
    else:
        frappe.response.message = "Employees Retrieved Successfully"
        frappe.response.employees = employees
        frappe.response.count = len(employees)


@frappe.whitelist(allow_guest=True, methods=["GET"])
def get_employee_details(id):
    try:
        is_user_not_logged_in()
        employee = iam.db.get(emp_id=id, **emp_queries.GET_EMPLOYEES_DETAILS)
    except Exception as e:
        iam.handle_api_exception(e)
    else:
        frappe.response.message = "Employee Retrieved Successfully"
        frappe.response.employee = employee


@frappe.whitelist(allow_guest=True, methods=["POST"])
def create_employee(**parameters):
    try:
        is_user_not_logged_in()
        expected_parameters = emp_queries.CREATE_EMPLOYEE.get("expected_parameters")
        required_parameters = emp_queries.CREATE_EMPLOYEE.get("required_parameters")
        parameters = iam.db.prepare_query_parameters(expected_parameters, parameters)
        validate_required_parameters(parameters, required_parameters)
        employee = insert_employee(**parameters)
    except Exception as e:

        iam.handle_api_exception(e)

    else:
        frappe.response.message = "Employee Createrd Successfully"
        frappe.response.employee = employee


# @frappe.whitelist(allow_guest=True, methods=["POST"])
# def create_employee(
#     company=None,
#     department=None,
#     employee_name=None,
#     designation=None,
#     email_address=None,
#     mobile_number=None,
#     address=None,
# ):  #  in the first step Employee Status is = Application Received
#     required_params = {
#         "company": company,
#         "department": department,
#         "employee_name": employee_name,
#         "designation": designation,
#         "email_address": email_address,
#         "mobile_number": mobile_number,
#     }
#     missing_params = [param for param, value in required_params.items() if not value]

#     if missing_params:
#         # If there are missing parameters, return an error response
#         frappe.local.response["http_status_code"] = 400

#         return returned_message(False, "Missing required parameters", missing_params)

#     try:
#         new_emp = frappe.get_doc(
#             {
#                 "doctype": "Employee DocType",
#                 "company": company,
#                 "department": department,
#                 "employee_name": employee_name,
#                 "email_address": email_address,
#                 "mobile_number": mobile_number,
#                 "designation": designation,
#                 "address": address,
#             }
#         )
#         new_emp.save()
#         frappe.local.response["http_status_code"] = 201
#         return returned_message(True, "Employee created successfully", new_emp)

#     except frappe.exceptions.ValidationError as e:
#         frappe.local.response["http_status_code"] = 400
#         return returned_message(False, "Validation Error in creating Employee", str(e))

#     except Exception as e:
#         frappe.local.response["http_status_code"] = 500

#         return returned_message(False, "You are make An unexpected error ", str(e))


@frappe.whitelist(allow_guest=True, methods=["PUT"])
def update_employee_information(**parameters):
    try:
        is_user_not_logged_in()

        expected_parameters = emp_queries.UPDATE_EMPLOYEE.get("expected_parameters")
        required_parameters = emp_queries.UPDATE_EMPLOYEE.get("required_parameters")
        parameters = iam.db.prepare_query_parameters(expected_parameters, parameters)

        validate_required_parameters(parameters, required_parameters)

        emp_id = parameters.get("employee_id")

        validate_employee_is_exists(emp_id)
        emp = insert_employee(emp_id=emp_id, **parameters)
    except Exception as error:
        iam.handle_api_exception(error)
    else:
        frappe.response.emp = emp
        frappe.response.message = " Employee Updated Successfully"


# @frappe.whitelist(allow_guest=True, methods=["PUT"])
# def update_employee_information(pk, **kwargs):
#     if frappe.db.exists("Employee DocType", pk):
#         try:

#             emp = frappe.get_doc("Employee DocType", pk)
#             valid_fields = {field.fieldname for field in emp.meta.fields}

#             valid_kwargs = {k: v for k, v in kwargs.items() if k in valid_fields}
#             invalid_fields = [k for k in kwargs.keys() if k not in valid_fields]
#             invalid_fields.remove("cmd")
#             if invalid_fields:
#                 frappe.local.response["http_status_code"] = 400
#                 return returned_message(
#                     False,
#                     "Validation Error in Upading Employee",
#                     f"You add invalid fields {invalid_fields }",
#                 )

#             emp.update(valid_kwargs)
#             emp.save()
#             return returned_message(
#                 True,
#                 "Employee successfully Updated ",
#                 emp,
#             )

#         except frappe.exceptions.ValidationError as e:
#             frappe.local.response["http_status_code"] = 400
#             return returned_message(
#                 False, "Validation Error in creating Employee", str(e)
#             )

#         except Exception as e:
#             frappe.local.response["http_status_code"] = 500
#         return returned_message(False, "You are make An unexpected error ", str(e))

#     else:
#         return returned_message(False, " The Employee ID is not Exist", "no data")


@frappe.whitelist(allow_guest=True, methods=["DELETE"])
def delete_employee_api(**parameters):
    try:
        is_user_not_logged_in()

        expected_parameters = emp_queries.DELETE_EMPLOYEE.get("expected_parameters")
        required_parameters = emp_queries.DELETE_EMPLOYEE.get("required_parameters")
        parameters = iam.db.prepare_query_parameters(expected_parameters, parameters)

        validate_required_parameters(parameters, required_parameters)

        emp_id = parameters.get("employee_id")
        delete_employee(emp_id)
    except Exception as error:
        iam.handle_api_exception(error)
    else:
        frappe.response.message = " Employee Deleted Successfully"


# @frappe.whitelist(allow_guest=True, methods=["DELETE"])
# def delete_employee(pk):
#     if frappe.db.exists("Employee DocType", pk):
#         try:
#             emp = frappe.get_doc("Employee DocType", pk)
#             emp.delete()
#             return returned_message(True, "Employee Deleted successfully", emp)
#         except frappe.exceptions.ValidationError as e:
#             frappe.local.response["http_status_code"] = 400
#             return returned_message(
#                 False, "Validation Error in updating Employee", str(e)
#             )
#         except Exception as e:
#             frappe.local.response["http_status_code"] = 500

#             return returned_message(False, "You are make An unexpected error ", str(e))

#     else:
#         return returned_message(False, " The Employee ID is not Exist", "no data")


# emp_app.employee.doctype.employee_doctype.api.api.
@frappe.whitelist(allow_guest=True, methods=["POST", "PUT"])
def update_employee_status(**parameters):
    try:
        is_user_not_logged_in()

        expected_parameters = emp_queries.CHANGE_STATUS.get("expected_parameters")
        required_parameters = emp_queries.CHANGE_STATUS.get("required_parameters")
        parameters = iam.db.prepare_query_parameters(expected_parameters, parameters)

        validate_required_parameters(parameters, required_parameters)

        emp_id = parameters.get("employee_id")
        action = parameters.get("action")
        emp = apply_action(emp_id, action)
    except Exception as error:

        iam.handle_api_exception(error)
    else:
        frappe.response.message = (
            f" Employee status Successfully to {emp.employee_status}"
        )
        frappe.response.employee = emp


# idea : make one api that take from employee_status and handel the next
# @frappe.whitelist(allow_guest=True, methods=["POST"])
# def update_employee_status_from_application_received(emp_id, response: bool):
#     try:
#         if frappe.db.exists("Employee DocType", emp_id):
#             emp = frappe.get_doc("Employee DocType", emp_id)
#             if response:
#                 emp.employee_status = "Interview Scheduled"
#                 emp.save()
#                 return returned_message(True, "Employee updating successfully", emp)

#             else:
#                 emp.employee_status = "Not Accepted"
#                 emp.save()
#                 return returned_message(True, "Employee updating successfully", emp)

#         else:
#             return returned_message(False, "The Employee ID is not Exist", "no data")

#     except frappe.exceptions.ValidationError as e:
#         frappe.local.response["http_status_code"] = 400
#         return returned_message(False, "Validation Error in creating Employee", str(e))

#     except Exception as e:
#         frappe.local.response["http_status_code"] = 500

#         return returned_message(False, "You are make An unexpected error ", str(e))


# @frappe.whitelist(allow_guest=True, methods=["POST"])
# def update_employee_status_from_interview_scheduled(emp_id, response: bool):
#     try:
#         if frappe.db.exists("Employee DocType", emp_id):
#             emp = frappe.get_doc("Employee DocType", emp_id)
#             if response:
#                 emp.employee_status = "Hired"
#                 emp.save()
#                 return returned_message(True, "Employee updating successfully", emp)

#             else:
#                 emp.employee_status = "Not Accepted"
#                 emp.save()
#                 return returned_message(True, "Employee updating successfully", emp)
#         else:
#             return returned_message(False, " The Employee ID is not Exist", "no data")

#     except frappe.exceptions.ValidationError as e:
#         frappe.local.response["http_status_code"] = 400
#         return returned_message(False, "Validation Error in updating Employee", str(e))
#     except Exception as e:
#         frappe.local.response["http_status_code"] = 500

#         return returned_message(False, "You are make An unexpected error ", str(e))
