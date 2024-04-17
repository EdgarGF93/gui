from PyQt5 import Qt
from silx.gui.plot import PlotWidget
from silx.gui.plot.actions import PlotAction
from silx.gui import icons
from silx.gui import qt
from silx.gui.plot.tools.menus import ZoomEnabledAxesMenu
from silx.gui.plot.actions.control import ZoomBackAction, ResetZoomAction

class Action1(PlotAction):
    def __init__(self, plot, parent):
        super().__init__(
            plot=plot,
            parent=parent,            
            icon=icons.getQIcon("math-substract"),
            text="action_1",
        )

class MyContextMenu(qt.QMenu):
    def __init__(self, plot=None):
        super(MyContextMenu, self).__init__(parent=plot)
        self._plot = plot
        self._build()
    
    def _build(self):
        action_zoom_back = ZoomBackAction(
            plot=self, 
            parent=self,
        )
        action_crosshair = ResetZoomAction(
            plot=self._plot, 
            parent=self._plot,
        )
        self.addAction(action_zoom_back)
        self.addSeparator()
        self.addAction(action_crosshair)
        self.addSeparator()
    
    def _exec(self, pos):
        plotArea = self._plot.getWidgetHandle()
        globalPosition = plotArea.mapToGlobal(pos)
        self.exec(globalPosition)

class MyPlotWidget(PlotWidget):
    def __init__(self):
        super().__init__()
        self._build()
    
    def _build(self):
        self._build_toolbar()
        self._build_context_menu()

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
    
    def _build_context_menu(self):
        plotArea = self.getWidgetHandle()
        plotArea.setContextMenuPolicy(qt.Qt.CustomContextMenu)
        plotArea.customContextMenuRequested.connect(self._contextMenu)
    
    def _contextMenu(self, pos):
        menu = MyContextMenu(plot=self)
        menu._exec(pos=pos)
        
    


    
class MyMainWindow(qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self._build()

    def _build(self):
        self._plot = MyPlotWidget()
        self.setCentralWidget(self._plot)

app = Qt.QApplication([])
main_window = MyMainWindow()
main_window.show()
app.exec()