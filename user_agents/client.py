import json
import os

class UserAgent(object):

    def __init__(self):
        self.data = []
        with open('{}/data.json'.format(os.path.dirname(os.path.abspath(__file__)))) as f:
            self.data = json.load(f)

    def random(self):
        if self.data.length > 0:
            return self.data[range(0, self.data.length)]
        else:
            return None
