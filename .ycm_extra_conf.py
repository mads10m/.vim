import os
import ycm_core

flags = [
  '-Wall',
  '-Wextra',
  '-Werror',
  '-Wno-long-long',
  '-Wno-variadic-macros',
  '-fexceptions',
  '-ferror-limit=10000',
  '-DNDEBUG',
  '-std=c99',
  '-xc',
  '-isystem/usr/include/',
  #'-isystem/usr/lib/avr/include/',
  #'-isystem~/Downloads/arduino-1.8.10-linux64/arduino-1.8.10/hardware/tools/avr/avr/include/',
  ]

SOURCE_EXTENSIONS = ['.cpp', '.cxx', '.cc', '.c', ]

def FlagsForFile( filename, **kwargs ):
  return {
  'flags': flags,
  'do_cache': True
  }
