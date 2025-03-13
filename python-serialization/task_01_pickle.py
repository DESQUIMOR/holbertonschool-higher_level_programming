import pickle


class CustomObject:
    """
    A class to demonstrate object serialization and deserialization.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initializes a CustomObject instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as error:
            print(f"Error serializing object: {error}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError) as error:
            print(f"Error deserializing object: {error}")
            return None
