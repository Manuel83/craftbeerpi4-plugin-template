import os

import logging
from unittest.mock import MagicMock, patch

from cbpi.api import *

logger = logging.getLogger(__name__)

@parameters([])
class CustomActor(CBPiActor):

    @action("action", parameters={})
    async def action(self, **kwargs):
        print("ACTION!", kwargs)
        pass
    
    def init(self):
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
    print("###### SETUP PLUGIN #####")
    
