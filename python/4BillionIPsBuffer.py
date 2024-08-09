# Python script version of 4BillionIPs written by @mukeenanyafiq

# This script will generate 4 billion IPs in your RAM, and then letting it all off on a file
# 64+ GBs of RAM are probably required.

import time
IP_COUNT = 2**32  # 4 billion IPs
BATCH_SIZE = 1000000  # Write 1 million IPs at a time
LOG_INTERVAL = IP_COUNT // 100  # Log progress every 1% completion
filename = "../4BillionIPs.txt"

def int_to_ip(int_ip):
    return f"{(int_ip >> 24) & 0xFF}.{(int_ip >> 16) & 0xFF}.{(int_ip >> 8) & 0xFF}.{int_ip & 0xFF}"

start = time.time()  # Record execution time

with open(filename, 'w') as file:
    ipBuffer = []  # Use a buffer to store IPs

    for i in range(IP_COUNT):
        ipBuffer.append(int_to_ip(i))

        # Log progress at intervals
        if i % LOG_INTERVAL == 0: print(f"[Progress] Generated {i:,}/{IP_COUNT:,} IPs ({(i / IP_COUNT) * 100:.2f}%)")

    # Write the generated IPs to the file
    file.write("\n".join(buffer))

print(f"IP generation complete and saved to file. ({time.time() - start:.2f}s)")