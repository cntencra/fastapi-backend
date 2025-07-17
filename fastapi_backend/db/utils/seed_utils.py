import json
from pathlib import Path
from fastapi_backend.db.schemas.seed_models import SeedDataDB

def load_seed_data(filepath: Path ) -> SeedDataDB:
    with open(filepath) as f:
        data = json.load(f)
    return SeedDataDB(**data)