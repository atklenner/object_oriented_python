class Television:
    def __init__(self) -> None:
        self.is_on = False
        self.is_muted = False
        self.channel_list = [3, 4, 6, 8, 10, 11, 12, 13]
        self.current_channel_index = 0
        self.volume_levels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.current_volume_index = 0

    def power(self):
        self.is_on = not self.is_on

    def volume_up(self):
        if self.is_on:
            if self.is_muted:
                self.is_muted = False
            if self.current_volume_index < len(self.volume_levels):
                self.current_volume_index += 1

    def volume_down(self):
        if self.is_on:
            if self.is_muted:
                self.is_muted = False
            if self.current_volume_index > 0:
                self.current_volume_index -= 1

    def mute(self):
        if self.is_on:
            self.is_muted = not self.is_muted

    def channel_up(self):
        if self.is_on:
            # allows the channel index to wrap around
            self.current_channel_index = (self.current_channel_index + 1) % len(self.channel_list)

    def channel_down(self):
        if self.is_on:
            # allows the channel index to wrap around
            self.current_channel_index = (self.current_channel_index - 1) % len(self.channel_list)

    def set_channel(self, new_channel):
        if self.is_on:
            if new_channel in self.channel_list:
                self.current_channel_index = self.channel_list.index(new_channel)

    def show(self):
        if self.is_on:
            print("current channel:", self.channel_list[self.current_channel_index])
            if self.is_muted:
                print("TV is muted")
            else:
                print("current volume:", self.volume_levels[self.current_volume_index])
        else:
            print("TV is off")

tv = Television()

tv.power()
tv.show()

tv.channel_up()
tv.channel_up()
tv.volume_up()
tv.volume_up()
tv.show()

tv.power()
tv.show()
tv.power()
tv.show()

tv.volume_down()
tv.mute()
tv.show()

tv.set_channel(11)
tv.mute()
tv.show()

Television.power(tv)
Television.show(tv)