from sqlalchemy import *
from migrate import *
import datetime

meta = MetaData()

contents = Table(
    'contents', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    Column('updated_at', DateTime(timezone=True),
           server_default=func.now(), onupdate=func.now())
)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    contents.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    contents.drop()
