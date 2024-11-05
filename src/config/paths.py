from pathlib import Path
from typing import Final

# Source Directories
CONFIG_DIR:Final = Path(__file__).parent
SRC_DIR:Final = CONFIG_DIR.parent

# Project Directories
PRJ_DIR:Final = SRC_DIR.parent
DATA_DIR:Final = PRJ_DIR / "data"
LOGS_DIR:Final = PRJ_DIR / "logs"

# Output Directories
TEST_OUTPUT_DIR:Final = PRJ_DIR / ".output"
TEST_DIR:Final = PRJ_DIR / "test"

if "__main__" in __name__:
      None