import json
from pathlib import Path
from datetime import datetime
from utils.logger import logger
from tabulate import tabulate


class ReportGenerator:
    def generate(self, results, output_path):
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        report = {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "summary": {
                "total": len(results),
                "success": sum(1 for r in results if r["status"] == "success"),
                "error": sum(1 for r in results if r["status"] == "error"),
            },
            "results": results,
        }

        with output_path.open("w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        logger.info("JSON report written to %s", output_path)

        # Optional: also print a simple table to console
        table = [
            [r["id"], r["name"], r["status"]]
            for r in results
        ]
        logger.info("\n" + tabulate(table, headers=["ID", "Name", "Status"]))
