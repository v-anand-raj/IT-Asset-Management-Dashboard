# IT Asset Management Dashboard

A web-based dashboard built using **Python, Flask, Pandas, HTML, CSS, and JavaScript**. The application provides employee authentication, employee asset information search, and Power BI-based asset visualization.

## Overview

The IT Asset Management Dashboard simplifies access to employee-related IT asset information through a centralized web interface.

Users can log in using their name and employee identification number and search for employee records using their name, Personal Number (P. No.), or Staff Number.

The application uses Pandas for employee data processing and Flask to handle backend operations and communication between the frontend and backend.

## Screenshots

### 1. Login Page

The login interface allows employees to access the dashboard using their name and Personal Number or Staff Number.
<img width="944" height="427" alt="Screenshot 2026-11-03 234217" src="https://github.com/user-attachments/assets/83c7d98c-ad9a-4ff9-bc47-c2a5f8996020" />



### 2. Power BI Asset Dashboard

The dashboard provides a visual overview of IT asset distribution, including allocated PCs, tagged and untagged assets, department-wise distribution, and other asset statistics.
<img width="658" height="360" alt="Screenshot 2026-11-03 233511" src="https://github.com/user-attachments/assets/bc23d502-6642-40df-aa95-3ca86cbcc2e6" />



### 3. Employee Search

Users can search employee records using their name, Personal Number, or Staff Number. The matching employee's IT asset details are dynamically displayed without reloading the page.
<img width="916" height="320" alt="Screenshot 2026-11-03 234312" src="https://github.com/user-attachments/assets/c11b270e-ac75-413f-8c97-71257b25c3c8" />



## Features

- **Employee Login:** Validates users using their name and Personal Number or Staff Number.
- **Employee Search:** Search employee records using their name, P. No., or Staff Number.
- **Data Processing:** Uses Pandas to load, clean, filter, and process employee records from a CSV file.
- **Dynamic Search Results:** Uses JavaScript Fetch API to retrieve search results asynchronously without reloading the page.
- **Employee Asset Details:** Displays information such as PC, monitor, UPS, printer, scanner, hostname, MAC address, operating system, and RAM.
- **Interactive UI:** Includes sidebar navigation, an animated interface, and a password visibility toggle.
- **Power BI Dashboard:** Provides an embedded dashboard interface for visualizing IT asset information.

## Tech Stack

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python     | Backend programming                        |
| Flask      | Web framework and request handling         |
| Pandas     | Employee data processing and filtering     |
| HTML       | Web page structure                         |
| CSS        | Styling and interface design               |
| JavaScript | DOM manipulation and asynchronous requests |
| CSV        | Employee data storage                      |
| Power BI   | IT asset visualization                     |

## Application Architecture

The application follows a layered architecture with separate responsibilities for the presentation, application, and data layers.

1. **Presentation Layer:** HTML, CSS, and JavaScript handle the user interface, login form, search form, and dynamic result display.
2. **Application Layer:** Flask handles incoming requests, validates login credentials, processes employee searches, and returns responses.
3. **Data Layer:** Employee records are loaded from a CSV file into a Pandas DataFrame for processing and retrieval.

### Application Workflow

```text
                 User
                  |
                  v
             Login Page
                  |
                  v
          Flask Authentication
                  |
          +-------+-------+
          |               |
      Valid Login     Invalid Login
          |               |
          v               v
      Home Page       Error Message
          |
          v
      Employee Search
          |
          v
       Fetch API
          |
          v
       Flask Route
          |
          v
    Pandas DataFrame
          |
          v
    Filter Employee Data
          |
          v
      JSON Response
          |
          v
  Dynamic Result Display
```

## Project Structure

```text
IT-Asset-Dashboard/
│
├── app.py
│
├── templates/
│   ├── login.html
│   └── home.html
│
├── employees.csv
├── requirements.txt
└── README.md
```

**Note:** The employee CSV file is not included in the public repository to protect employee information. A local dataset with the required column structure is needed to run the application.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/v-anand-raj/IT-Asset-Management-Dashboard.git
cd IT-Asset-Management-Dashboard
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the employee dataset

Place your local employee dataset named `employees.csv` in the project root directory, alongside `app.py`.

Ensure that it contains the required columns, including:

- Name
- P. No.
- Staff No.
- Department
- Section
- Location

Additional asset-related columns are required for displaying the corresponding employee asset details.

### 5. Run the application

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

## Backend Implementation

### Login Authentication

The Flask `/login` route receives the employee's name and identification number. Pandas compares the submitted values against employee records. If a matching record is found, the application returns the home page; otherwise, it displays an invalid credentials message.

### Employee Search

The `/search` route accepts search queries through a POST request.

Pandas performs:

- Case-insensitive partial matching for employee names.
- Exact matching for Personal Numbers.
- Exact matching for Staff Numbers.

The matching records are converted into dictionaries and returned as JSON using Flask's `jsonify()` function.

JavaScript processes the response and dynamically displays the employee information without a full-page reload.

## Future Improvements

- Integrate MySQL for structured and persistent employee data management.
- Implement secure authentication using password hashing and session management.
- Add role-based access control for different users.
- Improve search functionality with additional filters.
- Improve Power BI report integration.
- Deploy the application to a cloud platform.

## Security Note

This project was developed as an academic prototype. The current authentication mechanism uses employee identification numbers for validation and does not implement production-grade password security or session management.

The original employee dataset has been excluded from the repository to maintain data privacy.

---

**Developed as an IT Asset Management project using Python and Flask.**

## Author

**Anand Raj**

- GitHub: [v-anand-raj](https://github.com/v-anand-raj)


