from models.chairs.chair import Chair


class OldChair(Chair):
    def has_legs(self):
        return True

    def sit_on(self):
        print('Sitting on the old chair')
