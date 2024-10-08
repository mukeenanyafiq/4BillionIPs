// Node.js script version of 4BillionIPs written by @mukeenanyafiq

// This script will generate 4 billion IPs in your RAM, and then letting it all off on a file which would took a while
// 64+ GBs of RAM are probably required.

const fs = require('fs'); // Use node:fs to access filesystem
const IP_COUNT = Math.pow(2, 32); // 4 billion IPs
const BATCH_SIZE = 10000000; // Process 10 million IPs at a time
const LOG_INTERVAL = Math.floor(IP_COUNT / 100); // Log progress every 1% completion
const start = Date.now(); // Record execution time

function intToIP(int) {
    return [
        (int >>> 24) & 0xFF,
        (int >>> 16) & 0xFF,
        (int >>> 8) & 0xFF,
        int & 0xFF
    ].join('.');
}

// Use a buffer to store IPs
let ipBuffer = [];
for (let i = 1; i <= IP_COUNT; i++) {
    ipBuffer.push(intToIP(i));

    // Log progress at intervals
    if (i % LOG_INTERVAL == 0) console.log(`[Progress] Generated ${i.toLocaleString()}/${IP_COUNT.toLocaleString()} IPs (${(i / IP_COUNT) * 100}%)`);

    // Chunk proccessing
    if (i % BATCH_SIZE == 0) console.log(`[Progress] Reached ${i.toLocaleString()} IPs; continuing to generate...`);
}

// Write the generated IPs to the file
fs.writeFileSync("../4BillionIPs.txt", ipBuffer.join("\n"));
console.log(`IP generation complete and saved to file. (${(Date.now() - start)/1000}s)`);