from ScramblerDVB import ScramblerDVB
from fileUtil import FileUtils
from errorsUtil import BERUtil
from TransmissionSimulator import TransmissionSimulator

dvb_scrambler = ScramblerDVB()
simulator = TransmissionSimulator(15, 1024)
bits = FileUtils.read_file("Nagranie.mp3")
print(len(bits))

non_scrambled_transmission = simulator.execute_transmission(bits)
print(len(non_scrambled_transmission))
dvb_scrambler.perform_dvb_scrambling(bits)
scrambled_transmission = simulator.execute_transmission(dvb_scrambler.scrambledSignalDVB)
print(len(scrambled_transmission))
dvb_scrambler.perform_dvb_descrambling(scrambled_transmission)

BERUtil.count_BER(bits, non_scrambled_transmission)
BERUtil.count_BER(bits, dvb_scrambler.descrambledSignalDVB)
FileUtils.save_file(dvb_scrambler.descrambledSignalDVB)


# dvb_scrambler.descrambledSignalDVB[4324] = BinaryUtils.negate(dvb_scrambler.descrambledSignalDVB[4324])
# dvb_scrambler.descrambledSignalDVB[12000] = BinaryUtils.negate(dvb_scrambler.descrambledSignalDVB[12000])
# dvb_scrambler.descrambledSignalDVB[20000] = BinaryUtils.negate(dvb_scrambler.descrambledSignalDVB[20000])

FileUtils.save_file(dvb_scrambler.descrambledSignalDVB)
