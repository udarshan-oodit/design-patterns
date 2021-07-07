from .chair import Chair


class ModernChair(Chair):
    def has_legs(self):
        return False

    def sit_on(self):
        print('Sitting on the modern chair')
