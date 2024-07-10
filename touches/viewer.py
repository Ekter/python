"""Main module."""
import sys
import time
from typing import NoReturn

from PySide6.QtWidgets import QApplication

import json
import time

from PySide6.QtCore import Slot, Signal, Qt, QCoreApplication, QTimer
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QVBoxLayout,
    QWidget,
    QTableView,
    QProgressDialog,
    QLabel,
)


class IMainWindow(QMainWindow):

    closed_signal = Signal()

    def __init__(self, char: str) -> None:
        """Creates the main window."""
        QMainWindow.__init__(self)
        self.label = QLabel()
        self.label.setText(char)
        self.setCentralWidget(self.label)
        self.setWindowTitle(char)
        self.resize(100, 100)
        self.closed_signal.connect(self.close)
        self.timer_ticks = QTimer(self)
        self.timer_ticks.timeout.connect(self.close)
        self.timer_ticks.start(3000)

    @Slot()
    def close_window(self) -> None:
        """Close the window."""
        self.close()

    def closeEvent(self, event) -> None:
        """
        Method called on window closed. Used for stopping all the timers.

        Overloaded from QMainWindow.
        """
        print(f"closing event: {event}")
        self.closed_signal.emit()
        time.sleep(0.2)
        print("closing")
        event.accept()

def main() -> NoReturn:
    """Main function."""
    app = QApplication(sys.argv)

    window = IMainWindow()
    window.show()

    print("launching")
    exit_code: int = app.exec()
    print(f"Quitted, code = {exit_code}")
    time.sleep(0.5)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

