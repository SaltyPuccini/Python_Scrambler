from ScramblerDVB import ScramblerDVB
from ScramblerV34 import ScramblerV34
from TransmissionSimulator import TransmissionSimulator
from errorsUtil import BERUtil
from fileUtil import FileUtils
from testUtil import testUtil
import sys


def test(seq, des, p):

    print('\nsequence length:', seq)
    print('propability of error:', p)
    print('desynchronization length:', des)

    sequence_length = seq
    desynchronization_length = des

    no_scrambler = []
    dvb_scrambler = ScramblerDVB()
    v34_scrambler = ScramblerV34()
    simulator = TransmissionSimulator(seq, des)

    bits = FileUtils.read_file("piano_test_scrambler.mp3")

    print('\nPrzesyłanie bez scramblera:\n')

    no_scrambler = simulator.propability_desynch(bits, p)
    no_scrambler = simulator.execute_transmission(no_scrambler)
    testUtil.count_same_sequences(no_scrambler, sequence_length, desynchronization_length, 'no_scrambler', p)

    BERUtil.count_BER(bits, no_scrambler)
    FileUtils.save_file(no_scrambler, 1)

    print('\nPrzesyłanie, scrambler DVB:\n')

    dvb_scrambler.perform_dvb_scrambling(bits)

    dvb_scrambler.scrambledSignalDVB = simulator.propability_desynch(dvb_scrambler.scrambledSignalDVB, p)
    dvb_scrambler.scrambledSignalDVB = simulator.execute_transmission(dvb_scrambler.scrambledSignalDVB)
    testUtil.count_same_sequences(dvb_scrambler.scrambledSignalDVB, sequence_length, desynchronization_length, 'DVB', p)

    dvb_scrambler.perform_dvb_descrambling(dvb_scrambler.scrambledSignalDVB)

    BERUtil.count_BER(bits, dvb_scrambler.descrambledSignalDVB)
    FileUtils.save_file(dvb_scrambler.descrambledSignalDVB, 2)

    print('\nPrzesyłanie, scrambler v34:\n')

    v34_scrambler.perform_v34_scrambling(bits)

    v34_scrambler.scrambledSignalV34 = simulator.propability_desynch(v34_scrambler.scrambledSignalV34, p)
    v34_scrambler.scrambledSignalV34 = simulator.execute_transmission(v34_scrambler.scrambledSignalV34)
    testUtil.count_same_sequences(v34_scrambler.scrambledSignalV34, sequence_length, desynchronization_length, 'V34', p)

    v34_scrambler.perform_v34_descrambling(v34_scrambler.scrambledSignalV34)

    BERUtil.count_BER(bits, v34_scrambler.descrambledSignalV34)
    FileUtils.save_file(v34_scrambler.descrambledSignalV34, 3)


sys.stdout = open('pomiary.txt', 'w')

test(15, 1024, 0)


sys.stdout.close()
