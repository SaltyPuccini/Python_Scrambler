import numpy

class FileUtils:

    @staticmethod
    def read_file(filename):
        bytes = numpy.fromfile(filename, dtype="uint8")
        bits = numpy.unpackbits(bytes)
        return bits

    @staticmethod
    def save_file(bits, choosen):
        uint8 = numpy.packbits(bits)
        if choosen == 1:
            f = open("piano_no_scramble.mp3", "wb")
        if choosen == 2:
            f = open("piano_dvb.mp3", "wb")
        if choosen == 3:
            f = open("piano_v34.mp3", "wb")
        for b in uint8:
            f.write(b)
        f.close()


