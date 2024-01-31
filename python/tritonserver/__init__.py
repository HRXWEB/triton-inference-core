# Copyright 2023-2024, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Triton Inference Server In-Process Python API

The Triton Inference Server In-Process Python API enables developers to easily
embed a Triton inference server within their python
application. Developers can load and interact with models, send
inference requests, query metrics, etc. Everything available through
the C API for emebedding a Triton Inference Server in C / C++
applications has been provided within a Python API.

Note
----
The Python API is currently in BETA. Interfaces and
capabilities are subject to change. Any feedback is welcome.

Note
----
- Any objects not explicitly exported here are considered private.

- Any classes, methods, properties, or arguments prefixed with `_` are
  considered private.

"""
from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from tritonserver._api._allocators import MemoryAllocator as MemoryAllocator
from tritonserver._api._allocators import MemoryBuffer as MemoryBuffer
from tritonserver._api._allocators import MemoryType as MemoryType
from tritonserver._api._allocators import (
    default_memory_allocators as default_memory_allocators,
)
from tritonserver._api._dlpack import DLDeviceType as DLDeviceType
from tritonserver._api._logging import LogLevel as LogLevel
from tritonserver._api._logging import LogMessage as LogMessage
from tritonserver._api._model import Model as Model
from tritonserver._api._model import ModelBatchFlag as ModelBatchFlag
from tritonserver._api._model import ModelTxnPropertyFlag as ModelTxnPropertyFlag
from tritonserver._api._request import InferenceRequest as InferenceRequest
from tritonserver._api._response import AsyncResponseIterator as AsyncResponseIterator
from tritonserver._api._response import InferenceResponse as InferenceResponse
from tritonserver._api._response import ResponseIterator as ResponseIterator
from tritonserver._api._server import InstanceGroupKind as InstanceGroupKind
from tritonserver._api._server import LogFormat as LogFormat
from tritonserver._api._server import Metric as Metric
from tritonserver._api._server import MetricFamily as MetricFamily
from tritonserver._api._server import MetricFormat as MetricFormat
from tritonserver._api._server import MetricKind as MetricKind
from tritonserver._api._server import ModelControlMode as ModelControlMode
from tritonserver._api._server import ModelDictionary as ModelDictionary
from tritonserver._api._server import ModelLoadDeviceLimit as ModelLoadDeviceLimit
from tritonserver._api._server import Options as Options
from tritonserver._api._server import RateLimiterResource as RateLimiterResource
from tritonserver._api._server import RateLimitMode as RateLimitMode
from tritonserver._api._server import Server as Server
from tritonserver._api._tensor import DataType as DataType
from tritonserver._api._tensor import Tensor as Tensor
from tritonserver._c import AlreadyExistsError as AlreadyExistsError
from tritonserver._c import InternalError as InternalError
from tritonserver._c import InvalidArgumentError as InvalidArgumentError
from tritonserver._c import NotFoundError as NotFoundError
from tritonserver._c import TritonError as TritonError
from tritonserver._c import UnavailableError as UnavailableError
from tritonserver._c import UnknownError as UnknownError
from tritonserver._c import UnsupportedError as UnsupportedError

# Rename module from internal modules
# Due to how we are aliasing objects from the bindings
# We have to fix up the naming for documentation
_renamed_class_names = [
    "LogFormat",
    "ModelLoadDeviceLimit",
    "MemoryType",
    "MetricKind",
    "DataType",
    "LogLevel",
    "MetricFormat",
    "ModelControlMode",
    "RateLimitMode",
    "TritonError",
    "NotFoundError",
    "UnknownError",
    "InternalError",
    "InvalidArgumentError",
    "UnavailableError",
    "AlreadyExistsError",
    "UnsupportedError",
]


for class_name in _renamed_class_names:
    _class = globals()[class_name]
    _class.__module__ = "tritonserver"
    _class.__name__ = class_name

__all__ = []
__version__ = "UNKNOWN"

try:
    __version__ = version("tritonserver")
except PackageNotFoundError:
    pass

del version
del PackageNotFoundError
