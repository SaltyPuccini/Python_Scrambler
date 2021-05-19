from ScramblerDVB import ScramblerDVB
#from ScramblerV34 import ScramblerV34
from fileUtil import FileUtils
from errorsUtil import BERUtil
from TransmissionSimulator import TransmissionSimulator

dvb_scrambler = ScramblerDVB()
#v34_scrambler = ScramblerV34()
simulator = TransmissionSimulator(15, 1024)
bits = FileUtils.read_file("piano_test_scrambler.mp3")
print(len(bits))

non_scrambled_transmission = simulator.execute_transmission(bits)
print(len(non_scrambled_transmission))

dvb_scrambler.perform_dvb_scrambling(bits)
scrambled_transmission_dvb = simulator.execute_transmission(dvb_scrambler.scrambledSignalDVB)
print(len(scrambled_transmission_dvb))
dvb_scrambler.perform_dvb_descrambling(scrambled_transmission_dvb)

#v34_scrambler.perform_v34_scrambling(bits)
#scrambled_transmission_v34 = simulator.execute_transmission(v34_scrambler.scrambledSignalV34)
#print(len(scrambled_transmission_v34))
#v34_scrambler.perform_v34_descrambling(scrambled_transmission_v34)

BERUtil.count_BER(bits, non_scrambled_transmission)
BERUtil.count_BER(bits, dvb_scrambler.descrambledSignalDVB)
#BERUtil.count_BER(bits, v34_scrambler.descrambledSignalV34)
FileUtils.save_file(non_scrambled_transmission, 1)
FileUtils.save_file(dvb_scrambler.descrambledSignalDVB, 2)
#FileUtils.save_file(v34_scrambler.descrambledSignalV34, 3)


# dvb_scrambler.descrambledSignalDVB[4324] = BinaryUtils.negate(dvb_scrambler.descrambledSignalDVB[4324])
# dvb_scrambler.descrambledSignalDVB[12000] = BinaryUtils.negate(dvb_scrambler.descrambledSignalDVB[12000])
# dvb_scrambler.descrambledSignalDVB[20000] = BinaryUtils.negate(dvb_scrambler.descrambledSignalDVB[20000])
