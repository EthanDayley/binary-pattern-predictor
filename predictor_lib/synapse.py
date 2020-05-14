#!/usr/bin/python3


'''
This module contains the Synapse class definition
'''
class Synapse:
    def __str__(self) -> str:
        return '<Synapse, synaptic_strength: %f>' % self.synaptic_strength

    def __repr__(self) -> str:
        return self.__str__()

    def send_impulse(self) -> None:
        '''
        Sends value of synaptic_strength to the outgoing neuron
        '''
        self.outgoing_neuron.receive_impulse(self.synaptic_strength)

    def __init__(self, outgoing_neuron, synaptic_strength: float):
        '''
        This class represents a synaptic connection between two neurons
        '''
        self.outgoing_neuron = outgoing_neuron                  # outgoing Neuron
        self.synaptic_strength: float = synaptic_strength

        # tell the next neuron that we connected to it
        self.outgoing_neuron.add_incoming_synapse()