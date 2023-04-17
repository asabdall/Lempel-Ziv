import random

def random_bit_generator(message_size):
    """
    Generates a random bitstream of a given size.

    Parameters:
        message_size (int): The size of the message to generate.

    Returns:
        A string representing the generated bitstream.
    """
    bitstream = ""

    # Generate a random decimal number for each bit in the message
    for i in range(0, message_size):
        random_decimal = random.random()

        # If the random number is greater than 0.5, add a "1" bit to the bitstream, otherwise add a "0" bit
        if random_decimal > 0.5:
            added_bit = "1"
        else:
            added_bit = "0"

        bitstream += added_bit

    return bitstream
