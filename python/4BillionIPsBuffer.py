# Python script version of 4BillionIPs written by @mukeenanyafiq

# This script will generate 4 billion IPs in your RAM, and then letting it all off on a file which would took a while
# 64+ GBs of RAM are probably required.

import time
IP_COUNT = 2**32  # 4 billion IPs
BATCH_SIZE = 10_000_000  # Process 10 million IPs at a time
LOG_INTERVAL = IP_COUNT // 100  # Log progress every 1% completion
filename = "../4BillionIPs.txt"

def int_to_ip(int_ip):
    return f"{(int_ip >> 24) & 0xFF}.{(int_ip >> 16) & 0xFF}.{(int_ip >> 8) & 0xFF}.{int_ip & 0xFF}"

start = time.time()  # Record execution time

def generate_ips():
    start_time = time.time()
    ip_list = []

    for i in range(IP_COUNT):
        ip_list.append(int_to_ip(i))

        # Log progress at intervals
        if (i + 1) % LOG_INTERVAL == 0:
            elapsed_time = time.time() - start
            print(f"[Progress] Generated {i + 1:,}/{IP_COUNT:,} IPs ({(i + 1) / IP_COUNT * 100}%) in {elapsed_time:.3f} seconds")

        # Chunk processing
        if (i + 1) % BATCH_SIZE == 0: print(f"[Progress] Reached {i + 1:,} IPs; continuing to generate...")

    # Write all IPs to the file in one go
    with open(filename, 'w') as file:
        file.write("\n".join(ip_list))

    print(f"IP generation complete and saved to file in {time.time() - start:.3f} seconds.")

if __name__ == "__main__":
    generate_ips()