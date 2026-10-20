"""Filtro de git: quita las salidas de un notebook antes de subirlo.

Git le pasa el notebook por la entrada estándar y guarda lo que este
script devuelve. El archivo en tu computador no se modifica: solo la
versión que va al repositorio queda sin salidas.
"""
import json
import sys

nb = json.loads(sys.stdin.buffer.read().decode("utf-8"))
for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        cell["outputs"] = []
        cell["execution_count"] = None
    cell.get("metadata", {}).pop("execution", None)
nb.get("metadata", {}).pop("widgets", None)
sys.stdout.buffer.write(
    (json.dumps(nb, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
)
