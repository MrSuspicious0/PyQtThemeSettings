# PyQtThemeSettings

[![License](https://img.shields.io/github/license/MrSuspicious0/PyQtThemeSettings?label=License)](https://github.com/MrSuspicious0/PyQtThemeSettings/blob/master/LICENSE)
[![Version](https://img.shields.io/pypi/v/PyQtThemeSettings?label=Version)](https://pypi.org/project/PyQtThemeSettings/)
[![Downloads](https://img.shields.io/pypi/dw/PyQtThemeSettings?color=light&label=Downloads)](https://pypi.org/project/PyQtThemeSettings/)

A package for adding a theme management window to any PySide6 applications using [PyQtDarkTheme](https://github.com/5yutan5/PyQtDarkTheme).

Support for PyQt may come at some point, but PySide6 is the official recommendation of Qt for Python, so it's not a priority for me.

## Installation

PyQtThemeSettings can be installed using [pip](https://pip.pypa.io/en/stable/)

```bash
pip install pyqtthemesettings
```

# Usage

### Without PyQtThemeSettings

```python
if __name__ == "__main__":
    app = QApplication([]) # Initialise the App
    window = MainWindow() # Initialise Window
    window.show()
    exit(app.exec())
```

### With PyQtThemeSettings

```python
from PyQtThemeSettings import AppSettings

if __name__ == "__main__":
    app = QApplication([])
    app.setOrganizationName("MrSuspicious")
    app.setApplicationName("TestApp")
    settings = QSettings()
    appSettings = AppSettings(settings, app) # Pass in QSettings and QApplication
    window = MainWindow()
    window.show()
    exit(app.exec())
```

PyQtThemeSettings takes in a [QSettings](https://doc.qt.io/qtforpython/PySide6/QtCore/QSettings.html) object, which controls where the persistent settings are stored, and a [QApplication](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QApplication.html).

In order to access the settings window, connect whatever signal you wish to the `AppSettings.openSettings` slot.

To reset to default settings, connect whatever signal you wish to the `AppSettings.resetToDefaults` slot.

## Contribution to the Project

If you have any feature suggestions please feel free to make a [pull request](https://github.com/MrSuspicious0/PyQtThemeSettings/pulls)!

Also if you happen to test this with a version other than python 3.11 and notice no issues, please let me know so i can change the entry on PyPi
