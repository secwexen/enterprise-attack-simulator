from utils.logger import logger


class AttackExecutor:
    def __init__(self):
        self.results = []

    def run_techniques(self, techniques):
        logger.info("Running %d techniques", len(techniques))

        for technique in techniques:
            technique_id = technique.meta.get("id", "UNKNOWN")
            name = technique.meta.get("name", technique.__class__.__name__)

            logger.info("Executing technique %s (%s)", technique_id, name)

            try:
                outcome = technique.run()
                self.results.append({
                    "id": technique_id,
                    "name": name,
                    "status": "success",
                    "details": outcome,
                })
            except Exception as exc:
                logger.exception("Technique %s (%s) failed", technique_id, name)
                self.results.append({
                    "id": technique_id,
                    "name": name,
                    "status": "error",
                    "details": str(exc),
                })

        return self.results
