from ScramblerDVB import ScramblerDVB
from TransmissionSimulator import TransmissionSimulator
from errorsUtil import BERUtil
from fileUtil import FileUtils
from testUtil import testUtil

dvb_scrambler = ScramblerDVB()
simulator = TransmissionSimulator(10, 1024)
bits = FileUtils.read_file("piano_test_scrambler.mp3")
#bits = FileUtils.read_file("Nagranie.mp3")

print(len(bits))
non_scrambled_transmission = simulator.execute_transmission(bits)
print(len(non_scrambled_transmission))

dvb_scrambler.perform_dvb_scrambling(bits)
scrambled_transmission_dvb = simulator.execute_transmission(dvb_scrambler.scrambledSignalDVB)
print(len(scrambled_transmission_dvb))

dvb_scrambler.perform_dvb_descrambling(scrambled_transmission_dvb)

BERUtil.count_BER(bits, non_scrambled_transmission)
BERUtil.count_BER(bits, dvb_scrambler.descrambledSignalDVB)

FileUtils.save_file(non_scrambled_transmission, 1)
FileUtils.save_file(dvb_scrambler.descrambledSignalDVB, 2)