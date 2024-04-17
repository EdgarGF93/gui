from PyQt5 import Qt
from silx.gui.plot import PlotWidget

app = Qt.QApplication([])
plot = PlotWidget()
plot.show()
app.exec()