import gdb


class BaseAddr(gdb.Function):
    def __init__(self):
        super().__init__("baseaddr")

    def invoke(self, file_path=None):
        if file_path is None:
            file_path = pwndbg.proc.exe
        else:
            file_path = file_path.string()
        addr = [page.start for page in pwndbg.vmmap.proc_pid_maps() if file_path in page.objfile][0]
        return addr

BaseAddr()