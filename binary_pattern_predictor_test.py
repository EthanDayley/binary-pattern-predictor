#!/usr/bin/python3

from predictor_lib.neuron import Neuron
from predictor_lib.synapse import Synapse

from random import random
import threading

class BinaryPatternGenerator1:
    def __next__(self):
        self._index = (self._index + 1) % len(self._pattern)
        return self._pattern[self._index]

    def __iter__(self):
        '''
        This class creates a binary pattern like the following:
        011011011011011...
        NOTE: it is designed to be used as an iterable
        '''
        self._index = 0
        self._pattern = [0, 1, 1]
        return self

print("STARTING...")

OUTPUT_FILE = "output.csv"          # file to which we'll output the values of the last row of neurons
OUTPUT_FREQUENCY = 10               # frequency with which we'll write to the output file

NUM_NEURONS_IN_ROW = 10             # number of neurons in each row except the last
NUM_NEURONS_LAST_ROW = 10           # number of neurons in the last row
NUM_HIDDEN_ROWS = 8                # number of "hidden layers"

MAX_INITIAL_SYNAPTIC_STRENGTH = 5   # max value for initial random synaptic strength

NUM_ITERATIONS = 50                # number of times we will send input into the network


# SETUP
# TODO: rearrange this whole thing. I'm pretty sure it runs in O(N^N) or something.
INPUT_NEURON = Neuron()         # the initial neuron in the network
# make it thinks it has an incoming synapse so it will fire
INPUT_NEURON.add_incoming_synapse()

network = []

print("Creating Neurons...")

# create the rows of neurons
for row_index in range(NUM_HIDDEN_ROWS):
    row = []
    for col_index in range(NUM_NEURONS_IN_ROW):
        row.append(Neuron())
    network.append(row)
row = []
for col_index in range(NUM_NEURONS_LAST_ROW):
    row.append(Neuron())
network.append(row)

# create the synaptic connections between these rows

print("Connecting layers...")

# start with the first row, connecting them all to the input neuron
for neuron in network[0]:
    INPUT_NEURON.add_outgoing_synapse(Synapse(outgoing_neuron=neuron, synaptic_strength = random() * MAX_INITIAL_SYNAPTIC_STRENGTH))

# now connect the hidden layers
for row_index in range(0,NUM_HIDDEN_ROWS-1):
    for input_col_index in range(NUM_NEURONS_IN_ROW):
        for output_col_index in range(NUM_NEURONS_IN_ROW):
            network[row_index][input_col_index].\
                    add_outgoing_synapse(Synapse(outgoing_neuron=network[row_index+1][output_col_index],
                    synaptic_strength=random() * MAX_INITIAL_SYNAPTIC_STRENGTH))


print("Starting Compute Process...")

def send_initial_impulse(synapse):
    '''
    function sends an impulse through a synapse
    '''
    synapse.send_impulse()


# START PROCESS
binary_iterable = iter(BinaryPatternGenerator1())
for iteration in range(NUM_ITERATIONS):
    raw_pattern_output = next(binary_iterable)
    # encode raw pattern output
    if raw_pattern_output == 0:
        pattern_output = 0.5
    elif raw_pattern_output == 1:
        pattern_output = 1
    else:
        raise RuntimeError('Bad pattern output %f' % raw_pattern_output)

    # send impulse to input neuron
    INPUT_NEURON.receive_impulse(pattern_output)

    # # send impulses to first layer
    # for col_index in range(NUM_NEURONS_IN_ROW):
    #     threading.Thread(target=lambda: INPUT_NEURON.outgoing_synapses[col_index].send_impulse()).start()

    if iteration % OUTPUT_FREQUENCY == 0:
        for row in network:
            for neuron in row:
                if neuron._fired:
                    print('X ', end='')
                else:
                    print('  ', end='')
            print()
        print('='*90)