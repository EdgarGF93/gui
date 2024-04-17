from PyQt5 import Qt
from silx.gui.plot import PlotWidget
from silx.gui import qt

class Plot1Widget(PlotWidget):
    def __init__(self):
        super().__init__()
        self._build()
    
    def _build(self):
        self._build_toolbar()

    def _build_toolbar(self):
        toolbar = self._init_toolbar()
        self.addToolBar(toolbar)

    def _init_toolbar(self):
        toolbar = qt.QToolBar()
        return toolbar

app = Qt.QApplication([])
plot = Plot1Widget()
plot.show()
app.exec()