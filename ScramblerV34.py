from BinaryUtils import BinaryUtils

class ScramblerV34:
    def __init__(self):
       self.v34Register = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
       self.scrambledSignalV34 = []
       self.descrambledSignalV34 = []

    def perform_v34_scrambling(self, signal):
        for i in range(len(signal)):
            scrambling_v34(self.v34Register, signal[i], self.scrambledSignalV34)

    def perform_v34_descrambling(self, signal):
        for i in range(len(signal)):
            descrambling_v34(self.v34Register, signal[i], self.descrambledSignalV34)


def scrambling_v34(register, input, output):
    firstXOR = 0
    secondXOR = 0

    eighteenth = register[-6]
    twentythird = register[-1]

    firstXOR = BinaryUtils.XOR(eighteenth, twentythird)
    secondXOR = BinaryUtils.XOR(firstXOR, input)

    BinaryUtils.shift_register_with_feedback(register, secondXOR)

    output.append(secondXOR)

def descrambling_v34(register, input, output):
        firstXOR = 0
        secondXOR = 0

        eighteenth = register[-6]
        twentythird = register[-1]

        firstXOR = BinaryUtils.XOR(eighteenth, twentythird)
        secondXOR = BinaryUtils.XOR(firstXOR, input)

        BinaryUtils.shift_register_with_feedback(register, input)

        output.append(secondXOR)