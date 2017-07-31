#!/usr/bin/env python
import os
import time
import blinkt
import redis

blinkt.set_clear_on_exit()
blinkt.set_brightness(1)

r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=0)
for x in range(blinkt.NUM_PIXELS):
    r.hmset('blinkt_light_state:' + str(x), {'r': 0, 'g': 0, 'b': 0, 'bri': 1, 'mode': 'none'});

iter = 0;

while True:
    iter += 1
    for x in range(blinkt.NUM_PIXELS):
        dict = r.hgetall('blinkt_light_state:' + str(x));
        if dict['mode'] == "flashing":
            if iter % 2 == 0:
                blinkt.set_pixel(x, float(dict['r']), float(dict['g']), float(dict['b']), float(dict['bri']))
            else:
                blinkt.set_pixel(x, 0,0,0,0)
        else:
            blinkt.set_pixel(x, float(dict['r']), float(dict['g']), float(dict['b']), float(dict['bri']))
    blinkt.show()
    time.sleep(0.5)
