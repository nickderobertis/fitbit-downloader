import pytest

from fitbit_downloader.config import Config, OAuthConfig, DownloadConfig
from tests.config import GENERATED_PATH


@pytest.fixture
def config() -> Config:
    return Config(
        client_id="a",
        client_secret="b",
        oauth_config=OAuthConfig(access_token="c", refresh_token="d", expires_at=123),
        download=DownloadConfig(out_folder=GENERATED_PATH),
    )