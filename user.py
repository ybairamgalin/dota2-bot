
class User:
    """Class contains all data about single user"""
    """telegram id"""
    id = None

    """
    0 - <100
    1 - 100-500
    2 - 500-1000
    3 - 1000+
    """
    hours = None

    """
    1 - carry
    2 - mid
    3 - hard
    4 - semi sup
    5 - full sup 
    """
    role = None

    """
    0 - strength
    1 - agility
    2 - intelligence
    """
    category = None

    """
    0 - /start pressed
    1 - time set
    2 - role set
    """
    state = 0

    def __init__(self, tg_id: int):
        self.id = tg_id
