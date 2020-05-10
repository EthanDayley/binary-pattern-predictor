#!/usr/bin/python3

'''
This module contains the Neuron class definition
'''

from synaptic_connection import SynapticConnection

class Neuron:
    def receive_impulse(self, impulse_value: float) -> None:
        '''
        This method receives an impulse value from another neuron
        '''
        self._impulses_received.append(impulse_value)
    
    def fire(self) -> None:
        '''
        This method sends an impulse along all outgoing synaptic connections
        '''
        for synapse in self.synapses_outgoing:
            synapse.send_impulse()
    
    def connect_previous_neuron(self, neuron: Neuron) -> None:
        '''
        This method connects a previous neuron
        (one that will send INPUTS to this one)
        to the neuron
        '''
        self._num_previous_neurons += 1

    def __init__(self, synapses_outgoing=[], threshold=1):
        '''
        This class represents a neuron within the neural network
        Don't judge.
        '''
        self.synapses_outgoing = synapses_outgoing      # list of outgoing synaptic connections
        self.threshold = threshold                      # threshold for firing

        self._impulses_received = []                    # list of all impulses received from other neurons
        self._num_previous_neurons = 0                  # number of neurons giving inputs to this one