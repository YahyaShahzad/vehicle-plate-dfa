# Pakistan Vehicle Plate Validator

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://vehicle-plate-dfa.onrender.com)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [DFA Theory](#dfa-theory)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Screenshots](#project-screenshots)
- [Live Demo](#live-demo)
- [License](#license)
- [Authors](#authors)

---

## Overview

The **Pakistan Vehicle Plate Validator** is a web application that validates vehicle registration plates for all provinces and territories of Pakistan using **Deterministic Finite Automata (DFA)**.  
It provides a **visual plate preview**, **validation history**, and **charts** showing vehicle and province distributions.

This project demonstrates:
- DFA implementation in Python
- Web application development using Flask
- Data visualization using Chart.js
- Professional deployment on Render

---

## Features

- Validate vehicle plates based on province and vehicle type
- Visual plate preview (color-coded according to real-world formats)
- Validation history of the last 20 submissions
- Charts showing:
  - Vehicle type distribution
  - Province-wise distribution
- Responsive and modern UI using Bootstrap
- Live demo available online

---

## Technologies Used

- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend:** Python 3.13, Flask
- **Data Visualization:** Chart.js
- **Version Control:** Git & GitHub
- **Deployment:** Render.com

---

## DFA Theory

The project uses **Deterministic Finite Automata (DFA)** to validate vehicle plate formats.  

### Key Points:

- Each province has a specific plate format, e.g., Punjab:
  - 4-Wheeler: `L-DDDD` (e.g., `L-1234`)
  - 2-Wheeler: `LLL-DDDD` (e.g., `ABC-1234`)
- DFA ensures only valid letters/digits in the correct positions.
- Invalid patterns are rejected immediately.

Example DFA Pattern:

| Province | Vehicle Type | Pattern |
|----------|--------------|---------|
| Punjab   | 4-Wheeler    | L-DDDD  |
| Sindh    | 2-Wheeler    | LLL-DDDD|
| ICT      | 4-Wheeler    | LLL-DDD |

This demonstrates **formal automata theory** applied to a practical web application.

---

## Installation & Setup

### Prerequisites

- Python 3.13+
- Git
- Virtual Environment (recommended)

### Steps

1. Clone the repository:

```bash
git clone https://github.com/YahyaShahzad/vehicle-plate-dfa.git
cd vehicle-plate-dfa
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open the app in your browser:

cpp
Copy code
http://127.0.0.1:5000
Note: For Render deployment, Flask is configured to use host=0.0.0.0 and the port from environment variables.

Usage
Enter a plate number in the input box.

Select the province from the dropdown.

Select the vehicle type (2-Wheeler / 4-Wheeler).

Click Validate.

View results:

Result: Valid / Invalid

Plate Preview: Color-coded

Validation History: Last 20 validations

Charts: Vehicle type & province distributions

Project Screenshots
Plate Input & Preview

Validation History

Charts

(Add your own screenshots in a /screenshots folder)

Live Demo
Try the live demo here:
Pakistan Vehicle Plate Validator

License
This project is licensed under the MIT License.
See the LICENSE file for details.

Authors
Yahya Shahzad – Developer & Project Lead

Bilal Imtiaz – Contributor

Acknowledgements
DFA theory: University Automata Lectures

Chart.js for visualizations

Bootstrap for responsive design
