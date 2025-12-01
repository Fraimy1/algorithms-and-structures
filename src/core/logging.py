from loguru import logger  # type: ignore[import-not-found]
from src.core.errors import CustomError

def log_and_raise(error: CustomError) -> None:
    logger.error(f"{error.__class__.__name__}: {error.message}")
    raise error
