import logging

logging.basicConfig(level=logging.INFO)
def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Entering {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Exiting {func.__name__}")
        return result
    return wrapper