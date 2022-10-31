from machine import Pin,PWM
from time import sleep
led = PWM(Pin(21))
led.freq(1000)

cycle_time = 2 #adjust this to change the cycle time

led_speed = 500 #increase per frame
max_led_value = 65535
base_led_value = 0
cycle_number = int(max_led_value/led_speed)
#cycle_time = sleep_time * cycle_number
sleep_time = cycle_time/cycle_number

while True:
    for x in range (cycle_number):
        led.duty_u16(base_led_value + x*led_speed)
        sleep(sleep_time)
    for x in range (cycle_number):
        led.duty_u16(max_led_value + x*(-led_speed))
        sleep(sleep_time)
