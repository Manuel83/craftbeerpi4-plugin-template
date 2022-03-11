
# -*- coding: utf-8 -*-
import os
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *

logger = logging.getLogger(__name__)


class CustomWebExtension(CBPiExtension):

    @request_mapping(path="/", auth_required=False)
    async def hello_world(self, request):
        return web.HTTPFound('static/index.html')

    def __init__(self, cbpi):
        self.cbpi = cbpi
        path = os.path.dirname(__file__)
        self.cbpi.register(self, "/cbpi_uiplugin", static=os.path.join(path, "static"))


@parameters([])
class CustomSensor(CBPiSensor):
    
    def __init__(self, cbpi, id, props):
        super(CustomSensor, self).__init__(cbpi, id, props)
        self.value = 0

    @action(key="Test", parameters=[])
    async def action1(self, **kwargs):
        print("ACTION!", kwargs)

    async def run(self):
        while self.running is True:
            self.value = random.randint(0,50)
            self.push_update(self.value)
            await asyncio.sleep(1)
    
    def get_state(self):
        return dict(value=self.value)

@parameters([])
class CustomActor(CBPiActor):

    @action("action", parameters={})
    async def action(self, **kwargs):
        print("Action Triggered", kwargs)
        pass
    
    def on_start(self):
        self.state = False
        pass

    async def on(self, power=0):
        logger.info("ACTOR 1111 %s ON" % self.id)
        self.state = True

    async def off(self):
        logger.info("ACTOR %s OFF " % self.id)
        self.state = False

    def get_state(self):
        return self.state
    
    async def run(self):
        pass


def setup(cbpi):
    #cbpi.plugin.register("MyCustomActor", CustomActor)
    #cbpi.plugin.register("MyCustomSensor", CustomSensor)
    #cbpi.plugin.register("MyustomWebExtension", CustomWebExtension)
    pass
