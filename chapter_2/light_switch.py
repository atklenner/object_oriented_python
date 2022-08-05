class LightSwitch:
    def __init__(self) -> None:
        self.is_on = False

    def turn_on(self) -> None:
        self.is_on = True

    def turn_off(self) -> None:
        self.is_on = False

    def show(self) -> None:
        print(self.is_on)

light_switch = LightSwitch()
other_light_switch = LightSwitch()
light_switch.show()
other_light_switch.show()
light_switch.turn_on()
light_switch.show()
other_light_switch.show()
light_switch.turn_off()
light_switch.show()
other_light_switch.show()