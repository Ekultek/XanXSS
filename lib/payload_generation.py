import random

import lib.settings


class PayloadGeneration(object):

    """
    load the payloads into a set
    """

    def __init__(self, templates, amount=10):
        self.templates = templates
        self.amount = amount

    def create_tampers(self):
        return lib.settings.load_tampers()

    def obfuscate_tampers(self, tampers):
        retval = set()
        for _ in range(self.amount):
            payload = random.choice(self.templates)
            for tamper in tampers:
                if tamper is not None:
                    payload = tamper.tamper(payload)
            retval.add(payload)
        return retval
