import json
from pathlib import Path


class DatasetProcessor:
    """Read-only inspection tools for DatasetPuppy."""

    def inspect_dataset(self, file_path):
        path = Path(file_path)

        result = {
            "file_name": path.name,
            "file_type": path.suffix.lower(),
            "records": 0,
            "valid_records": 0,
            "invalid_records": 0,
        }

        if path.suffix.lower() == ".jsonl":
            self._inspect_jsonl(path, result)
        elif path.suffix.lower() == ".json":
            self._inspect_json(path, result)
        else:
            raise ValueError(f"Unsupported dataset type: {path.suffix}")

        return result

    def _inspect_jsonl(self, path, result):
        with path.open("r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                result["records"] += 1

                try:
                    json.loads(line)
                    result["valid_records"] += 1
                except json.JSONDecodeError:
                    result["invalid_records"] += 1

    def _inspect_json(self, path, result):
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            result["records"] = len(data)
            result["valid_records"] = len(data)
        else:
            result["records"] = 1
            result["valid_records"] = 1
