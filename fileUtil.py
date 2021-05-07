import numpy

class FileUtils:

    @staticmethod
    def read_file(filename):
        bytes = numpy.fromfile(filename, dtype="uint8")
        bits = numpy.unpackbits(bytes)
        return bits

    @staticmethod
    def save_file( bits):
        uint8 = numpy.packbits(bits)
        f = open("saved.mp3", "wb")
        for b in uint8:
            f.write(b)
        f.close()


