// Node.js script version of 4BillionIPs written by @mukeenanyafiq

const fs = require('fs'); // Use node:fs to access filesystem
const IP_COUNT = Math.pow(2, 32); // 4 billion IPs
const BATCH_SIZE = 1000000; // Write 1 million IPs at a time
const LOG_INTERVAL = Math.floor(IP_COUNT / 100); // Log progress every 1% completion
const filename = "../4BillionIPs.txt"
const start = Date.now(); // Record execution time

function intToIP(int) {
    return [
        (int >>> 24) & 0xFF,
        (int >>> 16) & 0xFF,
        (int >>> 8) & 0xFF,
        int & 0xFF
    ].join('.');
}

// Use a temporary buffer
let buffer = [];
for (let i = 0; i < IP_COUNT; i++) {
    buffer.push(intToIP(i));

    // If buffer size reaches BATCH_SIZE, write to file
    if (buffer.length == BATCH_SIZE) {
        fs.appendFileSync(filename, buffer.join("\n") + "\n");
        buffer = [];  // Clear the buffer
    }

    // Log progress at intervals
    if (i > 0 && i % LOG_INTERVAL == 0) console.log(`[Progress] Generated ${i.toLocaleString()}/${IP_COUNT.toLocaleString()} IPs (${(i / IP_COUNT) * 100}%)`);
}

// Write any remaining IPs in the buffer to the file
if (buffer.length > 0) fs.appendFileSync(filename, buffer.join("\n"));
console.log(`IP generation complete and saved to file. (${(Date.now() - start)/1000}s)`);