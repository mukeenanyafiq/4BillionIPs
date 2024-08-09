# Python script version of 4BillionIPs written by @mukeenanyafiq

# "I kind of make it overtimized and uh... it almost uses 100% power of your storage."
# "With this kind of power... I recommend you get an SSD instead of HDD."
# - @mukeenanyafiq

import time
import mmap
import os
from multiprocessing import Pool

IP_COUNT = 2**32  # 4 billion IPs
BATCH_SIZE = 10_000_000  # Process 10 million IPs at a time
LOG_INTERVAL = IP_COUNT // 100  # Log progress every 1% completion
filename = "../4BillionIPs.txt"

def int_to_ip(int_ip):
    return f"{(int_ip >> 24) & 0xFF}.{(int_ip >> 16) & 0xFF}.{(int_ip >> 8) & 0xFF}.{int_ip & 0xFF}\n"

def generate_ips(start, end):
    # Generate IPs from start to end and return as a large string
    return ''.join(int_to_ip(i) for i in range(start, end))

def worker_task(args):
    start, end, offset, size = args
    with open(filename, 'r+b') as f:
        mm = mmap.mmap(f.fileno(), length=size, offset=offset)
        mm.write(generate_ips(start, end).encode('utf-8'))
        mm.close()

if __name__ == "__main__":
    start_time = time.time()

    # Calculate the total size needed
    total_size = IP_COUNT * 16  # Each IP takes approximately 15 bytes plus newline
    
    # Pre-allocate the file size
    with open(filename, 'wb') as f:
        f.truncate(total_size)

    pool = Pool()

    tasks = []
    for i in range(0, IP_COUNT, BATCH_SIZE):
        end = min(i + BATCH_SIZE, IP_COUNT)
        offset = i * 16
        size = (end - i) * 16
        tasks.append((i, end, offset, size))

    pool.map(worker_task, tasks)
    pool.close()
    pool.join()

    print(f"IP generation complete and saved to file. ({time.time() - start_time:.3f}s)")