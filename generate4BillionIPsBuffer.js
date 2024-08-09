// This script will generate 4 billion IPs but instead of saving it first, it will put all the generated IPs in your RAM.
// 128 GBs of RAM are probably required.

const fs = require('fs');
const generatedIPs = new Set();
const IP_COUNT = Math.pow(2, 32) + 1;
const LOG_INTERVAL = Math.floor(IP_COUNT / 100); // Log progress every 1% completion

function generateIP() {
    let generatedIP;
    do {
        generatedIP = `${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}`;
    } while (generatedIPs.has(generatedIP));

    generatedIPs.add(generatedIP);
    return generatedIP;
}

// Use a buffer to store IPs
let ipBuffer = [];
for (let i = 1; i <= IP_COUNT + 1; i++) {
    ipBuffer.push(generateIP());

    // Log progress at intervals
    if (i % LOG_INTERVAL === 0) console.log(`[Progress] Generated ${i} / ${IP_COUNT} IPs (${(i / IP_COUNT) * 100}%)`);
}

// Write the generated IPs to the file
fs.writeFileSync("./4BillionIPs.txt", ipBuffer.join("\n"));
console.log("IP generation complete and saved to file.");