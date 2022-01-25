from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from config import config
import re

class Contents(Base):
    __tablename__ = 'contents'
    __table_args__ = {'autoload': True}
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
			'id': self.id,
			'name': self.name,
			'created_at': self.created_at,
			'updated_at': self.updated_at
		}
