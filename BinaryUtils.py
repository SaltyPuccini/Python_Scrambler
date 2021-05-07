class BinaryUtils:
    # tymi rencoma napisany xor
    @staticmethod
    def XOR(a, b):
        return 1 if a + b == 1 else 0

    @staticmethod
    def negate(a):
        return 1 if a == 0 else 0

    # przesuwa rejestr o jeden w prawo
    @staticmethod
    def shift_register_with_feedback(register, feedback):
        register.insert(0, feedback)
        register.pop(-1)

