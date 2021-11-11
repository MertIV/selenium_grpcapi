import contextlib
from sqlalchemy.orm import Session
from app import db
from app.module.db.db_model import Base

def execute(*args,**kwargs):
    with db.connect() as conn:
        result = conn.execute(*args,**kwargs)
        result = db.connect().execute()
        print(result.all())
    return result

def create_session():
    session = Session(db, future=True)
    return session

def truncate_tables():
    with contextlib.closing(db.connect()) as con:
        trans = con.begin()
        for table in reversed(Base.metadata.sorted_tables):
            con.execute(table.delete())
        trans.commit()

def drop_tables():
    Base.metadata.drop_all(db)

def create_tables():
    Base.metadata.create_all(db)
