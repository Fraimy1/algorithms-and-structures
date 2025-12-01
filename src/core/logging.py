from loguru import logger

def log_and_raise(error: Exception) -> None:
    logger.error(f"{error.__class__.__name__}: {error.message}")
    raise error