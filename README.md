A web application to manage funds, loans, and repayments efficiently.

Features
User registration & authentication
Deposit & withdrawal tracking
Loan management with interest calculation
Loan repayment functionality
User dashboard to view financial status
Installation
1. Clone the Repository
sh
Copy
Edit
git clone https://github.com/yourusername/money-lending-app.git
cd money-lending-app
2. Create a Virtual Environment & Install Dependencies
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
3. Apply Migrations & Load Sample Data
sh
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata test_data.json  # Optional test data
4. Create a Superuser (for Admin Access)
sh
Copy
Edit
python manage.py createsuperuser
5. Run the Development Server
sh
Copy
Edit
python manage.py runserver
Now, visit http://127.0.0.1:8000/ in your browser.

Usage
User Dashboard: View balances, loans, and repayments.
Deposit Money: Add funds to your account.
Request Loan: Apply for a loan with interest.
Repay Loan: Repay loans partially or fully.
Admin Panel
Access the Django admin panel at:
👉 http://127.0.0.1:8000/admin/

Technologies Used
Django (Python Framework)
SQLite / PostgreSQL (Database)
Bootstrap / Tailwind CSS (Frontend)
