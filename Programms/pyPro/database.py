from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config

database = config['database']
database_url = database['engine'] + '://' + database['username'] + ':' + \
    database['password'] + '@' + database['host'] + '/' + database['database']

engine = create_engine(
    database_url,
    pool_size=database['pool_size'],
    max_overflow=database['max_overflow'],
    isolation_level="READ UNCOMMITTED",
    pool_pre_ping=True,
    pool_recycle=1800
)
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
