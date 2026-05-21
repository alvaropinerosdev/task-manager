# User.py

class User:

    FIELDS = {
        "id",
        "name",
        "email",
        "password_hash",
        "phone"
    }

    def __init__(self, **kwargs):

        self.id = kwargs.get("id")

        self.name = kwargs.get("name", "")

        self.email = kwargs.get("email", "")

        self.password_hash = kwargs.get("password_hash", "")

        self.phone = kwargs.get("phone")

    # Convert object to dictionary
    def to_dict(self):

        return {
            field: getattr(self, field)
            for field in self.FIELDS
        }

    # Create object from dictionary
    @classmethod
    def from_dict(cls, data):

        filtered_data = {
            key: value
            for key, value in data.items()
            if key in cls.FIELDS
        }

        return cls(**filtered_data)