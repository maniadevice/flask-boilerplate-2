from task.models import Category
from utils.database import db
from base import app

with app.app_context():
    ctgry1 = Category(name='Business')
    ctgry2 = Category(name='Personal')
    ctgry3 = Category(name='Other')

    db.session.add(ctgry1)
    db.session.add(ctgry2)
    db.session.add(ctgry3)

    db.session.commit()

    categories = Category.query.all()
    for c in categories:
        print(c.name)
