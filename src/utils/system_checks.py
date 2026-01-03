from utils.logger import logger
import os


def ensure_safe_environment():
    """
    Very basic safety check to avoid running in unintended environments.
    This is intentionally conservative and non-destructive.
    """
    if os.environ.get("EAS_PROD") == "1":
        logger.warning("EAS_PROD=1 detected. Aborting for safety.")
        raise SystemExit("Refusing to run in production-like environment.")

    logger.info("Environment checks passed (educational / lab use assumed).")
