from abc import ABCMeta, abstractmethod

class ISueldo:
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self, sueldo=0):
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def setsueldo(self,sueldo):
        self._sueldo=sueldo
