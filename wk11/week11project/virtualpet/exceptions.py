class TamagotchiException(Exception):
    """
    Base exception class
    """


class DeathException(TamagotchiException):
    """
    Exception raised when an animal dies
    """


class RunAwayException(TamagotchiException):
    """
    Exception raised when an animal runs away because it is too bored with you
    """