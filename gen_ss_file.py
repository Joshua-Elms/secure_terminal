from pathlib import Path

project_dir = Path(__file__).parent.resolve()
filestr = f"""#!/bin/bash

# Safety Shutdown Script
cd {project_dir}
source .venv/bin/activate
python safety_shutdown.py"""
with open(project_dir / "ss", "w") as f:
    f.write(filestr)