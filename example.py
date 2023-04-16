# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
from ftdi_bmp3xx import BMP3XX_I2C, BMP3XX_SPI

# I2C setup
#bmp = BMP3XX_I2C()

# SPI setup
bmp = BMP3XX_SPI()

bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2

while True:
    print(
        "Pressure: {:6.4f}  Temperature: {:5.2f}".format(bmp.pressure, bmp.temperature)
    )
    time.sleep(1)
