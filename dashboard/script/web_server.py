import os.path as osp
import logging
import sys

class MLDashClient(object):
    def __init__(self,dump_dir):
        self.dump_dir = dump_dir
        self.desc = None
        self.expr = None
        self.run = None
    
    def _refresh(self):
        self.desc = None