import logging
from abc import ABC, abstractmethod
from typing import ClassVar

from ModuBotCore import BaseConfig


class BaseModule(ABC, BaseConfig):
    NAME: ClassVar[str] = "BaseModule"
    ENABLING: ClassVar[bool] = True

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(self.NAME)

    @abstractmethod
    def on_enable(self):
        pass

    @abstractmethod
    def on_disable(self):
        pass
