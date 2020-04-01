#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represent an Amenity for a MySQL database.

    Attributes:
        name: The Amenity name
        place_amenities (relationship): The Place - Amenity relationship.

    """

    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       viewonly=False)
    else:
        name = ''
