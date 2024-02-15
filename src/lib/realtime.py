from time import localtime, time


UTC_OFFSET = -5 * 60 * 60  # EST


def realtime():
    return localtime(time() + UTC_OFFSET)
