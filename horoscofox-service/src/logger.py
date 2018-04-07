class LogColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def warn(message):
    print(LogColors.WARNING + ' ⚠️  WARN : ' + message + LogColors.ENDC)


def error(message):
    print(LogColors.FAIL + ' 🚨  ERROR : ' + message + LogColors.ENDC)


def info(message):
    print(LogColors.OKBLUE + ' 🦋  INFO : ' + message + LogColors.ENDC)


def success(message):
    print(LogColors.OKGREEN + ' 🍀  SUCCESS : ' + message + LogColors.ENDC)
