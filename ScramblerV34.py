#TODO

# from scramblerUtils import ScramblerUtils
#
# class ScramblerV34:
#     def scrambling_v34(self, register, input, output):
#         firstXOR = 0
#         secondXOR = 0
#         eighteenth = register[-1]
#         twentythird = register[-6]
#         firstXOR = ScramblerUtils.XOR(eighteenth, twentythird)
#         secondXOR = ScramblerUtils.XOR(firstXOR, input)
#         ScramblerUtils.shift_register_with_feedback(register, secondXOR)
#         output.append(secondXOR)
#
#     def perform_v34_scrambling(self, inputSignal):
#         v34Register = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0]  # rejestr scramblera
#
#         scrambledSignalv34 = []  # sygnał wyjściowy ze scramblera
#         descrambledSignalv34 = []
#
#         print(inputSignal)
#
#         for i in range(len(inputSignal)):
#             self.scrambling_v34(v34Register, inputSignal[i], scrambledSignalv34)
#
#         print(scrambledSignalv34)
#
#     def perform_v34_descrambling(self, inputSignal):
#         v34Register = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0]
#
#         for i in range(size):
#             self.scrambling_v34(v34Register, scrambledSignalv34[i], descrambledSignalv34)
#         print(descrambledSignalv34)
#         print()
#         count_BER(inputSignal, descrambledSignalv34)