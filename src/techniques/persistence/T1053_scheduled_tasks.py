from utils.logger import logger
from utils.platform_detection import get_platform


class Technique:
    """
    Simulated persistence via scheduled tasks.
    This is a harmless placeholder that does NOT create real tasks.
    """

    def __init__(self):
        self.meta = {
            "id": "T1053",
            "name": "Scheduled Task Persistence (Simulated)",
            "tactic": "persistence",
        }

    def run(self):
        platform = get_platform()
        logger.info("Simulating scheduled task persistence on: %s", platform)

        simulated_task = {
            "task_name": "SystemUpdateCheck",
            "interval": "Daily",
            "action": "Run benign script",
        }

        logger.info("Simulated scheduled task created: %s", simulated_task["task_name"])

        return {
            "platform": platform,
            "simulated_task": simulated_task,
        }
