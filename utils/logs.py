import logging


class Logger:

    def __init__(self, is_log_required: bool) -> None:
        self.is_log_required = is_log_required
        self.logger = ''