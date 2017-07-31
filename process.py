#!/usr/bin/env python
import os
import time
import blinkt
import redis

blinkt.set_clear_on_exit()
blinkt.set_brightness(1)

r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=0)
for x in range(blinkt.NUM_PIXELS):
    r.hmset('blinkt_light_state:' + str(x), {'r': 0, 'g': 0, 'b': 0});

itercount = 0;

while True:
    itercount += 1
    for x in range(blinkt.NUM_PIXELS):
        dict = r.hgetall('blinkt_light_state:' + str(x));
#       print "%d: Setting pixel %d to RGB (%d,%d,%d)" % (itercount, x, float(dict['r']), float(dict['g']), float(dict['b']))
        blinkt.set_pixel(x, float(dict['r']), float(dict['g']), float(dict['b']))
    blinkt.show()
#   print ""
    time.sleep(0.5)