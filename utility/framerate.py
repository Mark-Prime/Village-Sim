import time

def current_time():
    return time.time()

def pause_on_frame(start):
    time.sleep(max(1 - (time.time() - start), 0))