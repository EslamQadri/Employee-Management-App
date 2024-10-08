import frappe
from frappe.exceptions import DoesNotExistError
from emp_app import queries as emp_queries
from frappe.model.workflow import (
    apply_workflow,
    WorkflowTransitionError,
    WorkflowStateError,
)
from iam.exceptions import InvalidWord


def insert_employee(emp_id=None, **data):
    if emp_id:
        emp = frappe.get_doc("Employee DocType", emp_id)

    else:
        emp = frappe.new_doc("Employee DocType")
    emp.update(data)
    emp.save()
    return emp


def validate_employee_is_exists(emp_id):
    if not frappe.db.exists("Employee DocType", emp_id):
        raise DoesNotExistError


def get_employee(emp_id):
    validate_employee_is_exists(emp_id)
    emp = frappe.get_doc("Employee DocType", emp_id)
    return emp


def delete_employee(emp_id):
    emp = get_employee(emp_id)
    emp.delete()


def is_status_word_is_allowed(word):
    if not word in emp_queries.STATUS.get("available_status"):
        raise InvalidWord


def is_action_word_is_allowed(word):
    if word not in emp_queries.STATUS.get("available_action"):
        raise InvalidWord()


def apply_action(emp_id, word):
    is_action_word_is_allowed(word)
    doc = get_employee(emp_id)
    apply_workflow(doc, action=word)
    return doc
