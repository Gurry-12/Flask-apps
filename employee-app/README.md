
# Employee Management System

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Employee Management System is a web application developed using Flask, SQLAlchemy, and Behave. The application allows users to manage employee records efficiently, enabling CRUD (Create, Read, Update, Delete) operations. This project demonstrates the integration of Behave for Behavior-Driven Development (BDD) testing.

## Technologies Used
- **Flask**: A micro web framework for Python, used for developing the web application.
- **SQLAlchemy**: An ORM (Object-Relational Mapper) that simplifies database interactions.
- **Behave**: A BDD testing framework that allows writing tests in plain English.
- **HTML/CSS**: For the front-end interface.

## Features
- **Employee Management**: Create, read, update, and delete employee records.
- **Form Validation**: Ensures proper data entry for employee records.
- **Testing**: Comprehensive BDD testing using Behave for all functionalities.
- **Responsive Design**: User-friendly interface for managing employee data.

## Setup Instructions
To set up the Employee Management System on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd employee-management-system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**:
   - Make sure to configure your database connection in the `config.py` file (if applicable).
   - Run the following command to initialize the database:
     ```bash
     flask db init
     flask db migrate
     flask db upgrade
     ```

## Usage
1. **Run the application**:
   ```bash
   flask run
   ```

2. **Open your web browser and navigate to**: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

3. **Manage Employee Records**: Use the interface to create, view, update, or delete employee records.

## Testing
To run the tests using Behave, ensure you have Behave installed, then run:
```bash
behave
```
This will execute all the defined scenarios in your feature files.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request or open an issue in the repository.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

