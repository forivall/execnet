from typing import BinaryIO
from .gateway import Gateway
from .xspec import XSpec

class HostNotFound(Exception): ...

def bootstrap(io: BinaryIO, spec: XSpec) -> Gateway: ...
