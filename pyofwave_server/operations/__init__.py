"""
Please place files here to add operations for use with client protocols.
The name of the file will be used as the namespace and any contained public functions will be used as
operations. The information is passed as kwargs to the function.
Requests which don't match your function defination will return an error.
"""

class OperationError(Exception):
    def __init__(self, code, **status):
        super(Exception).__init__(self)
        
        self.code = code
        self.status = status
