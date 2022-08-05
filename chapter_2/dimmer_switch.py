from msilib.schema import Class


class DimmerSwitch:
    def __init__(self) -> None:
        self.is_on = False
        self.brightness_level = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def raise_level(self, value):
        if value <= 10:
            for i in range(self.brightness_level, value):
                self.brightness_level = i + 1

    def lower_level(self, value):
        if value >= 0:
            for i in range(self.brightness_level, value - 1, -1):
                self.brightness_level = i + 1

    def show(self):
        print("is_on:", self.is_on)
        print("brightness_level:", self.brightness_level)

dimmer_switch = DimmerSwitch()
dimmer_switch.show()
dimmer_switch.turn_on()
dimmer_switch.raise_level(5)
dimmer_switch.show()
dimmer_switch.turn_off()
dimmer_switch.show()
dimmer_switch.turn_on()
dimmer_switch.lower_level(2)
dimmer_switch.show()