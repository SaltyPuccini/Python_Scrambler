from ScramblerDVB import ScramblerDVB
from fileUtil import FileUtils
from errorsUtil import BERUtil
from TransmissionSimulator import TransmissionSimulator


def commands(x, y):
    dvb_scrambler = ScramblerDVB()
    simulator = TransmissionSimulator(x, y)
    bits = FileUtils.read_file("piano_test_scrambler.mp3")

    print(len(bits))
    non_scrambled_transmission = simulator.execute_transmission(bits)
    print(len(non_scrambled_transmission))

    dvb_scrambler.perform_dvb_scrambling(bits)
    scrambled_transmission_dvb = simulator.execute_transmission(dvb_scrambler.scrambledSignalDVB)
    print(len(scrambled_transmission_dvb))
    testUtil.count_same_sequences(scrambled_transmission_dvb)

    dvb_scrambler.perform_dvb_descrambling(scrambled_transmission_dvb)

    BERUtil.count_BER(bits, non_scrambled_transmission)
    BERUtil.count_BER(bits, dvb_scrambler.descrambledSignalDVB)


commands(15, 2048)
commands(14, 2048)
commands(13, 2048)
commands(12, 2048)
commands(11, 2048)
commands(10, 2048)

commands(15, 1024)
commands(14, 1024)
commands(13, 1024)
commands(12, 1024)
commands(11, 1024)
commands(10, 1024)

commands(15, 512)
commands(14, 512)
commands(13, 512)
commands(12, 512)
commands(11, 512)
commands(10, 512)

commands(15, 256)
commands(14, 256)
commands(13, 256)
commands(12, 256)
commands(11, 256)
commands(10, 256)
