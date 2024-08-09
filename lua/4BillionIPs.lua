-- This script is only compatible for Lua 5.3+
-- Lua script version of 4BillionIPs written by @mukeenanyafiq

local IP_COUNT = 2^32 -- 4 billion IPs
local BATCH_SIZE = 1000000 -- Write 1 million IPs at a time
local LOG_INTERVAL = math.floor(IP_COUNT / 100) -- Log progress every 1% completion
local filename = "../4BillionIPs.txt"

local start = os.time() -- Record execution time

function intToIP(int)
    return string.format("%d.%d.%d.%d",
        (int >> 24) & 0xFF,
        (int >> 16) & 0xFF,
        (int >> 8) & 0xFF,
        int & 0xFF)
end

local buffer = {} -- Use a temporary buffer
local file = io.open(filename, "a") -- Open file in append mode

for i = 1, IP_COUNT - 1 do
    table.insert(buffer, intToIP(i))

    -- If buffer size reaches BATCH_SIZE, write to file
    if #buffer == BATCH_SIZE then
        file:write(table.concat(buffer, "\n"))
        buffer = {};  -- Clear the buffer
    end

    -- Log progress at intervals
    if i > 0 and i % LOG_INTERVAL == 0 then print(string.format("[Progress] Generated %d/%d IPs (%.2f%%)", i, IP_COUNT, (i/IP_COUNT) * 100)) end
end

-- Write any remaining IPs in the buffer to the file
if #buffer > 0 then file:write(table.concat(buffer, "\n")) end
print(string.format("IP generation complete and saved to file. (%.2fs)", os.time() - start));