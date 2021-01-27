import sys

colors = {
  'red': '\033[31m',
  'green': '\033[32m',
  'blue': '\033[34m',
  'yellow': '\033[33m',
  'reset': '\033[0m',
  }

class emoji:
  log= 'ℹ'
  party= '🎉'
  new= '✨'
  update= '🖋'
  paper= '📄'
  folder= '📁'
  config= '⚙'
  success= '✅'
  waning= '⚠'
  error= '⛔'

def errPrint(msg: str):
  print(msg, file=sys.stderr)

def __log(color: str, msg: str, err: bool = False):
  if err:
    errPrint(f'{color}{msg}{colors["reset"]}')
  else:
    print(f'{color}{msg}{colors["reset"]}')

def log(msg: str):
  __log(colors['reset'], msg)

def info(msg: str):
  __log(colors['blue'], f'[INFO] {msg}')

def success(msg: str):
  __log(colors['green'], f'[SUCCESS] {msg}')

def warn(msg: str):
  __log(colors['yellow'], f'[WARNING] {msg}')

def error(msg: str):
  __log(colors['red'], f'[ERROR] {msg}', True)