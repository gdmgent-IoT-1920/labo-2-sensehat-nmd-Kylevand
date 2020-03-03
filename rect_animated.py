from sense_hat import SenseHat
from time import sleep

sense = SenseHat()



while True:

    g = (0, 0, 0)
    b = (255, 255, 255)

    rectang1 = [
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, g, g, b, b, b,
        b, b, b, g, g, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b
    ]

    rectang2 = [
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, g, g, g, g, b, b,
        b, b, g, b, b, g, b, b,
        b, b, g, b, b, g, b, b,
        b, b, g, g, g, g, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b
    ]

    rectang3 = [
        b, b, b, b, b, b, b, b,
        b, g, g, g, g, g, g, b,
        b, g, b, b, b, b, g, b,
        b, g, b, b, b, b, g, b,
        b, g, b, b, b, b, g, b,
        b, g, b, b, b, b, g, b,
        b, g, g, g, g, g, g, b,
        b, b, b, b, b, b, b, b
    ]

    rectang4 = [
        g, g, g, g, g, g, g, g,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        g, g, g, g, g, g, g, g
    ]







    sense.set_pixels(rectang1)
    sleep(0.5)
    sense.set_pixels(rectang2)
    sleep(0.5)
    sense.set_pixels(rectang3)
    sleep(0.5)
    sense.set_pixels(rectang4)
    sleep(0.5)
    sense.set_pixels(rectang3)
    sleep(0.5)
    sense.set_pixels(rectang2)
    sleep(0.5)
    sense.set_pixels(rectang1)