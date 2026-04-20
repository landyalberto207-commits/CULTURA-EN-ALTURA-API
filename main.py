from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


backend_dir = Path(__file__).resolve().parent / "backend"
backend_main = backend_dir / "main.py"

if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

spec = importlib.util.spec_from_file_location("backend_entrypoint", backend_main)
if spec is None or spec.loader is None:
    raise RuntimeError("No se pudo cargar el entrypoint del backend")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

app = module.app