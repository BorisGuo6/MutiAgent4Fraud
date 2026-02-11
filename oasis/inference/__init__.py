# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from .inference_manager import InferencerManager
from .inference_thread import InferenceThread

# OpenClaw 兼容模块（可选依赖）
try:
    from .openclaw_adapter import OpenClawInferenceAdapter  # type: ignore
    from .openclaw_server import OpenClawServer, ServerConfig  # type: ignore
except Exception:  # pragma: no cover - optional module may be missing
    OpenClawInferenceAdapter = None  # type: ignore
    OpenClawServer = None  # type: ignore
    ServerConfig = None  # type: ignore

__all__ = ["InferencerManager", "InferenceThread"]

if OpenClawInferenceAdapter is not None:
    __all__ += ["OpenClawInferenceAdapter", "OpenClawServer", "ServerConfig"]
