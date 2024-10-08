-- This script is only compatible for Lua 5.3+
-- Lua script version of 4BillionIPs written by @mukeenanyafiq

-- This script will generate 4 billion IPs in your RAM, and then letting it all off on a file which would took a while
-- 64+ GBs of RAM are probably required.

local IP_COUNT = 2^32 -- 4 billion IPs
local BATCH_SIZE = 10000000; -- Process 10 million IPs at a time
local LOG_INTERVAL = math.floor(IP_COUNT / 100) -- Log progress every 1% completion
local filename = "../4BillionIPs.txt"

local start = os.time() -- Record execution time

local function intToIP(int)
    return string.format("%d.%d.%d.%d",
        (int >> 24) & 0xFF,
        (int >> 16) & 0xFF,
        (int >> 8) & 0xFF,
        int & 0xFF)
end

local ipBuffer = {} -- Use a buffer to store the IPs
local file = io.open(filename, "a") -- Open file in append mode

for i = 1, IP_COUNT - 1 do
    table.insert(ipBuffer, intToIP(i))

    -- Log progress at intervals
    if i % LOG_INTERVAL == 0 then print(string.format("[Progress] Generated %d/%d IPs (%.2f%%)", i, IP_COUNT, (i/IP_COUNT) * 100)) end

    -- Chunk proccessing
    if i > 0 & i % BATCH_SIZE == 0 then print(string.format("[Progress] Reached %d IPs; continuing to generate...", i)) end
end

-- Write any remaining IPs in the buffer to the file
file:write(table.concat(ipBuffer, "\n"))
print(string.format("IP generation complete and saved to file. (%.3fs)", os.time() - start));