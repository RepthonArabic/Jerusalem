# config values will be loaded from here

import os

ENV = bool(os.environ.get("ENV", "ANYTHING"))

if ENV:
    from sample_config import Config  # noqa
elif os.path.exists("config.py"):
    from config import Development as Config  # noqa
else:
    from sample_config import Config  # noqa
