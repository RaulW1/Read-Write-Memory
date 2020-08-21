import ctypes

#dlls

kernel32 = ctypes.windll.kernel32

#process permissions

PROCESS_QUERY_INFORMATION = (0x0400)
PROCESS_VM_OPERATION = (0x0008)
PROCESS_VM_READ = (0x0010)
PROCESS_VM_WRITE = (0x0020)
PROCESS_ALL_ACCESS = (0x1F0FFF)

#win apis

OpenProcess = kernel32.OpenProcess
CloseHandle = kernel32.CloseHandle
GetLastError = kernel32.GetLastError
ReadProcessMemory = kernel32.ReadProcessMemory
WriteProcessMemory = kernel32.WriteProcessMemory

class ReadWriteMem:

    def OpenProcess(self, processPID):
        hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, processPID)

        return hProcess

    def CloseHandle(self, hProcess):
        CloseHandle(hProcess)

    def GetLastError(self):
        GetLastError()

        return GetLastError()

    def ReadProcessMemory(self, hProcess, MemAddress):
        try:
            MemValue = ctypes.c_uint()
            MemValueSize = ctypes.sizeof(MemValue)

            ReadProcessMemory(hProcess, MemAddress, ctypes.byref(MemValue), MemValueSize, None)

            return MemValue.value
            

        except(BufferError, ValueError, TypeError):
            CloseHandle(hProcess)
            error = "Handle closed. Error:", hProcess, GetLastError()

            return error

    def WriteProcessMemory(self, hProcess, MemAddress, Value):
        try:
            ValueBuffer = ctypes.c_int(Value)
            ValueBufferSize = ctypes.sizeof(ValueBuffer)

            WriteProcessMemory(hProcess, MemAddress, ctypes.byref(ValueBuffer), ValueBufferSize, None)

        except(BufferError, ValueError, TypeError):
            CloseHandle(hProcess)
            error = "Handle closed. Error:", hProcess, GetLastError()

            return error

rwm = ReadWriteMem()
 