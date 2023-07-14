"""Class freindly_error_msg"""


class freindly_error_msg(Exception):
    """Customize Error message to be showed in freindly manner"""

    def __init__(self, message):
        super().__init__(message)
