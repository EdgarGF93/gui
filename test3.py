from PyQt5 import Qt
from silx.gui.plot import PlotWidget
from silx.gui.plot.actions import PlotAction
from silx.gui import icons
from silx.gui import qt

class Action1(PlotAction):
    def __init__(self, plot, parent):
        super().__init__(
            plot=plot,
            parent=parent,            
            icon=icons.getQIcon("math-substract"),
            text="action_1",
        )



class Plot1Widget(PlotWidget):
    def __init__(self):
        super().__init__()
        self._build()
    
    def _build(self):
        self._build_toolbar()

    def _build_toolbar(self):
        toolbar = self._init_toolbar()
        self.addToolBar(toolbar)

    def _init_toolbar(self) -> qt.QToolBar:
        toolbar = qt.QToolBar()
        action1 = Action1(
            plot=self,
            parent=toolbar,
        )
        toolbar.addAction(action1)
        return toolbar
    

app = Qt.QApplication([])
plot = Plot1Widget()
plot.show()
app.exec()