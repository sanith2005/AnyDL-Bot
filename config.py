import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("1788714820:AAFE_SabbETUv5njBtUSV0v3RApN4tBFdT4", "")

    APP_ID = int(os.environ.get("2409052", 12345))

    API_HASH = os.environ.get("b8c5a4066d7312639b130ddaaeafff92", "")
