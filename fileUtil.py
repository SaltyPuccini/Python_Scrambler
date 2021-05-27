import numpy
from xlwt import Workbook

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

    @staticmethod
    def save_to_excel(array_of_zero_sequences, array_of_one_sequences, x, y, w, p):
        wb = Workbook()
        sheet1 = wb.add_sheet('Sheet 1')
        #(row, column)
        i = 1

        sheet1.write(1, 0, 0)
        sheet1.write(2, 0, 1)
        while i<70:
            sheet1.write(1, i, array_of_zero_sequences[i])
            sheet1.write(2, i, array_of_one_sequences[i])
            sheet1.write(0, i, i)
            i = i+1

        z = '.xls'
        wb.save("histogram_%s%s%s%s%s" % (x, y, w, p, z))



