import datetime
import json
from pathlib import Path

import fitbit

from tests.config import INTRADAY_RESPONSES_FOLDER, RESPONSES_FOLDER


def download_sample_responses(client: fitbit.Fitbit):
    for activity_type in ("steps", "heart", "elevation"):
        activity_str = f"activities/{activity_type}"
        out_path = INTRADAY_RESPONSES_FOLDER / f"{activity_type}.json"
        data = client.intraday_time_series(activity_str)
        _write_json(data, out_path)

    sleep_data = client.get_sleep(datetime.date.today())
    sleep_out_path = RESPONSES_FOLDER / "sleep.json"
    _write_json(sleep_data, sleep_out_path)


def _write_json(data: dict, path: Path):
    path.write_text(json.dumps(data, indent=2))
