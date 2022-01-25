from lib.decorators.dbSession import provide_session
from entites.Contents import Contents
import pdb

@provide_session
def createContents(contentsJson, session=None):
    try:
        contents = Contents(
            name = "kafka"
        )
        session.add(contents)
        session.commit()
    except Exception as e:
        session.rollback()
        return null

    return contents.to_dict()

@provide_session
def getContents(session=None):
    contents = []
    records = session.query(Contents).all()
    for record in records:
        contents.append(record.to_dict())
    return contents
