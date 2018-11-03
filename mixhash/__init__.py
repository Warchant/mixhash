# import hashlib
import qubit_hash
# import keccak_hash
# import lyra2re_hash
# import x11_hash
# import lyra2re2_hash
# import lyra2re_hash
# import qubit_hash

# def SHA256(x):
#     """Two rounds of SHA256."""
#     return hashlib.sha256(hashlib.sha256(x).digest()).digest()
#
# def Lyra2re(x):
#     return lyra2re_hash.getPoWHash(x)
#
# def Keccak(x):
#     return keccak_hash.getPoWHash(x, len(x))

def Qubit(x):
    return qubit_hash.getPoWHash(x)

# def Neoscrypt(x):
#     return neoscrypt.getPoWHash(x)

# def SkeinHash(x):
#     return skeinhash.getPoWHash(x)

# def QubitHash(x):
#     return qubit_hash.getPoWHash(x)

# def GroestlHash(x):
#     return groestlcoin_hash.getHash(x, len(x))

# def X11(x):
#     return x11_hash.getPoWHash(x)

# def ScryptHash(x):
#     """Scrypt (Litecoin parameters) hash."""
#     return ltc_scrypt.getPoWHash(x)

# algorithms = {
#     # SHA256Hash is not advertised.
#     'SHA256d': SHA256dHash,
#     'NeoScrypt': NeoscryptHash,
#     'Skein': SkeinHash,
#     'Qubit': QubitHash,
#     'Groestl': GroestlHash,
#     'X11': X11Hash,
#     'Scrypt': ScryptHash,
# }
