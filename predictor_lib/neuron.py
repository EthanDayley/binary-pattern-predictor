#!/usr/bin/python3

'''
This module contains the Neuron class definition
'''

class Neuron:
    def __str__(self) -> str:
        return '<Neuron, incoming_synapses: %d, outgoing_synapses: %d, threshold: %f>' % (
            self._num_incoming_synapses, len(self.outgoing_synapses), self.threshold
        )

    def __repr__(self) -> str:
        return self.__str__()

    def receive_impulse(self, impulse_value: float) -> None:
        '''
        This method receives an impulse value from another neuron
        '''
        self._impulses_received.append(impulse_value)
        if len(self._impulses_received) == self._num_incoming_synapses and sum(self._impulses_received) >= self.threshold:
            self.fire()
            self._fired = True
        else:
            self._fired = False

    def fire(self) -> None:
        '''
        This method sends an impulse along all outgoing synaptic connections
        '''
        for synapse in self.outgoing_synapses:
            synapse.send_impulse()
        self._impulses_received = []

    def add_incoming_synapse(self) -> None:
        '''
        This method connects an incoming synapse
        (one that will send INPUTS to this one)
        to the neuron
        '''
        self._num_incoming_synapses += 1

    def add_outgoing_synapse(self, outgoing_synapse) -> None:
        '''
        Adds an outgoing synapse
        '''
        self.outgoing_synapses.append(outgoing_synapse)

    def __init__(self, threshold=1):
        '''
        This class represents a neuron within the neural network
        Don't judge.
        '''
        self.outgoing_synapses = []                     # list of outgoing synaptic connections
        self.threshold = threshold                      # threshold for firing

        self._impulses_received = []                    # list of all impulses received from other neurons
        self._num_incoming_synapses = 0                 # number of neurons giving inputs to this one

        self._fired = False