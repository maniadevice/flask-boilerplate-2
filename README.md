### Flask Boilerplate with SQLite db, Flask-SQLAlchemy and Flask-Login

The app is split into two blueprints in core and task modules. The core has a simple view and task has a more complex view including a form post.

The SQLite db is in todo.db that was created by running the following 
```shell
flask db init
flask db migrate -m "Put any comment of your choice here"
flask db upgrade
```

To run the app run
```shell
poetry install
poetry shell
flask run
```

The vars in .flaskenv file will be used when running the application

This tutorial is taken from [here](https://dev.to/nagatodev/adding-authentication-to-a-flask-application-53ep).