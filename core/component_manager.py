
from core.manager import Manager


class ComponentManager:
    def __init__(self, owner):
        self._manager = Manager()
        self._owner = owner

    def add(self, cls_name, *args, **kwargs):
        self._manager.add(cls_name(self._owner, *args, **kwargs))

    def remove(self, obj):
        self._manager.remove(obj)

    def get(self, obj_cls):
        return self._manager.get(obj_cls)

    def update(self):
        self._manager.update()

    def fixed_update(self):
        self._manager.fixed_update()

    def draw(self, screen):
        self._manager.draw(screen)
