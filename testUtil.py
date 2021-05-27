from fileUtil import FileUtils

class testUtil:

    @staticmethod
    def count_same_sequences(bits, x, y, w, p):
        array_of_zero_sequences = [0 for x in range(100)]
        array_of_one_sequences = [0 for x in range(100)]
        last_el = -1
        curr_length = 0
        for b in bits:

            if b == last_el:
                curr_length=curr_length + 1

            if b != last_el:
                if last_el == 0:
                    array_of_zero_sequences[curr_length] = array_of_zero_sequences[curr_length] + 1

                if last_el == 1:
                    array_of_one_sequences[curr_length] = array_of_one_sequences[curr_length] + 1

                last_el = b
                curr_length = 1
        FileUtils.save_to_excel(array_of_zero_sequences, array_of_one_sequences, x, y, w, p)