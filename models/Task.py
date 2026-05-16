# task.py

class Task:

    FIELDS = {
        "id",
        "title",
        "description",
        "started_date",
        "finished_date",
        "user_id",
        "id_category",
        "id_status",
        "active"
    }

    def __init__(self, **kwargs):

        self.id = kwargs.get("id")

        self.title = kwargs.get("title", "")

        self.description = kwargs.get("description")

        self.started_date = kwargs.get("started_date")

        self.finished_date = kwargs.get("finished_date")

        self.user_id = kwargs.get("user_id")

        self.id_category = kwargs.get("id_category")

        self.id_status = kwargs.get("id_status", 0)

        self.active = kwargs.get("active", 1)

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