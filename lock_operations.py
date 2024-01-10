import time

def acquire_lock(pid, flags, coords, wait_count):
    coords[pid] = 1

    while sum(coords.values()) <= len(coords) // 2:
        time.sleep(0.1)

    flags[pid] = 1

def release_lock(pid, flags, coords):
    flags[pid] = 0
    coords[pid] = 0
