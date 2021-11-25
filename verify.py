from typing import Union
import grpcbigbuffer as grpcbf
from logger import LOGGER
import hashlib
from celaut_pb2 import Any, Any, Service

# -- HASH IDs --
SHAKE_256_ID = bytes.fromhex("46b9dd2b0ba88d13233b3feb743eeb243fcd52ea62b81b82b50c27646ed5762f")
SHA3_256_ID = bytes.fromhex("a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a")

# -- HASH FUNCTIONS --
SHAKE_256 = lambda value: "" if value is None else hashlib.shake_256(value).digest(32)
SHA3_256 = lambda value: "" if value is None else hashlib.sha3_256(value).digest()

HASH_FUNCTIONS = {
    SHA3_256_ID: SHA3_256,
    SHAKE_256_ID: SHAKE_256
}

def calculate_hashes(value) -> list:
    return [
        Any.Metadata.HashTag.Hash(
            type = SHA3_256_ID, 
            value = SHA3_256(value)
        ),
        Any.Metadata.HashTag.Hash(
            type = SHAKE_256_ID,
            value = SHAKE_256(value)
        )
    ]

def check_service(service_buffer: bytes, hashes: list) -> bool:
    for hash in hashes:
        if hash.type in HASH_FUNCTIONS and \
            hash.value == HASH_FUNCTIONS[hash.type](
                            value = service_buffer
                            ):
                return True
    return False

# Return the service's sha3-256 hash on hexadecimal format.
def get_service_hex_main_hash(
    service_buffer: Union[bytes, str, Service, tuple] = None, 
    metadata: Any.Metadata = Any.Metadata(),
    other_hashes: list = []
    ) -> str:
    # Find if it has the hash.
    for hash in  list(metadata.hashtag.hash) + other_hashes:
        if hash.type == SHA3_256_ID:
            return hash.value.hex()

    # If not but the spec. is complete, calculate the hash prunning it before.
    # If not and is incomplete, it's going to be imposible calculate any hash.
    
    if metadata.complete and service_buffer:
        if type(service_buffer) is not tuple: service_buffer = (service_buffer)
        return SHA3_256(
            value = grpcbf.partitions_to_buffer(partitions = service_buffer)
        ).hex()

    LOGGER(' sha3-256 hash function is not implemented on this method.')
    raise Exception(' sha3-256 hash function is not implemented on this method.')

def get_service_list_of_hashes(service_buffer: bytes, metadata: Any.Metadata) -> list:
    if metadata.complete:
        return calculate_hashes(
            value = service_buffer
        )
    else:
        raise Exception("Can't get the hashes if the service is not complete.")
