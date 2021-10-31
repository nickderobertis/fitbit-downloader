import datetime
from typing import Final, Optional

from pyappconf import BaseConfig, AppConfig, ConfigFormats
from pydantic import BaseModel

APP_NAME: Final = "fitbit-downloader"


class OAuthConfig(BaseModel):
    access_token: str
    refresh_token: str
    expires_at: float
    
    @property
    def expires_at_time(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.expires_at)


class Config(BaseConfig):
    client_id: str
    client_secret: str
    oauth_config: Optional[OAuthConfig]

    _settings = AppConfig(
        app_name=APP_NAME, default_format=ConfigFormats.TOML, config_name="fitbit-downloader"
    )

    class Config:
        env_file = ".env"
        env_prefix = "FITBIT_DOWNLOADER_"


if __name__ == "__main__":
    print(Config.load_recursive())
