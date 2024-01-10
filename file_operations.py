import time

def file_operation(pid, attempts, flags, coords, wait_count, acquire_lock, release_lock):
    fname = "decent.txt"

    for attempt in range(attempts):
        acquire_lock(pid, flags, coords, wait_count)

        try:
            with open(fname, "r+") as f:
                content = f.read().strip()
                counter = int(content) if content else 0
                print(f"P{pid} locked attempt {attempt} -> counter: {counter + 1}.")
                f.seek(0)
                f.write(str(counter + 1))
                f.truncate()
                time.sleep(0.5)
                print(f"P{pid} released the lock.")
        finally:
            release_lock(pid, flags, coords)
            wait_count.value += 1

    print(f"P{pid} took an average of {wait_count.value/attempts:.1f} attempts to access the file.")
