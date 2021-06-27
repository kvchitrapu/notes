Good old [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree) is foundation of blockchain - rollup tree of hashes

Replace trust with c
Transaction rate conundrum. Two factors:  block size; block generation time
> tps = (MAX_BLOCK_SIZE/AVG_TXN_SIZE) * BLOCK_GEN_TIME
2. MAX_BLOCK_SIZE = high (1GB+) or small (< 1GB) 

| Small Block        | Big Block |
| ----------- | ----------- |
| high barrier of entry     | small entry investment - h/w to solve small puzzles to validate trannsactions       |
| high transaction (write) rate like Visa/MC (~2k tps)  | high trust on small (indie) transaction (~5 tps)        |
2. Generation time is ~10 mins
