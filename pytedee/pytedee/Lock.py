'''
Created on 02.11.2020

@author: joerg
'''

from enum import Enum


'''class State(Enum):
    Unknown = 0
    Locked = 6
    Unlocked = 2'''

    
class Lock(object):
    '''
    classdocs
    '''

    def __init__(self, name, id):
        '''
        Constructor
        '''
        self._name = name
        self._id = id
        self._state = 0
        self._battery_level = None
        self._is_connected = False
        
    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._id
    
    def is_state_locked(self):
        return self._status == 6
    
    def is_state_unlocked(self):
        return self._status == 2
    
    def get_state(self):
        return self._state
    
    def set_state(self, status):
        self._state = status
        
    def get_battery_level(self):
        return self._battery_level
    
    def set_battery_level(self, level):
        self._battery_level = level
        
    def set_connected(self, connected):
        self._is_connected = connected
    
    def is_connected(self):
        return self._is_connected
