# author: Matthias Dellweg
# (c) 2017

import re
import logging
import sys
import subprocess


def sop_plugin():
    return QrUrl()


class QrUrl:
    match_pattern = r"https?://.*"

    def __init__(self):
        self.matcher = re.compile(self.match_pattern)
        logging.debug("QrUrl aktiviert")

    def handle(self, message):
        match = self.matcher.match(message)
        if match:
            subprocess.run(['sensible-browser', message])
            return True
        return False
