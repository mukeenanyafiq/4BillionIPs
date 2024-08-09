# Python script version of 4BillionIPs written by @mukeenanyafiq

import time
IP_COUNT = 2**32  # 4 billion IPs
BATCH_SIZE = 1000000  # Write 1 million IPs at a time
LOG_INTERVAL = IP_COUNT // 100  # Log progress every 1% completion
filename = "../4BillionIPs.txt"

def int_to_ip(int_ip):
    return f"{(int_ip >> 24) & 0xFF}.{(int_ip >> 16) & 0xFF}.{(int_ip >> 8) & 0xFF}.{int_ip & 0xFF}"

start = time.time()  # Record execution time

with open(filename, 'w') as file:
    buffer = []

    for i in range(IP_COUNT):
        buffer.append(int_to_ip(i))

        # If buffer size reaches BATCH_SIZE, write to file
        if len(buffer) == BATCH_SIZE:
            file.write("\n".join(buffer) + "\n")
            buffer = []  # Clear the buffer

        # Log progress at intervals
        if i > 0 and i % LOG_INTERVAL == 0: print(f"[Progress] Generated {i:,}/{IP_COUNT:,} IPs ({(i / IP_COUNT) * 100:.2f}%)")

    # Write any remaining IPs in the buffer to the file
    if buffer: file.write("\n".join(buffer) + "\n")

print(f"IP generation complete and saved to file. ({time.time() - start:.2f}s)")