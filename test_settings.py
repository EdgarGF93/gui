from PyQt5.QtCore import QSettings



settings = QSettings(
    # QSettings.IniFormat,
    # QSettings.UserScope,
    "ESRF",
    "pyxscat",
    None,
)
settings.sync()

settings.setValue("username", "edgar")

print(settings.fileName())

print(settings.value("username"))