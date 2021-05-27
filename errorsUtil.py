class BERUtil:
    @staticmethod
    def count_BER( inputSignal, descrambledSignal):
        good = 0
        for i in range(len(inputSignal)):
            if descrambledSignal[i] == inputSignal[i]:
                good = good + 1
        print("Success ratio = ", good, "/", len(inputSignal))
        print(good / len(inputSignal) * 100,"%")

class Errors:
    @staticmethod
    def make_error(bit):
        return 0 if bit == 1 else 1
