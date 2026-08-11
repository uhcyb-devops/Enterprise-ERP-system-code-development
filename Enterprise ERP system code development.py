# ==========================================================
#               Enterprise ERP Management System
# ==========================================================
# Developed by: Muhammad Shahzaib

# ==========================================================

import os
import json
import time
import platform
from datetime import datetime


# ==========================
# JSON FILES
# ==========================

DATA_DIR = "data"

USERS_FILE = os.path.join(DATA_DIR, "users.json")
PRODUCTS_FILE = os.path.join(DATA_DIR, "products.json")
SUPPLIERS_FILE = os.path.join(DATA_DIR, "suppliers.json")
EMPLOYEES_FILE = os.path.join(DATA_DIR, "employees.json")
SALES_FILE = os.path.join(DATA_DIR, "sales.json")
PURCHASES_FILE = os.path.join(DATA_DIR, "purchases.json")
PAYROLL_FILE = os.path.join(DATA_DIR, "payroll.json")


# ==========================
# GLOBAL DATA
# ==========================

users = []
products = []
suppliers = []
employees = []
sales = []
purchases = []
payroll = []


# ==========================
# UTILITY FUNCTIONS
# ==========================

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")


def welcome_screen():
    clear_screen()

    print("===============================================================")
    print("                ENTERPRISE ERP MANAGEMENT SYSTEM")
    print("================================================================")
    print("            Smart Business Management Solution")
    print("================================================================")
    print("               Developed by Muhammad Shahzaib")
    print("================================================================")

    input("\nPress Enter to Continue...")


def loading_screen():
    clear_screen()

    print("=================================================================")
    print("                ENTERPRISE ERP MANAGEMENT SYSTEM")
    print("=================================================================")

    print("\nLoading System", end="")

    for _ in range(6):
        print(".", end="", flush=True)
        time.sleep(0.3)

    print("\n\nSystem Loaded Successfully!")
    time.sleep(1)


def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def next_id(data_list, key, prefix):

    if not data_list:
        return f"{prefix}001"

    numbers = []
    for item in data_list:
        raw = item.get(key, "")
        digits = "".join(ch for ch in raw if ch.isdigit())
        if digits:
            numbers.append(int(digits))

    next_num = max(numbers) + 1 if numbers else 1
    return f"{prefix}{next_num:03d}"


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number! Please try again.")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number! Please try again.")


def initialize_data():
    global users, products, suppliers, employees, sales, purchases, payroll

    os.makedirs(DATA_DIR, exist_ok=True)

    users = load_data(USERS_FILE)
    products = load_data(PRODUCTS_FILE)
    suppliers = load_data(SUPPLIERS_FILE)
    employees = load_data(EMPLOYEES_FILE)
    sales = load_data(SALES_FILE)
    purchases = load_data(PURCHASES_FILE)
    payroll = load_data(PAYROLL_FILE)

    # If no users exist yet, create a default admin account so the
    # system is usable on first run.
    if not users:
        users = [{
            "username": "admin",
            "password": "admin123",
            "role": "Administrator"
        }]
        save_data(USERS_FILE, users)


# ==========================
# AUTHENTICATION
# ==========================

def login():
    clear_screen()

    print("=====================================================================")
    print("                          LOGIN")
    print("=====================================================================")

    username = input("Username : ")
    password = input("Password : ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("\nLogin Successful...")
            time.sleep(1)
            return True

    print("\nInvalid Username or Password!")
    time.sleep(1.5)

    return False


def change_password():
    clear_screen()

    print("==================================================")
    print("                     CHANGE PASSWORD")
    print("===================================================")

    username = input("Username        : ")
    old_password = input("Current Password: ")

    for user in users:
        if user["username"] == username and user["password"] == old_password:
            new_password = input("New Password     : ")
            confirm_password = input("Confirm Password : ")

            if new_password != confirm_password:
                print("\nPasswords do not match!")
                input("\nPress Enter to Continue...")
                return

            user["password"] = new_password
            save_data(USERS_FILE, users)

            print("\nPassword Changed Successfully!")
            input("\nPress Enter to Continue...")
            return

    print("\nInvalid Username or Current Password!")
    input("\nPress Enter to Continue...")


# ==========================
# DASHBOARD
# ==========================

def dashboard():
    while True:
        clear_screen()

        print("=======================================================")
        print("                 ENTERPRISE ERP SYSTEM")
        print("=======================================================")
        print("                     ADMIN DASHBOARD")
        print("=======================================================")

        print("""
1. Inventory Management
2. Sales Management
3. Purchase Management
4. HR Management
5. Payroll Management
6. Reports
7. Change Password
8. Logout
9. Exit
""")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            inventory_management()

        elif choice == "2":
            sales_management()

        elif choice == "3":
            purchase_management()

        elif choice == "4":
            hr_management()

        elif choice == "5":
            payroll_management()

        elif choice == "6":
            reports_menu()

        elif choice == "7":
            change_password()

        elif choice == "8":
            print("\nLogging Out...")
            time.sleep(1)
            break

        elif choice == "9":
            print("\nThank You For Using Enterprise ERP System.")
            exit()

        else:
            print("\nInvalid Choice!")
            time.sleep(1.5)


# ==========================
# PRODUCT CLASS
# ==========================

class Product:

    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }


# ==========================
# INVENTORY MANAGEMENT
# ==========================

def inventory_management():
    while True:
        clear_screen()

        print("=" * 70)
        print("               INVENTORY MANAGEMENT")
        print("=" * 70)

        print("""
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Back
""")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            break

        else:
            print("\nInvalid Choice!")
            time.sleep(1)


def add_product():
    clear_screen()

    print("=====================================================================")
    print("                     ADD PRODUCT")
    print("=====================================================================")

    product_id = input("Product ID (leave blank to auto-generate): ").strip()

    if not product_id:
        product_id = next_id(products, "product_id", "P")
        print(f"Generated Product ID: {product_id}")

    for product in products:
        if product["product_id"] == product_id:
            print("\nProduct ID already exists!")
            input("\nPress Enter to Continue...")
            return

    name = input("Product Name    : ")
    category = input("Category        : ")
    price = get_float_input("Price           : ")
    quantity = get_int_input("Quantity        : ")

    new_product = Product(product_id, name, category, price, quantity)

    products.append(new_product.to_dict())
    save_data(PRODUCTS_FILE, products)

    print("\nProduct Added Successfully!")
    input("\nPress Enter to Continue...")


def view_products():
    clear_screen()

    print("=========================================================")
    print("                   PRODUCT LIST")
    print("=========================================================")

    if len(products) == 0:
        print("\nNo Products Found.")

    else:
        for product in products:
            print(f"""
Product ID : {product["product_id"]}
Name       : {product["name"]}
Category   : {product["category"]}
Price      : {product["price"]}
Quantity   : {product["quantity"]}
------------------------------------------------------------""")

    input("\nPress Enter to Continue...")


def search_product():
    clear_screen()

    pid = input("Enter Product ID : ")

    for product in products:
        if product["product_id"] == pid:
            print(f"""
Product Found

Product ID : {product["product_id"]}
Name       : {product["name"]}
Category   : {product["category"]}
Price      : {product["price"]}
Quantity   : {product["quantity"]}
""")
            input("\nPress Enter...")
            return

    print("\nProduct Not Found.")
    input("\nPress Enter...")


def update_product():
    clear_screen()

    print("========================================================")
    print("                   UPDATE PRODUCT")
    print("=========================================================")

    pid = input("Enter Product ID to Update : ")

    for product in products:
        if product["product_id"] == pid:

            print("\nLeave a field blank to keep its current value.\n")

            name = input(f"Name [{product['name']}]         : ").strip()
            category = input(f"Category [{product['category']}]     : ").strip()
            price = input(f"Price [{product['price']}]        : ").strip()
            quantity = input(f"Quantity [{product['quantity']}]     : ").strip()

            if name:
                product["name"] = name
            if category:
                product["category"] = category
            if price:
                try:
                    product["price"] = float(price)
                except ValueError:
                    print("\nInvalid price, keeping old value.")
            if quantity:
                try:
                    product["quantity"] = int(quantity)
                except ValueError:
                    print("\nInvalid quantity, keeping old value.")

            save_data(PRODUCTS_FILE, products)

            print("\nProduct Updated Successfully!")
            input("\nPress Enter...")
            return

    print("\nProduct Not Found.")
    input("\nPress Enter...")


def delete_product():
    clear_screen()

    print("======================================================")
    print("                   DELETE PRODUCT")
    print("======================================================")

    product_id = input("Enter Product ID : ")

    for product in products:
        if product["product_id"] == product_id:

            confirm = input("Are you sure? (Y/N) : ").upper()

            if confirm == "Y":
                products.remove(product)
                save_data(PRODUCTS_FILE, products)
                print("\nProduct Deleted Successfully!")
            else:
                print("\nDelete Cancelled.")

            input("\nPress Enter...")
            return

    print("\nProduct Not Found.")
    input("\nPress Enter...")


# ==========================
# SALES MANAGEMENT
# ==========================

def sales_management():
    while True:
        clear_screen()

        print("====================================================")
        print("                 SALES MANAGEMENT")
        print("=====================================================")

        print("""
1. New Sale
2. View Sales
3. Search Sale
4. Back
""")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            new_sale()

        elif choice == "2":
            view_sales()

        elif choice == "3":
            search_sale()

        elif choice == "4":
            break

        else:
            print("\nInvalid Choice!")
            time.sleep(1)


def new_sale():
    clear_screen()

    print("============================================================")
    print("                       NEW SALE")
    print("============================================================")

    if not products:
        print("\nNo Products Available. Please add products first.")
        input("\nPress Enter...")
        return

    product_id = input("Enter Product ID : ")

    product = None
    for p in products:
        if p["product_id"] == product_id:
            product = p
            break

    if not product:
        print("\nProduct Not Found.")
        input("\nPress Enter...")
        return

    print(f"\nProduct: {product['name']}  |  Available Stock: {product['quantity']}  |  Price: {product['price']}")

    quantity = get_int_input("Enter Quantity to Sell : ")

    if quantity <= 0:
        print("\nQuantity must be greater than zero.")
        input("\nPress Enter...")
        return

    if quantity > product["quantity"]:
        print("\nInsufficient Stock Available!")
        input("\nPress Enter...")
        return

    total_price = quantity * product["price"]

    sale_id = next_id(sales, "sale_id", "S")

    sale_record = {
        "sale_id": sale_id,
        "product_id": product["product_id"],
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "total_price": total_price,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    sales.append(sale_record)
    save_data(SALES_FILE, sales)

    # Reduce stock
    product["quantity"] -= quantity
    save_data(PRODUCTS_FILE, products)

    print(f"\nSale Recorded Successfully! Sale ID: {sale_id}  |  Total: {total_price}")
    input("\nPress Enter...")


def view_sales():
    clear_screen()

    print("==========================================================")
    print("                      SALES LIST")
    print("===========================================================")

    if not sales:
        print("\nNo Sales Found.")
    else:
        total_revenue = 0
        for sale in sales:
            print(f"""
Sale ID    : {sale["sale_id"]}
Product    : {sale["product_name"]} ({sale["product_id"]})
Quantity   : {sale["quantity"]}
Unit Price : {sale["unit_price"]}
Total      : {sale["total_price"]}
Date       : {sale["date"]}
------------------------------------------------------------""")
            total_revenue += sale["total_price"]

        print(f"\nTotal Revenue: {total_revenue}")

    input("\nPress Enter to Continue...")


def search_sale():
    clear_screen()

    sid = input("Enter Sale ID : ")

    for sale in sales:
        if sale["sale_id"] == sid:
            print(f"""
Sale Found

Sale ID    : {sale["sale_id"]}
Product    : {sale["product_name"]} ({sale["product_id"]})
Quantity   : {sale["quantity"]}
Unit Price : {sale["unit_price"]}
Total      : {sale["total_price"]}
Date       : {sale["date"]}
""")
            input("\nPress Enter...")
            return

    print("\nSale Not Found.")
    input("\nPress Enter...")


# ==========================
# PURCHASE MANAGEMENT
# ==========================

def purchase_management():
    while True:
        clear_screen()

        print("======================================================")
        print("               PURCHASE MANAGEMENT")
        print("=======================================================")

        print("""
1. Add Supplier
2. View Suppliers
3. New Purchase
4. View Purchases
5. Back
""")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            add_supplier()

        elif choice == "2":
            view_suppliers()

        elif choice == "3":
            new_purchase()

        elif choice == "4":
            view_purchases()

        elif choice == "5":
            break

        else:
            print("\nInvalid Choice!")
            time.sleep(1)


def add_supplier():
    clear_screen()

    print("===============================================================")
    print("                    ADD SUPPLIER")
    print("===============================================================")

    supplier_id = next_id(suppliers, "supplier_id", "SUP")

    name = input("Supplier Name : ")
    contact = input("Contact No.   : ")
    address = input("Address       : ")

    suppliers.append({
        "supplier_id": supplier_id,
        "name": name,
        "contact": contact,
        "address": address
    })

    save_data(SUPPLIERS_FILE, suppliers)

    print(f"\nSupplier Added Successfully! Supplier ID: {supplier_id}")
    input("\nPress Enter...")


def view_suppliers():
    clear_screen()

    print("=============================================================")
    print("                   SUPPLIER LIST")
    print("=============================================================")

    if not suppliers:
        print("\nNo Suppliers Found.")
    else:
        for s in suppliers:
            print(f"""
Supplier ID : {s["supplier_id"]}
Name        : {s["name"]}
Contact     : {s["contact"]}
Address     : {s["address"]}
------------------------------------------------------------""")

    input("\nPress Enter to Continue...")


def new_purchase():
    clear_screen()

    print("============================================================")
    print("                     NEW PURCHASE")
    print("============================================================")

    if not suppliers:
        print("\nNo Suppliers Found. Please add a supplier first.")
        input("\nPress Enter...")
        return

    supplier_id = input("Enter Supplier ID : ")

    supplier = None
    for s in suppliers:
        if s["supplier_id"] == supplier_id:
            supplier = s
            break

    if not supplier:
        print("\nSupplier Not Found.")
        input("\nPress Enter...")
        return

    product_id = input("Enter Product ID (existing or new) : ")

    product = None
    for p in products:
        if p["product_id"] == product_id:
            product = p
            break

    quantity = get_int_input("Enter Quantity Purchased : ")
    unit_price = get_float_input("Enter Unit Purchase Price : ")
    total_price = quantity * unit_price

    if product:
        # Existing product: increase stock
        product["quantity"] += quantity
        product_name = product["name"]
    else:
        # New product: create it
        name = input("New Product Name     : ")
        category = input("New Product Category : ")

        new_prod = Product(product_id, name, category, unit_price, quantity)
        products.append(new_prod.to_dict())
        product_name = name

    save_data(PRODUCTS_FILE, products)

    purchase_id = next_id(purchases, "purchase_id", "PUR")

    purchase_record = {
        "purchase_id": purchase_id,
        "supplier_id": supplier_id,
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_price": total_price,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    purchases.append(purchase_record)
    save_data(PURCHASES_FILE, purchases)

    print(f"\nPurchase Recorded Successfully! Purchase ID: {purchase_id}  |  Total: {total_price}")
    input("\nPress Enter...")


def view_purchases():
    clear_screen()

    print("============================================================")
    print("                    PURCHASE LIST")
    print("============================================================")

    if not purchases:
        print("\nNo Purchases Found.")
    else:
        total_spent = 0
        for pur in purchases:
            print(f"""
Purchase ID : {pur["purchase_id"]}
Supplier ID : {pur["supplier_id"]}
Product     : {pur["product_name"]} ({pur["product_id"]})
Quantity    : {pur["quantity"]}
Unit Price  : {pur["unit_price"]}
Total       : {pur["total_price"]}
Date        : {pur["date"]}
------------------------------------------------------------""")
            total_spent += pur["total_price"]

        print(f"\nTotal Spent: {total_spent}")

    input("\nPress Enter to Continue...")


# ==========================
# HR MANAGEMENT
# ==========================

def hr_management():
    while True:
        clear_screen()

        print("============================================================")
        print("                  HR MANAGEMENT")
        print("============================================================")

        print("""
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Back
""")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            break

        else:
            print("\nInvalid Choice!")
            time.sleep(1)


def add_employee():
    clear_screen()

    print("============================================================")
    print("                    ADD EMPLOYEE")
    print("============================================================")

    emp_id = next_id(employees, "emp_id", "E")

    name = input("Employee Name : ")
    designation = input("Designation   : ")
    salary = get_float_input("Basic Salary  : ")
    contact = input("Contact No.   : ")

    employees.append({
        "emp_id": emp_id,
        "name": name,
        "designation": designation,
        "salary": salary,
        "contact": contact
    })

    save_data(EMPLOYEES_FILE, employees)

    print(f"\nEmployee Added Successfully! Employee ID: {emp_id}")
    input("\nPress Enter...")


def view_employees():
    clear_screen()

    print("============================================================")
    print("                   EMPLOYEE LIST")
    print("============================================================")

    if not employees:
        print("\nNo Employees Found.")
    else:
        for e in employees:
            print(f"""
Employee ID : {e["emp_id"]}
Name        : {e["name"]}
Designation : {e["designation"]}
Salary      : {e["salary"]}
Contact     : {e["contact"]}
------------------------------------------------------------""")

    input("\nPress Enter to Continue...")


def search_employee():
    clear_screen()

    eid = input("Enter Employee ID : ")

    for e in employees:
        if e["emp_id"] == eid:
            print(f"""
Employee Found

Employee ID : {e["emp_id"]}
Name        : {e["name"]}
Designation : {e["designation"]}
Salary      : {e["salary"]}
Contact     : {e["contact"]}
""")
            input("\nPress Enter...")
            return

    print("\nEmployee Not Found.")
    input("\nPress Enter...")


def update_employee():
    clear_screen()

    print("============================================================")
    print("                   UPDATE EMPLOYEE")
    print("============================================================")

    eid = input("Enter Employee ID to Update : ")

    for e in employees:
        if e["emp_id"] == eid:

            print("\nLeave a field blank to keep its current value.\n")

            name = input(f"Name [{e['name']}]               : ").strip()
            designation = input(f"Designation [{e['designation']}]   : ").strip()
            salary = input(f"Salary [{e['salary']}]              : ").strip()
            contact = input(f"Contact [{e['contact']}]            : ").strip()

            if name:
                e["name"] = name
            if designation:
                e["designation"] = designation
            if salary:
                try:
                    e["salary"] = float(salary)
                except ValueError:
                    print("\nInvalid salary, keeping old value.")
            if contact:
                e["contact"] = contact

            save_data(EMPLOYEES_FILE, employees)

            print("\nEmployee Updated Successfully!")
            input("\nPress Enter...")
            return

    print("\nEmployee Not Found.")
    input("\nPress Enter...")


def delete_employee():
    clear_screen()

    print("============================================================")
    print("                   DELETE EMPLOYEE")
    print("============================================================")

    eid = input("Enter Employee ID : ")

    for e in employees:
        if e["emp_id"] == eid:

            confirm = input("Are you sure? (Y/N) : ").upper()

            if confirm == "Y":
                employees.remove(e)
                save_data(EMPLOYEES_FILE, employees)
                print("\nEmployee Deleted Successfully!")
            else:
                print("\nDelete Cancelled.")

            input("\nPress Enter...")
            return

    print("\nEmployee Not Found.")
    input("\nPress Enter...")


# ==========================
# PAYROLL MANAGEMENT
# ==========================

def payroll_management():
    while True:
        clear_screen()

        print("============================================================")
        print("                PAYROLL MANAGEMENT")
        print("============================================================")

        print("""
1. Generate Payroll
2. View Payroll Records
3. Search Payroll Record
4. Back
""")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            generate_payroll()

        elif choice == "2":
            view_payroll()

        elif choice == "3":
            search_payroll()

        elif choice == "4":
            break

        else:
            print("\nInvalid Choice!")
            time.sleep(1)


def generate_payroll():
    clear_screen()

    print("============================================================")
    print("                  GENERATE PAYROLL")
    print("============================================================")

    if not employees:
        print("\nNo Employees Found. Please add employees first.")
        input("\nPress Enter...")
        return

    emp_id = input("Enter Employee ID : ")

    employee = None
    for e in employees:
        if e["emp_id"] == emp_id:
            employee = e
            break

    if not employee:
        print("\nEmployee Not Found.")
        input("\nPress Enter...")
        return

    print(f"\nEmployee: {employee['name']}  |  Basic Salary: {employee['salary']}")

    bonus = get_float_input("Enter Bonus (0 if none)      : ")
    deduction = get_float_input("Enter Deduction (0 if none)  : ")

    net_salary = employee["salary"] + bonus - deduction

    payroll_id = next_id(payroll, "payroll_id", "PAY")

    payroll_record = {
        "payroll_id": payroll_id,
        "emp_id": emp_id,
        "emp_name": employee["name"],
        "basic_salary": employee["salary"],
        "bonus": bonus,
        "deduction": deduction,
        "net_salary": net_salary,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    payroll.append(payroll_record)
    save_data(PAYROLL_FILE, payroll)

    print(f"\nPayroll Generated Successfully! Payroll ID: {payroll_id}  |  Net Salary: {net_salary}")
    input("\nPress Enter...")


def view_payroll():
    clear_screen()

    print("============================================================")
    print("                   PAYROLL RECORDS")
    print("============================================================")

    if not payroll:
        print("\nNo Payroll Records Found.")
    else:
        for p in payroll:
            print(f"""
Payroll ID   : {p["payroll_id"]}
Employee     : {p["emp_name"]} ({p["emp_id"]})
Basic Salary : {p["basic_salary"]}
Bonus        : {p["bonus"]}
Deduction    : {p["deduction"]}
Net Salary   : {p["net_salary"]}
Date         : {p["date"]}
------------------------------------------------------------""")

    input("\nPress Enter to Continue...")


def search_payroll():
    clear_screen()

    pid = input("Enter Payroll ID : ")

    for p in payroll:
        if p["payroll_id"] == pid:
            print(f"""
Payroll Record Found

Payroll ID   : {p["payroll_id"]}
Employee     : {p["emp_name"]} ({p["emp_id"]})
Basic Salary : {p["basic_salary"]}
Bonus        : {p["bonus"]}
Deduction    : {p["deduction"]}
Net Salary   : {p["net_salary"]}
Date         : {p["date"]}
""")
            input("\nPress Enter...")
            return

    print("\nPayroll Record Not Found.")
    input("\nPress Enter...")


# ==========================
# REPORTS
# ==========================

def reports_menu():
    while True:
        clear_screen()

        print("=" * 70)
        print("                        REPORTS")
        print("=" * 70)

        print("""
1. Inventory Summary
2. Sales Summary
3. Purchase Summary
4. Payroll Summary
5. Back
""")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            inventory_summary_report()

        elif choice == "2":
            sales_summary_report()

        elif choice == "3":
            purchase_summary_report()

        elif choice == "4":
            payroll_summary_report()

        elif choice == "5":
            break

        else:
            print("\nInvalid Choice!")
            time.sleep(1)


def inventory_summary_report():
    clear_screen()

    print("=" * 70)
    print("                 INVENTORY SUMMARY REPORT")
    print("=" * 70)

    if not products:
        print("\nNo Products Found.")
    else:
        total_items = len(products)
        total_stock_value = sum(p["price"] * p["quantity"] for p in products)
        low_stock = [p for p in products if p["quantity"] < 5]

        print(f"\nTotal Distinct Products : {total_items}")
        print(f"Total Stock Value       : {total_stock_value}")

        print("\nLow Stock Items (Qty < 5):")
        if low_stock:
            for p in low_stock:
                print(f"  - {p['name']} ({p['product_id']}) : Qty {p['quantity']}")
        else:
            print("  None")

    input("\nPress Enter to Continue...")


def sales_summary_report():
    clear_screen()

    print("============================================================")
    print("                   SALES SUMMARY REPORT")
    print("============================================================")

    if not sales:
        print("\nNo Sales Found.")
    else:
        total_sales = len(sales)
        total_revenue = sum(s["total_price"] for s in sales)
        total_units = sum(s["quantity"] for s in sales)

        print(f"\nTotal Sales Transactions : {total_sales}")
        print(f"Total Units Sold         : {total_units}")
        print(f"Total Revenue            : {total_revenue}")

    input("\nPress Enter to Continue...")


def purchase_summary_report():
    clear_screen()

    print("============================================================")
    print("                 PURCHASE SUMMARY REPORT")
    print("============================================================")

    if not purchases:
        print("\nNo Purchases Found.")
    else:
        total_purchases = len(purchases)
        total_spent = sum(p["total_price"] for p in purchases)
        total_units = sum(p["quantity"] for p in purchases)

        print(f"\nTotal Purchase Transactions : {total_purchases}")
        print(f"Total Units Purchased       : {total_units}")
        print(f"Total Amount Spent          : {total_spent}")

    input("\nPress Enter to Continue...")


def payroll_summary_report():
    clear_screen()

    print("============================================================")
    print("                 PAYROLL SUMMARY REPORT")
    print("============================================================")

    if not payroll:
        print("\nNo Payroll Records Found.")
    else:
        total_records = len(payroll)
        total_paid = sum(p["net_salary"] for p in payroll)

        print(f"\nTotal Payroll Records : {total_records}")
        print(f"Total Amount Paid     : {total_paid}")

    input("\nPress Enter to Continue...")


# ==========================
# MAIN ENTRY POINT
# ==========================

def main():
    welcome_screen()
    loading_screen()
    initialize_data()

    while True:
        if login():
            dashboard()
        else:
            retry = input("\nTry Again? (Y/N) : ").upper()
            if retry != "Y":
                print("\nExiting System. Goodbye!")
                break


if __name__ == "__main__":
    main()