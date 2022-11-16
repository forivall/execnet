from typing import TYPE_CHECKING, Literal, Optional, Protocol, TypedDict
from queue import Queue
from .gateway import Gateway
from .gateway_base import Channel

if TYPE_CHECKING:
    class AddTargetOptions(TypedDict):
        delete: Optional[bool]

    class RsyncCallback(Protocol):
        def __call__(self, event: Literal["ack", "list"], s: int, channel: Channel) -> None: ...

class RSync(object):
    def __init__(self, sourcedir, callback: Optional[RsyncCallback]=None, verbose=True): ...
    def filter(self, path: str) -> bool: ...
    def send(self, raises=True) -> None: ...
    def add_target(self, gateway: Gateway, destdir: str, finishedcallback=None, **options: AddTargetOptions) -> None: ...
