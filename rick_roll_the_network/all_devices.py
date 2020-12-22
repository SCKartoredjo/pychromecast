#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time
import pychromecast
from pprint import pprint
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)

# Get all chromecasts on network
divices_on_network = [i[3] for i in services]
all_chromecasts = [pychromecast.get_listed_chromecasts(friendly_names=[name]) for name in divices_on_network]
cast_all = [i[0][0] for i in all_chromecasts]
let_them_wait = [i.wait() for i in cast_all]

repeats = 5
stop = time.time()+(212*repeats)

while stop > time.time():
    for this_device in cast_all:
        yt = YouTubeController()
        this_device.register_handler(yt)
        yt.play_video("dQw4w9WgXcQ")

pychromecast.discovery.stop_discovery(browser)

