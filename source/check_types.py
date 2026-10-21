"""Check every notebook code cell without executing downloads or training."""

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory


def main() -> int:
    root = Path(__file__).resolve().parent
    notebook = root / "notebooks" / "har_complete_pipeline.ipynb"
    cells = json.loads(notebook.read_text(encoding="utf-8"))["cells"]
    code = ""
    locations = []
    for index, cell in enumerate(cells, 1):
        if cell["cell_type"] != "code":
            continue
        code += f"\n# Notebook cell {index}\n"
        start = len(code.splitlines()) + 1
        code += "".join(cell["source"]) + "\n"
        locations.append((start, len(code.splitlines()), index))
    with TemporaryDirectory(prefix="har-typecheck-") as temporary:
        script = Path(temporary) / "har_complete_pipeline.py"
        script.write_text(code, encoding="utf-8")
        result = subprocess.run(
            [sys.executable, "-m", "pyright", "--project", str(root / "pyrightconfig.json"),
             "--pythonpath", sys.executable, "--outputjson", str(script)],
            capture_output=True, text=True,
        )
        if result.returncode not in (0, 1):
            print(result.stderr or result.stdout)
            return result.returncode
        report = json.loads(result.stdout)
        for diagnostic in report["generalDiagnostics"]:
            line = diagnostic["range"]["start"]["line"] + 1
            cell = next((i for start, end, i in locations if start <= line <= end), None)
            print(f"{notebook.name}: cell {cell}: {diagnostic['message']}")
        summary = report["summary"]
        print(f"Notebook: {summary['errorCount']} errors, {summary['warningCount']} warnings")
        return int(bool(summary["errorCount"] or summary["warningCount"]))


if __name__ == "__main__":
    raise SystemExit(main())
