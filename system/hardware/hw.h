#pragma once

#include <string>

#include "system/hardware/base.h"
#include "common/util.h"

#if QCOM2
#include "system/hardware/tici/hardware.h"
#define Hardware HardwareTici
#else
#include "system/hardware/pc/hardware.h"
#define Hardware HardwarePC
#endif

namespace Path {
  inline bool is_android() {
    return getenv("ANDROID_DATA") != nullptr;
  }

  inline std::string openpilot_prefix() {
    return util::getenv("OPENPILOT_PREFIX", "");
  }

  inline std::string comma_home() {
    return util::getenv("HOME") + "/.comma" + Path::openpilot_prefix();
  }

  inline std::string log_root() {
    if (const char *env = getenv("LOG_ROOT")) {
      return env;
    }
    if (is_android()) {
      return "/sdcard/flowpilot/realdata";
    }
    return Hardware::PC() ? Path::comma_home() + "/media/0/realdata" : "/data/media/0/realdata";
  }

  inline std::string params() {
    if (const char *env = getenv("PARAMS_ROOT")) {
      return env;
    }
    if (is_android()) {
      return "/sdcard/flowpilot/params";
    }
    return Hardware::PC() ? (Path::comma_home() + "/params") : "/data/params";
  }

  inline std::string rsa_file() {
    return Hardware::PC() ? Path::comma_home() + "/persist/comma/id_rsa" : "/persist/comma/id_rsa";
  }

  inline std::string swaglog_ipc() {
    return "ipc:///tmp/logmessage" + Path::openpilot_prefix();
  }

  inline std::string download_cache_root() {
    if (const char *env = getenv("COMMA_CACHE")) {
      return env;
    }
    if (is_android()) {
      return "/sdcard/flowpilot/cache";
    }
    return "/tmp/comma_download_cache" + Path::openpilot_prefix() + "/";
  }

 inline std::string shm_path() {
    #ifdef __APPLE__
     return"/tmp";
    #else
     return "/dev/shm";
    #endif
 }

  inline std::string model_root() {
    if (is_android()) {
      return "/sdcard/flowpilot/models";
    }
    return Hardware::PC() ? Path::comma_home() + "/media/0/models" : "/data/media/0/models";
  }
}  // namespace Path
