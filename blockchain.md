(Merkle tree) [https://en.wikipedia.org/wiki/Merkle_tree]
Transaction rate conundrum. Two factors:  block size; block generation time
1. tps = (MAX_BLOCK_SIZE/AVG_TXN_SIZE)*BLOCK_GEN_TIME
2. MAX_BLOCK_SIZE=high(1GB+) >< small (< 1GB) 
  1. high barrier of entry >< affordable to participate  
  1. high transaction (write) rate (~2k tps) >< high trust on small transaction (~5 tps) 
2. Generation time is ~10 mins
