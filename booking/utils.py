import random
import string


def generate_booking_id(length: int = 8):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))