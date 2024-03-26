from pathlib import Path
import json

json_file_path = Path("questions.json")
with open(json_file_path, "r", encoding="utf-8") as json_file:
    json_data = json_file.read()

data = json.loads(json_data)
pass
