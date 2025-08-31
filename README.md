Screenshots:-
Home Page :-
<img width="1918" height="1033" alt="image" src="https://github.com/user-attachments/assets/8cad0f1b-34ac-4ff5-b6e3-fcbf3b8e1694" />

Vulnerable Login:-
<img width="1918" height="1001" alt="image" src="https://github.com/user-attachments/assets/c146d751-2287-4320-a914-7082d1e56688" />

Secure Login:-
<img width="1915" height="998" alt="image" src="https://github.com/user-attachments/assets/d44a24ac-32a7-4fc0-924a-10365e43b050" />

Logs:-
<img width="1918" height="993" alt="image" src="https://github.com/user-attachments/assets/1891b5f5-e2a6-4697-a236-ea8ac94bb447" />


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
