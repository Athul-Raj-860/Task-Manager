 Task Manager
 
  A simple Django-based Task Management application with CRUD functionality and status filtering.

 Features
 
  Create, read, update, and delete tasks
  Filter tasks by status (NotStarted, InProgress, Completed, etc.)

RESTful API using Django REST Framework

  Status-based task filtering endpoint

Project Structure

TaskManager/
├── task/                 # Django app for task operations
│   ├── models.py         # Task model
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API views
│   └── urls.py           # App URLs
├── TaskManager/          # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md

 Setup Instructions
 
1. Clone the repository
git clone https://github.com/your-username/task-manager.git
cd task-manager

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt
If you don't have requirements.txt, generate it with:
pip freeze > requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Run the development server
python manage.py runserver
Open your browser at http://127.0.0.1:8000

 API Endpoints

Method	  Endpoint	        Description
GET	     view/     	        List all tasks
POST	   add/        	      Create a new task
PUT	     update/<id>/      	Update a task (partial/full)
DELETE	 delete/<id>/	      Delete a task
GET	     filter/<status>/  	Filter tasks by status


Acknowledgements
Django
Django REST Framework
