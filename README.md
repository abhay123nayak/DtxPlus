# 🩺 Provider Platform - QA Automation Framework

This project automates QA testing for a healthcare Provider Platform using Selenium, Pytest, and the Page Object Model (POM) design. It validates core workflows such as login, patient creation, dashboard verification, and logout, while integrating with Allure for test reporting.
(https://github.com/abhay123nayak/DtxPlus)

---

## 🌐 Platform Details

- **URL:** https://qa-takehome.dtxplus.com/
- **Username:** `dtxplus`
- **Password:** `dtxplus`

---

## 🧰 Tools & Technologies

| Tool            | Purpose                              |
|-----------------|---------------------------------------|
| Python 3.8+     | Programming language                  |
| Selenium        | UI automation                         |
| Pytest          | Test runner and assertion framework   |
| Allure          | Advanced test report visualizations   |
| POM             | Page Object Model for maintainability |
| ConfigParser    | Config management                     |
| Faker (optional)| Dummy data generation                 |

---

## 🗂️ Project Folder Structure

provider-platform-tests/
│
├── locators/ # Element locators
│
├── pages/ # Page Object classes (POM)
│ ├── login_page.py
│ ├── dashboard_page.py
│ ├── logout_page.py
│ └── patient_form_page.py
│
├── tests/ # Test scripts
│ ├── test_login.py
│ ├── test_dashboard.py
│ ├── test_add_patient_success.py
│ └── test_logout.py
│
├── utils/ # Utility modules
│ ├── config.py
│ ├── driver_factory.py
│ └── helpers.py
│
├── reports/ # Allure report output
│
├── config.ini # Environment config
├── conftest.py # Pytest fixtures
└── README.md # Project documentation

# run proeject with this cmd 
pytest tests/test_login.py::TestLogin::test_valid_login --alluredir=reports/
