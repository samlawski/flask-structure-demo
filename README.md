# Demo Flask App

This Demo application is meant to show how you could structure your Flask application. 

It uses Blueprints, databases, migrations, authentication and shows you how you could split all these different parts into different folders.

## Local Setup

### Virtual Environment

To install this locally, clone the repository. 

Then, you need to first create and activate a virtual environment: 

* `python3 -m venv venv`
* `source venv/bin/activate`

Now, you need to install all the packages in the requirements.txt file by running: 

`pip install -r requirements.txt`

### Environemnt Variables

Secondly, you need to set up your .env file. By default that file should be ignored and not committed to GitHub. Check out the file **.env.example**. This is an example for what the **.env** file looks like. Make sure to create that file with a similar set up before you start your server locally.

### Database Setup

Lastly, your database needs to be set up. Locally, the database is stored in a database.db SQLite file. We also don't commit that to GitHub because it's dynamic data that changes around whenever we add new records. So you need to set that up locally before you get started as well. 

* So run: `flask db init` to initialize the database. 
* Then, run `flask db upgrade` to actually execute all the migrations stored in the **migrations** folder. That will generate the database tables. 

### Run the server

Now you can **startup the server by running**:

```
python run.py
```

## Making changes to the database

Whenever you make any changes to your models (e.g. add columns) you need to create a new migration. To do that run the following two commands: 

```
flask run migrate -m 'migration description'
flask db upgrade
```

Replace 'migration description' with your own description that describes what the migration added or removed. 