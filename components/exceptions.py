"""Class friendly_error_msg"""


class friendly_error_msg(Exception):
    """Customize Error message to be showed in freindly manner"""

    def __init__(self, message):
        super().__init__(message)
