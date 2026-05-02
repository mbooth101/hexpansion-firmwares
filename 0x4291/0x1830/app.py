import app
import neopixel
import asyncio
from patterns.rainbow import RainbowPattern


class RainbowUK(app.App):
    def __init__(self, config=None):
        self.config = config
        self.leds = neopixel.NeoPixel(config.pin[3], 78)
        self.pattern = RainbowPattern()


    def update(self, delta=None):
        self.minimise()

    async def background_task(self):
        while True:
            frame = self.pattern.next()
            for i, val in enumerate(frame*7):
                if i > 78:
                    break
                self.leds[i] = tuple(int(c * 0.05) for c in val)
            self.leds.write()
            await asyncio.sleep(1/self.pattern.fps)

__app_export__ = RainbowUK
