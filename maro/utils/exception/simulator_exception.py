# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.


from .backends_exception import MAROException
from .error_code import ERROR_CODE


class BusinessEngineNotFoundError(MAROException):
    def __init__(self):
        super().__init__(2200, ERROR_CODE[2200])