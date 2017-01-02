"""
Represent traits to get
information on an item, or bin
"""

class Entity(object):
  def __init__(self, args=dict()):
    self.used=False
    self.tried=False
    for k,v in args.iteritems():
      setattr(self, k, v)
    """ if we have an id use it otherwise generate one """
    if not "id" in args.keys():
       from .helpers import get_a_binner_id
       setattr(self, "id", get_a_binner_id())
    self.slots = []
    self.items = []
