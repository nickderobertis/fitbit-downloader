import fitbit

from fitbit_downloader.authorize import set_authorization, initial_client_authorization
from fitbit_downloader.config import Config


def get_client(config: Config) -> fitbit.Fitbit:
    if config.oauth_config is None:
        initial_client_authorization(config)

    def on_refresh_token(raw_token_data: dict[str, any]):
        set_authorization(config, raw_token_data)

    oa = config.oauth_config
    return fitbit.Fitbit(
        config.client_id,
        config.client_secret,
        oauth2=True,
        access_token=oa.access_token,
        refresh_token=oa.refresh_token,
        expires_at=oa.expires_at,
        refresh_cb=on_refresh_token,
    )
