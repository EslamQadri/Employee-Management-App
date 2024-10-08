# Copyright (c) 2024, managing companies, departments, and employees. The system will allow users to create, read, update, and delete and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Department(Document):
    def before_save(self):
        self.number_of_employee = frappe.db.count(
            "Employee DocType", {"department": self.name}
        )

    def after_insert(self):
        company = frappe.get_doc("Company", self.company).save()

    def after_delete(self):
        company = frappe.get_doc("Company", self.company).save()
