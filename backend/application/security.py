from flask_security import Security, SQLAlchemyUserDatastore
from .data.models import db, User, Roles

user_datastore = SQLAlchemyUserDatastore(db,User,Roles)
security = Security()