
class BaseObject:
    def __init__(self, active=True, name=""):
        self.name = name
        self.active = active

    def update(self):
        """ update function called once per frame """

    def fixed_update(self):
        """ update function called once per physics update """

    def draw(self, screen):
        """ function to draw the object """
