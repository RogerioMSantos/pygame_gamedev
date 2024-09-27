
from core.base import BaseObject


class Component(BaseObject):
    def __init__(self, owner: BaseObject, active=True, name=""):
        super().__init__(active, name)
        self.object = owner
