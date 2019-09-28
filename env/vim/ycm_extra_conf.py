from distutils.sysconfig import get_python_inc
import platform
import os
import subprocess
import ycm_core

flags = [
    '-Wall',
    '-Wextra',
    '-Werror',
    '-x', 'c',
    '-isystem', '/usr/lib/gcc/x86_64-linux-gnu/7/include',
    '-isystem', '/usr/local/include',
    '-isystem', '/usr/include',
]

def Settings( **kwargs ):
    return {
        'flags': flags,
    }
    return {}
