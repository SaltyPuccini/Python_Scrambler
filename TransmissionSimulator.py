from BinaryUtils import BinaryUtils
import random
import time


class TransmissionSimulator:
    def __init__(self, num_of_bits_to_desync, length_of_desync):
        self.num_of_bits_to_desync = num_of_bits_to_desync
        self.length_of_desync = length_of_desync

    def execute_transmission(self, bits):
        temp = []
        is_zero = True
        is_desync = False
        transmitted_bits = []
        number_of_desyncs = 0
        time_in_desync = 0
        start_of_desync = 0
        end_of_desync = 0
        desync_bits_counter = 0

        start_of_transmission = time.perf_counter()
        for b in bits:

            if len(temp) == self.num_of_bits_to_desync and not is_desync:
                temp = []
                is_desync = True
                number_of_desyncs = number_of_desyncs + 1
                start_of_desync = time.perf_counter()

            if desync_bits_counter == self.length_of_desync:
                desync_bits_counter = 0
                is_desync = False
                end_of_desync = time.perf_counter()
                time_in_desync = time_in_desync + (end_of_desync - start_of_desync)

            if is_desync:
                b = BinaryUtils.XOR(b, random.randint(0, 2))
                transmitted_bits.append(b)
                desync_bits_counter = desync_bits_counter + 1

            if not is_desync:
                transmitted_bits.append(b)
                if is_zero and b == 0:
                    temp.append(0)
                if not is_zero and b == 0:
                    is_zero = True
                    temp = [0]
                if not is_zero and b == 1:
                    temp.append(1)
                if is_zero and b == 1:
                    is_zero = False
                    temp = [1]

        end_of_transmission = time.perf_counter()
        time_of_transmission = end_of_transmission - start_of_transmission

        print(f"Number of desyncs: {number_of_desyncs}")
        print(f"Time system was desynchronized: {time_in_desync}")
        print(f"Time of whole transmission: {time_of_transmission}")
        print(f"Quality of transmission is: {self.calculate_quality_of_sync_in_system(time_of_transmission, time_in_desync) *100}%")

        return transmitted_bits

    def calculate_quality_of_sync_in_system(self, whole_time, time_in_desync):
        time_in_sync = whole_time - time_in_desync
        quality = time_in_sync / whole_time
        return quality