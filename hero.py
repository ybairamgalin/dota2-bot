
class Hero:
    time_needed = None
    role = None
    category = None
    image = None
    description = None

    def __init__(self, time_needed: int, role: int, category: int,
                 image: str, description: str):
        self.time_needed = time_needed
        self.role = role
        self.category = category
        self.image = "img/" + image
        self.description = description

