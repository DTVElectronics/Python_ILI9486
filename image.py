from PIL import Image
import RPi.GPIO as GPIO
import spidev as SPI
import time
import ILI9486 as LCD
import config


if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        lcd = LCD.ILI9486(dc=config.DC_PIN, rst=config.RST_PIN, spi=SPI.SpiDev(config.SPI_BUS, config.SPI_DEVICE))
        lcd.begin()

        print('Loading image...')
        image = Image.open('sample.png')

        while True:
            print('Drawing image')
            lcd.display(image)
            time.sleep(1)
            print('Turning on inverted mode')
            lcd.invert()
            time.sleep(1)
            print('Turning off inverted mode')
            lcd.invert(False)
            time.sleep(1)
            print('Turning off display')
            lcd.off()
            time.sleep(1)
            print('Turning on display')
            lcd.on()
            time.sleep(1)
            print('Turning on idle mode')
            lcd.idle()
            time.sleep(1)
            print('Turning off idle mode')
            lcd.idle(False)
            time.sleep(1)
            print('Clearing display')
            lcd.clear()
            lcd.display()
            time.sleep(1)
            print('Resetting display')
            lcd.begin()
            time.sleep(1)

    except KeyboardInterrupt:
        # catching keyboard interrupt to exit, but do the cleanup in finally block
        pass
    finally:
        GPIO.cleanup()
