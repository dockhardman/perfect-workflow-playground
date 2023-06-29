from typing import Text

from pydantic import BaseSettings

from .version import VERSION


class Settings(BaseSettings):
    version: Text = VERSION
