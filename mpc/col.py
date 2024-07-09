from colorama import Fore
import os

_cont = ["", " ", "\n"]


def set_cont(beg: str = "", sep: str = " ", end: str = "\n") -> None:
    _cont[0] = beg
    _cont[1] = sep
    _cont[2] = end


def error(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    print(
        Fore.RED
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


err = error


def warning(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    print(
        Fore.YELLOW
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


warn = warning


def info(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    print(
        Fore.BLUE
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


note = info


def valid(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    print(
        Fore.GREEN
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


ok = valid


def default(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    print(
        Fore.RESET
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


def new_block(sep: str = "█"):
    print(sep * os.get_terminal_size()[0])


def decorate(s: str, col=Fore.RED):
    return col + s + Fore.RESET

deco = decorate