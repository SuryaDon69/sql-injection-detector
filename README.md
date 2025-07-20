Screenshots:-
Home Page :-
<img width="1917" height="1038" alt="image" src="https://github.com/user-attachments/assets/bcc17fd6-0b12-4557-b0c3-453e919c1f40" />

Vulnerable Login:-
<img width="1908" height="985" alt="image" src="https://github.com/user-attachments/assets/159510e5-cd95-4f76-b862-4590b1d1ab0f" />

Secure Login:-
<img width="1912" height="982" alt="image" src="https://github.com/user-attachments/assets/d4fde4b4-5c0c-4784-a008-edf998b03347" />

Logs:-
<img width="1918" height="997" alt="image" src="https://github.com/user-attachments/assets/11622856-dd15-4fa3-b4df-e2946a3d6d3a" />


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
