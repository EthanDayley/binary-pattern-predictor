#!/usr/bin/python3

from neuron import Neuron

'''
This module contains the SynapticConnection class definition
'''
class SynapticConnection:
    def send_impulse(self) -> None:
        '''
        Sends value of synaptic_strength to the outgoing neuron
        '''
        self.outgoing_neuron.receive_impulse(self.synaptic_strength)

    def __init__(self, outgoing_neuron: Neuron, synaptic_strength: float):
        '''
        This class represents a synaptic connection between two neurons
        '''
        self.outgoing_neuron: Neuron = outgoing_neuron
        self.synaptic_strength: float = synaptic_strength