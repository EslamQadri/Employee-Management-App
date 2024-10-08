# Copyright (c) 2024, managing companies, departments, and employees. The system will allow users to create, read, update, and delete and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now, date_diff


class EmployeeDocType(Document):

    def before_validate(self):

        self.set_dates()

    def after_insert(self):
        self.update_company_and_department()

    def after_delete(self):
        self.update_company_and_department()

    def set_dates(self):

        if self.employee_status == "Hired" and not self.hired_on:
            self.hired_on = now()
        elif self.employee_status == "Left" and not self.left_on:
            self.left_on = now()

    def update_company_and_department(self):
        company = frappe.get_doc("Company", self.company).save()
        department = frappe.get_doc("Department", self.department).save()

    @property
    def days_employed(self):
        if (
            self.employee_status in ["Hired", "Left"] and self.hired_on
        ):  # self.hired_on assuming we have hire date

            if self.employee_status == "Hired":
                return date_diff(now(), self.hired_on)
            else:
                if self.left_on:
                    return date_diff(self.left_on, self.hired_on)
        return None

