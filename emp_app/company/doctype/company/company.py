# Copyright (c) 2024, managing companies, departments, and employees. The system will allow users to create, read, update, and delete and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Company(Document):

    def before_save(self):
        self.number_of_department = frappe.db.count("Department", {"company": self.name})
        self.number_of_employee = frappe.db.count("Employee DocType", {"company": self.name})
        
