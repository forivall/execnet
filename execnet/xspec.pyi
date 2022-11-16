from typing import Optional

class XSpec:
    popen: Optional[str | bool] 
    ssh: Optional[str | bool] 
    socket: Optional[str | bool] 
    python: Optional[str | bool] 
    chdir: Optional[str | bool] 
    nice: Optional[str | bool] 
    dont_write_bytecode: Optional[str | bool] 
    execmodel: Optional[str | bool] 

    def __init__(self, string: str): ...
