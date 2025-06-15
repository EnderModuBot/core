import os
from dataclasses import dataclass
from typing import ClassVar

from . import BaseConfig


@dataclass(frozen=True)
class LoggerConfig(BaseConfig):
    LEVEL: ClassVar[str] = os.getenv("LOG_LEVEL", "INFO")
    FORMAT: ClassVar[str] = "[%(asctime)s - %(levelname)s - %(name)s]: %(message)s"
    DATEFMT: ClassVar[str] = "%m/%d/%Y %H:%M:%S"
