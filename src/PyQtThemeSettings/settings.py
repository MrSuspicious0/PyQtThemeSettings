import qdarktheme
from PySide6.QtCore import QSettings
from PySide6.QtGui import QIcon, QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QColorDialog, QDialog

from .ui.settingswindowUI import Ui_SettingsWindow


class AppSettings:

    # Default accent colours for each theme as per qdarktheme docs
    DEFAULTS = {"dark": "#8ab4f7", "light": "#1a73e8"}

    def __init__(self, settings: QSettings, app: QApplication, icon: QIcon | QPixmap = None):
        """Initialises an AppSettings object that will store theme information in the location provided by `settings`, will automatically change
           app theme through `app`. `icon` specifies the icon that will be used for the settings window, can be left blank."""
        self.settings = settings
        self.app = app
        self.icon = icon

        self.loadValues()

        self.updateTheme()

    def loadValues(self):
        self.currentTheme: str = self.settings.value("theme", "dark")
        self.currentAccent: str = self.settings.value(
            "accent", self.DEFAULTS.get(self.currentTheme))

        if not self._currentAccent:
            self.currentAccent = self.DEFAULTS.get(self.currentTheme)

    def updateTheme(self):
        self.app.setStyleSheet(qdarktheme.load_stylesheet(
            self.currentTheme, custom_colors={"primary": self.currentAccent}))
        self.app.setPalette(qdarktheme.load_palette(self.currentTheme))

    def openSettings(self):
        window = SettingsWindow(self, self.icon)
        state = window.exec()
        if state == QDialog.DialogCode.Accepted:
            self.currentTheme = window.comboxTheme.currentText().lower()
            if window.newAccent is not None:
                self.currentAccent = window.newAccent

            self.updateTheme()

    @property
    def currentAccent(self):
        return self._currentAccent

    @currentAccent.setter
    def currentAccent(self, val):
        self._currentAccent = val
        self.settings.setValue("accent", val)
        self.settings.sync()

    @property
    def currentTheme(self):
        return self._currentTheme

    @currentTheme.setter
    def currentTheme(self, val):
        self._currentTheme = val
        self.settings.setValue("theme", val)
        self.settings.sync()


class SettingsWindow(QDialog, Ui_SettingsWindow):

    def __init__(self, master: AppSettings, icon: QIcon | QPixmap = None):
        super().__init__()
        self.master = master
        self.setupUi(self)
        self.btnApply.setDefault(True)

        if icon is not None and isinstance(icon, (QIcon, QPixmap)):
            self.setWindowIcon(icon)

        self.updatePreview(master.currentAccent)
        self.newAccent = None
        self.comboxTheme.addItems(["Dark", "Light"])
        self.comboxTheme.setCurrentText(self.master.currentTheme.title())

        self.btnChangeAccent.clicked.connect(self.changeAccent)
        self.btnApply.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)

    def updatePreview(self, colour1: str, colour2: str = None):
        if colour2 is None:
            colour2 = colour1
            self.lblColourPreview.setToolTip(colour1)
        else:
            self.lblColourPreview.setToolTip(f"{colour1} -> {colour2}")

        width = self.lblColourPreview.width()
        height = self.lblColourPreview.height()

        preview = QPixmap(width, height)
        previewLeft = QPixmap(width/2, height)
        previewRight = QPixmap(width/2, height)

        previewLeft.fill(colour1)
        previewRight.fill(colour2)

        painter = QPainter(preview)
        painter.drawPixmap(0, 0, width/2, height, previewLeft)
        painter.drawPixmap(width/2, 0, width, height, previewRight)
        painter.end()

        self.lblColourPreview.setPixmap(preview)

    def changeAccent(self):
        dialog = QColorDialog(self.master.currentAccent, self)
        dialog.setWindowTitle("Choose Accent Colour")

        if dialog.exec() == dialog.DialogCode.Accepted:
            colour = dialog.selectedColor().name()

            self.updatePreview(self.master.currentAccent, colour)
            self.newAccent = colour
