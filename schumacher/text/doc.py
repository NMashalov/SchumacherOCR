# https://github.com/facebookresearch/cc_net/blob/main/cc_net/minify.py
import typing as tp
import hashlib
import base64

HASH_SIZE = 4

def get_hashes(lines: tp.Iterable[str]) -> tp.List[bytes]:
    h = HASH_SIZE
    return [hashlib.sha1(bytes(l, encoding="utf-8")).digest()[:h] for l in lines]