import os
import platform
from pathlib import Path

from openpilot.system.hardware import PC, ANDROID

DEFAULT_DOWNLOAD_CACHE_ROOT = "/tmp/comma_download_cache"

class Paths:
  @staticmethod
  def android_root() -> str:
    return os.environ.get("ANDROID_STORAGE_ROOT", "/sdcard/flowpilot")

  @staticmethod
  def comma_home() -> str:
    return os.path.join(str(Path.home()), ".comma" + os.environ.get("OPENPILOT_PREFIX", ""))

  @staticmethod
  def log_root() -> str:
    if os.environ.get('LOG_ROOT', False):
      return os.environ['LOG_ROOT']
    elif ANDROID:
      return str(Path(Paths.android_root()) / "realdata")
    elif PC:
      return str(Path(Paths.comma_home()) / "media" / "0" / "realdata")
    else:
      return '/data/media/0/realdata/'

  @staticmethod
  def log_root_external() -> str:
    return '/mnt/external_realdata/'

  @staticmethod
  def swaglog_root() -> str:
    if ANDROID:
      return os.path.join(Paths.android_root(), "log")
    if PC:
      return os.path.join(Paths.comma_home(), "log")
    else:
      return "/data/log/"

  @staticmethod
  def swaglog_ipc() -> str:
    return "ipc:///tmp/logmessage" + os.environ.get("OPENPILOT_PREFIX", "")

  @staticmethod
  def download_cache_root() -> str:
    if os.environ.get('COMMA_CACHE', False):
      return os.environ['COMMA_CACHE'] + "/"
    if ANDROID:
      return os.path.join(Paths.android_root(), "cache") + "/"
    return DEFAULT_DOWNLOAD_CACHE_ROOT + os.environ.get("OPENPILOT_PREFIX", "") + "/"

  @staticmethod
  def persist_root() -> str:
    if ANDROID:
      return os.path.join(Paths.android_root(), "persist")
    if PC:
      return os.path.join(Paths.comma_home(), "persist")
    else:
      return "/persist/"

  @staticmethod
  def stats_root() -> str:
    if ANDROID:
      return os.path.join(Paths.android_root(), "stats")
    if PC:
      return str(Path(Paths.comma_home()) / "stats")
    else:
      return "/data/stats/"

  @staticmethod
  def stats_sp_root() -> str:
    if ANDROID:
      return os.path.join(Paths.android_root(), "stats_sp")
    if PC:
      return str(Path(Paths.comma_home()) / "stats")
    else:
      return "/data/stats_sp/"

  @staticmethod
  def config_root() -> str:
    if ANDROID:
      return Paths.android_root()
    if PC:
      return Paths.comma_home()
    else:
      return "/tmp/.comma"

  @staticmethod
  def shm_path() -> str:
    if PC and platform.system() == "Darwin":
      return "/tmp"  # This is not really shared memory on macOS, but it's the closest we can get
    return "/dev/shm"

  @staticmethod
  def model_root() -> str:
    if ANDROID:
      return str(Path(Paths.android_root()) / "models")
    if PC:
      return str(Path(Paths.comma_home()) / "media" / "0" / "models")
    else:
      return "/data/media/0/models"

  @staticmethod
  def crash_log_root() -> str:
    if ANDROID:
      return str(Path(Paths.android_root()) / "crashes")
    if PC:
      return str(Path(Paths.comma_home()) / "community" / "crashes")
    else:
      return "/data/community/crashes"

  @staticmethod
  def mapd_root() -> str:
    if ANDROID:
      return str(Path(Paths.android_root()) / "osm")
    if PC:
      return str(Path(Paths.comma_home()) / "media" / "0" / "osm")
    else:
      return "/data/media/0/osm"
