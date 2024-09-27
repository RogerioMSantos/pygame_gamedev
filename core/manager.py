
from typing import List

from core.base import BaseObject


class Manager:
    def __init__(self):
        self._objects: List[BaseObject] = []

    def add(self, obj):
        self._objects.append(obj)

    def remove(self, obj):
        if obj in self._objects:
            self._objects.remove(obj)

    def get(self, obj_cls):
        for o in self._objects:
            if isinstance(o, obj_cls):
                return o
        return None

    def update(self):
        for o in self._objects:
            if o.active:
                o.update()

    def fixed_update(self):
        for o in self._objects:
            if o.active:
                o.fixed_update()

    def draw(self, screen):
        for o in self._objects:
            if o.active:
                o.draw(screen)
