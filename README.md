Campaign Tracker

A simple Campaign Tracker web application built using HTML, CSS, JavaScript, and Python (Flask) with a MySQL database.

->Features

*Add new marketing campaigns

*View all campaigns

*Update campaign status (Active / Paused / Completed)

*Delete campaigns

*Backend connected with MySQL

->Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python (Flask)

Database: MySQL

->Setup Instructions
1. Clone the repository
git clone https://github.com/yourusername/campaign-tracker.git
cd campaign-tracker

2. Install dependencies
pip install -r requirements.txt

3. Set up the MySQL database

Run the following commands in your MySQL terminal:

CREATE DATABASE campaign_db;
USE campaign_db;

CREATE TABLE campaigns (
    id INT AUTO_INCREMENT PRIMARY KEY,
    campaign_name VARCHAR(100),
    client_name VARCHAR(100),
    start_date DATE,
    status VARCHAR(50)
);

4. Run the Flask server
python app.py


Then open your browser and go to:
http://localhost:5000
