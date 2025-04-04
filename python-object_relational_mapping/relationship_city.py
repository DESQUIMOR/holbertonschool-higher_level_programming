#!/usr/bin/python3
"""Object-relational mapping - task 15. City relationship
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from relationship_state import Base


class City(Base):
    """Defines ORM class for table `cities`, with 3 columns:

       `id` (Column): unique identifier, primary key
       `name` (Column): name of city
       `state_id` (Column): integer, foreign key `states.id`

    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
