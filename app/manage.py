from flask.cli import FlaskGroup
from app.main import app, db
from app.models.user import User

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    sam = User('Sam','1234','12345','Floripa','Sam@gmail.com')
    Pedro = User('Pedro','1234','12345','Floripa','Pedro@gmail.com')
    db.session.add_all([sam,Pedro])
    db.session.commit()

if __name__ == "__main__":
    cli()