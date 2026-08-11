<div align="center">

# 🏢 Enterprise ERP Management System

### A Smart, Modular Business Management Solution — Inventory, Sales, Purchases, HR & Payroll in One Platform

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](#)
[![Made With](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red?style=for-the-badge)](#)

**Developed by Muhammad Shahzaib**

</div>

---

## 📖 Overview

**Enterprise ERP Management System** is a complete, terminal-based Enterprise Resource Planning solution built entirely in Python. It unifies five core business functions — **Inventory, Sales, Purchases, Human Resources, and Payroll** — into a single, secure, menu-driven platform, backed by a structured JSON database and real-time reporting.

Designed with clean modular architecture, auto-generated IDs, and self-healing data storage, it's built to scale from a small business tool into the foundation of a larger enterprise system.

---

## ✨ Features

### 🔐 Authentication & Security
- Secure login system with a default admin account created automatically on first run
- Change password functionality for account security

### 📦 Inventory Management
- Add, view, search, update, and delete products
- Auto-generated Product IDs (`P001`, `P002`, ...)
- Real-time stock quantity tracking

### 💰 Sales Management
- Record new sales with automatic stock deduction
- Auto-calculated totals based on quantity and unit price
- Full sales history with search by Sale ID
- Live revenue totals

### 🚚 Purchase Management
- Supplier database with auto-generated Supplier IDs
- Record purchases from suppliers, restocking existing products or creating new ones on the fly
- Full purchase history with total spend tracking

### 👥 HR Management
- Add, view, search, update, and delete employee records
- Auto-generated Employee IDs (`E001`, `E002`, ...)
- Track designation, salary, and contact details

### 💵 Payroll Management
- Generate payroll per employee with bonus and deduction support
- Automatic net salary calculation
- Full payroll history with search functionality

### 📊 Business Reports
- **Inventory Summary** — total products, stock value, and low-stock alerts (qty < 5)
- **Sales Summary** — total transactions, units sold, and revenue
- **Purchase Summary** — total transactions, units purchased, and amount spent
- **Payroll Summary** — total records and total amount paid

### 🛠️ Under the Hood
- Auto-generated, sequential ID system across all modules
- Robust input validation for numeric fields
- JSON-based persistent storage with automatic file/folder creation
- Graceful handling of missing or corrupted data files
- Clean, object-oriented `Product` class structure

---

## 🗺️ Application Flow

```
Welcome Screen → Loading Screen → Initialize Data → Login
                                                        │
                                                        ▼
                                              ADMIN DASHBOARD
        ┌───────────────┬───────────────┬───────────────┼───────────────┬───────────────┐
        │               │               │               │               │               │
   Inventory        Sales           Purchase          HR            Payroll         Reports
  Management      Management       Management     Management      Management
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8** or higher installed on your system

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/enterprise-erp-system.git

# 2. Move into the project directory
cd enterprise-erp-system

# 3. Run the application
python erp_system.py
```

> No external packages required — the project uses only Python's standard library (`os`, `json`, `time`, `platform`, `datetime`).

On first run, a `data/` folder is automatically created along with a default admin account, so the system is ready to use immediately.

### Default Login Credentials

| Username | Password  |
|----------|-----------|
| `admin`  | `admin123`|

> ⚠️ For production/client use, it's strongly recommended to change the default password immediately using the **Change Password** option, or move credentials to a more secure authentication method.

---

## 🧩 Project Structure

```
enterprise-erp-system/
├── erp_system.py             # Core application logic
├── data/
│   ├── users.json             # Auto-generated: user accounts & credentials
│   ├── products.json          # Auto-generated: inventory data
│   ├── suppliers.json         # Auto-generated: supplier records
│   ├── employees.json         # Auto-generated: employee records
│   ├── sales.json             # Auto-generated: sales transactions
│   ├── purchases.json         # Auto-generated: purchase transactions
│   └── payroll.json           # Auto-generated: payroll records
└── README.md                   # Project documentation
```

---

## 🖼️ Preview

```
===============================================================
                ENTERPRISE ERP MANAGEMENT SYSTEM
================================================================
            Smart Business Management Solution
================================================================
               Developed by Muhammad Shahzaib
================================================================

=======================================================
                 ENTERPRISE ERP SYSTEM
=======================================================
                     ADMIN DASHBOARD
=======================================================

1. Inventory Management
2. Sales Management
3. Purchase Management
4. HR Management
5. Payroll Management
6. Reports
7. Change Password
8. Logout
9. Exit
```

---

## 🛠️ Tech Stack

| Layer         | Technology            |
|---------------|------------------------|
| Language       | Python 3               |
| Data Storage   | JSON (file-based)      |
| Interface      | Command Line (CLI)     |
| Architecture   | Modular, OOP-based      |

---

## 🔮 Future Enhancements

- [ ] GUI or web-based dashboard (Tkinter / Flask / Django)
- [ ] Role-based access control (Admin, Manager, Staff)
- [ ] Password hashing & encrypted authentication
- [ ] Database migration (SQLite / PostgreSQL / MySQL)
- [ ] Export reports to PDF/Excel
- [ ] Multi-branch and multi-user support
- [ ] Attendance and leave management module
- [ ] Invoice generation for sales and purchases

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](../../issues) or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

<div align="center">

### ⭐ If you find this project useful, consider giving it a star!

**Made with 💻 and ☕ by Muhammad Shahzaib**

</div>
