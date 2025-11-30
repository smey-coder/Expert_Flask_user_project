from flask_sqlalchemy import SQLALchemy
from flask_wtf import CSRFProtect

db =  SQLALchemy()
csrf = CSRFProtect()