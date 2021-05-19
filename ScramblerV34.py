from BinaryUtils import BinaryUtils

class ScramblerV34:
    def __init__(self):
       self.v34Register = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0]
       self.scrambledSignalV34 = []
       self.descrambledSignalV34 = []

    def perform_v34_scrambling(self, signal):
        self.v34Register = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0]
        for i in range(len(signal)):
            scrambling_v34(self.v34Register, signal[i], self.scrambledSignalV34)

    def perform_v34_descrambling(self, signal):
        self.v34Register = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0]
        for i in range(len(signal)):
            scrambling_v34(self.v34Register, signal[i], self.descrambledSignalV34)


def scrambling_v34(register, input, output):
    firstXOR = 0
    secondXOR = 0

    eighteenth = register[-1]
    twentythird = register[-6]

    firstXOR = BinaryUtils.XOR(eighteenth, twentythird)
    secondXOR = BinaryUtils.XOR(firstXOR, input)

    BinaryUtils.shift_register_with_feedback(register, secondXOR)

    output.append(secondXOR)