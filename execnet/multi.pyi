from typing import Literal, Optional
from .gateway import Gateway
from .gateway_base import Backend, ExecModel
from .xspec import XSpec

class MultiChannel: ...

class Group(object):
  defaultspec: Literal["popen"]
  @property
  def execmodel(self) -> ExecModel: ...
  @property
  def remote_execmodel(self) -> ExecModel: ...

  def __init__(self, xspecs: tuple[str] = (), execmodel: Backend = "thread"): ...
  def makegateway(self, spec: Optional[str | XSpec] = None) -> Gateway: ...
  def set_execmodel(
    self,
    execmodel: Backend | ExecModel,
    remote_execmodel: Backend | ExecModel = None,
  ) -> None: ...

default_group: Group
makegateway = default_group.makegateway
set_execmodel = default_group.set_execmodel
