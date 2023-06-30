import logging


class Logger:
    """Represents a singleton logger that is globally available across the application."""

    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.handler = logging.StreamHandler()
        
    def initialize_logger(self, is_log_required: bool=None) -> None:
        """Initializes the level of the logger based on options passed into the CLI."""

        if is_log_required:
            self.logger.setLevel(logging.INFO)
            self.handler.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.ERROR)
            self.handler.setLevel(logging.ERROR)
        self.logger.addHandler(self.handler)

    def is_log_required(self) -> bool:
        """Returns if the low-level log mode is enabled."""

        if self.logger.level == logging.ERROR:
            return False
        return True
    
    def error(self, message: str) -> None:
        """If an error-level log message is requested."""

        self.logger.error(message)
    
    def info(self, message: str) -> None:
        """If an info-level log message is requested."""
        self.logger.info(message)


logger = Logger()
