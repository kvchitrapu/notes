#! /usr/bin/env python3

import json
import re
import argparse
import sys
import pprint
import random
import hashlib

# TODO: improve the randomness with better entropy

WORD_MAP = {
    '000': "ABC"
}


def random_sequence(random_seq_len):
    """
    create cryptographic random sequence S of 128 to 256 bits
    Args:
      random_seq_len: 128 - 256 bits
    """
    # create S of length random_seq_len
    random.seed()
    random_seq = random.getrandbits(random_seq_len)
    print("Random sequence of {random_seq_len}: {random_seq}")
    return random_seq


def create_checksum(random_seq):
    """
    create checksum with the first (random_seq_bitlen/32) bits of SHA-256
    Args:
        random_seq: random sequence bits
    Output:
        checksum:
    """
    checksum = ''
    random_seq_bitlen = random_seq.bit_length()
    checksum_len = random_seq_bitlen/32

    h = hashlib.sha256()
    h.update(random_seq.to_bytes(
        (random_seq_bitlen + 7) // 8, byteorder='little'))
    digest = h.hexdigest()
    # extract random_seq_bitlen bits from digest
    # checksum = digest.getbits(random_seq_bitlen)
    return checksum


def divide_sequence(random_seq, checksum):
    """
    append checksum to random_seq and check them into sections
    """
    checksummed_seq = ''
    sections = []
    # checksummed_seq = random_seq.append(checksum)
    # sections = checksummed_seq.chopinto(11)
    return sections


def get_words(sectioned_seq):
    """
    find word for each section
    """
    mnemonic_words = []
    for k in sectioned_seq:
        mnemonic_words.append(word_map[k])

    print(mnemonic_words)


def main():
    """
    main function for testing all ports
    Args:
      args: command line arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--entropy', '-e', dest='entropy', required=True,
                        help='entropy')
    parser.add_argument('--verbose', '-v', action='count')

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as errmsg:
        print("Invalid arguments {0}".format(errmsg))
        return False

    random_seq = random_sequence()
    checksum = create_checksum(random_seq)
    sections = divide_sequence(random_seq, checksum)
    mnemonic_words = get_words(sections)

    return True


if __name__ == '__main__':
    STATUS = 0 if main() else 1
    print('Exiting with status: %d' % STATUS)
    sys.exit(STATUS)
