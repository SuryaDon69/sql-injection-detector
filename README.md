
MySQL-Based SQL Injection Playground Setup Instructions:

1. Create the database and table manually in MySQL:
   - Log in to MySQL:
     mysql -u root -p
   - Run the following:
     CREATE DATABASE sqli_demo;
     USE sqli_demo;
     CREATE TABLE users (username VARCHAR(255), password VARCHAR(255));
     INSERT INTO users VALUES ('admin', 'admin');

2. Install Python packages:
   pip install flask mysql-connector-python

3. Update `app.py` with your MySQL password.

4. Run the app:
   python app.py

5. Open browser and navigate to:
   http://127.0.0.1:5000
