lazy import os
from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, agencia, conta, saldo):
        ...