import os
from typing import cast

from openpilot.system.hardware.base import HardwareBase
from openpilot.system.hardware.tici.hardware import Tici
from openpilot.system.hardware.pc.hardware import Pc

TICI = os.path.isfile('/TICI')
AGNOS = os.path.isfile('/AGNOS')
ANDROID = "ANDROID_DATA" in os.environ
PC = (not TICI) and (not ANDROID)


if TICI:
  HARDWARE = cast(HardwareBase, Tici())
else:
  # Android wrapper runs as a Linux-like userland with PC hardware defaults.
  HARDWARE = cast(HardwareBase, Pc())
