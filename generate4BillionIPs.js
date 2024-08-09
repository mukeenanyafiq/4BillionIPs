const fs = require('fs');
const IP_COUNT = Math.pow(2, 32) + 1;  // 4 billion IPs
const BATCH_SIZE = 1000000;            // Write 1 million IPs at a time
const LOG_INTERVAL = Math.floor(IP_COUNT / 100); // Log progress every 1% completion

function intToIP(int) {
    return [
        (int >>> 24) & 0xFF,
        (int >>> 16) & 0xFF,
        (int >>> 8) & 0xFF,
        int & 0xFF
    ].join('.');
}

let buffer = [];
for (let i = 0; i < IP_COUNT; i++) {
    buffer.push(intToIP(i));

    // If buffer size reaches BATCH_SIZE, write to file
    if (buffer.length == BATCH_SIZE) {
        fs.appendFileSync("./4BillionIPs.txt", buffer.join("\n") + "\n");
        buffer = [];  // Clear the buffer
    }

    // Log progress at intervals
    if (i > 0 && i % LOG_INTERVAL == 0) console.log(`[Progress] Generated ${i} / ${IP_COUNT} IPs (${(i / IP_COUNT) * 100}%)`);
}

// Write any remaining IPs in the buffer to the file
if (buffer.length > 0) fs.appendFileSync("./4BillionIPs.txt", buffer.join("\n") + "\n");
console.log("IP generation complete and saved to file.");