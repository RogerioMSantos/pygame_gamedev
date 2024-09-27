
import pygame as pg


class Events:
    _events = []

    @staticmethod
    def update():
        Events._events = pg.event.get()

    @staticmethod
    def get(condition_fn):
        for e in Events._events:
            if condition_fn(e):
                return e
        return None
