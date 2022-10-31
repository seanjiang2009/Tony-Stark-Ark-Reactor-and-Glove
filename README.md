# Tony-Stark-Ark-Reactor-and-Glove

3D resin printing for Tony Stark's ark reactor and Iron Man's gloves. Code for how to make a breathing light pattern using Python and Thonny for Raspberry Pi Pico.


## Ark Reactor

### Materials:
1. link for 3D printer
2. link for resin printing material
3. link for Raspberry Pi Pico
4. link for battery pack
5. link to ark reactor design
6. link to blue filter paper
7. link to car light

### Methods:
1. once it is finished 3D printing don't put transparent piece of ark reactor under UV light for additional curing
2. put face plate of ark reactor under UV light for additional curing
3. put the car light into the transparent piece
4. create a strap that fits and can go into the holes of the transparent piece which you will wear
5. cut a circle of the blue filter paper and place it inbetween the transparent piece and the face plate to alter the color of the ark reactor

#### Code for breathing light pattern:
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

#### Wiring Scheme:

## Gloves
### Materials:
link to 3D printing for the palm, backhand plate, and finger knuckles
link to the metallic red spray paint
hot glue gun
link to fabric gloves

### Methods:

#### Spray Paint:
1. get wooden skewers
2. get any large cardboard box
3. wrap the skewers with foam or paper towels or anything that can hold the pieces of the palm in place as shown in the image
4. stab the wrapped skewers with the knuckles on them into the box
5. choose a good place to start spray painting
6. do 2 or 3 layers of painting make sure that you didn't miss any visible spots

#### Wiring Scheme:
1. hot glue the transparent palm piece where your LED lights will go (make sure that it is firmly in place)
2. hot glue in the wires of the LED lights to the inside of the palm piece to reduce movement of the wires
3. solder batteries to clipped pieces of male wire ends for extra sturdiness of the battery

#### Glove Assembly
10. get any fabric glove (preferably thin) and begin to hot glue the knuckles and the backhand plate to the glove in the appropriate places (a map will be provided) (you do not need to hot glue the palm of the hand because the thickness of the knucle pieces will keep it in place) (glue the bottom-inside of the knucles, to the palm side of your fingers) (DO NOT glue the knuckles to the backhand side of your fingers) (it might be helpful to wear an extra layer of gloves that can be removeable to avoid being burned by the hot glue) (adding too much hot glue will result in smudges)
11. let the hot glue dry and set in
