"""Run the ten SmartJunction module entry points in order."""

import subprocess
import sys
from pathlib import Path


def main():
    repo_root = Path(__file__).resolve().parent
    for number in range(1, 11):
        module = f"src.smartjunction.module_{number:02d}.run"
        print(f"Running Module {number:02d}", flush=True)
        result = subprocess.run([sys.executable, "-m", module], cwd=repo_root)
        if result.returncode:
            print(f"Module {number:02d} exited with code {result.returncode}.", file=sys.stderr)
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
