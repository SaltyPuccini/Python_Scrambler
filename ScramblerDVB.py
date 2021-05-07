from BinaryUtils import BinaryUtils

class ScramblerDVB:
    def __init__(self):
        self.dvbRegister = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.scrambledSignalDVB = []
        self.descrambledSignalDVB = []

    def perform_dvb_scrambling(self, signal):
        self.dvbRegister = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(signal)):
            scrambling_dvb(self.dvbRegister, signal[i], self.scrambledSignalDVB)

    def perform_dvb_descrambling(self, signal):
        self.dvbRegister = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(signal)):
            scrambling_dvb(self.dvbRegister, signal[i], self.descrambledSignalDVB)



def scrambling_dvb(register, input, output):
    firstXOR = 0
    secondXOR = 0

    fifteenth = register[-1]
    fourteenth = register[-2]

    # dwa xory - pierwszy to xor z piętnastego i czternastego miejsca w rejestrze, drugi z otrzymanego wyniku i inputu
    firstXOR = BinaryUtils.XOR(fifteenth, fourteenth)
    secondXOR = BinaryUtils.XOR(input, firstXOR)
    # na początek rejestru idzie pierwszy xor, rejestr jest przesuwany
    BinaryUtils.shift_register_with_feedback(register, firstXOR)
    # do outputu idzie wynik drugiego xora
    output.append(secondXOR)