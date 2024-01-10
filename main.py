import multiprocessing
from file_operations import file_operation
from lock_operations import acquire_lock, release_lock

def main():
    num_procs = 3
    attempts = 5

    manager = multiprocessing.Manager()
    wait_count = manager.Value('i', 0)
    flags = manager.dict({i: 0 for i in range(num_procs)})
    coords = manager.dict({i: 0 for i in range(num_procs)})

    processes = [
        multiprocessing.Process(
            target=file_operation,
            args=(i, attempts, flags, coords, wait_count, acquire_lock, release_lock)
        ) for i in range(num_procs)
    ]

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()

if __name__ == "__main__":
    main()
