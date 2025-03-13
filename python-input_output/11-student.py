#!/usr/bin/python3
"""
A Student class that defines a Student (module)
"""


class Student:
    """
    A Student class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """
        INIT
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student instance
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces attributes of the Student instance
        with values from a dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
