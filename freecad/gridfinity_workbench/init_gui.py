import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.gridfinity_workbench import ICONPATH

try:
    from FreeCADGui import Workbench
except ImportError as e:
    App.Console.PrintWarning(
        "you are using the GearWorkbench with an old version of FreeCAD (<0.16)")
    App.Console.PrintWarning(
        "the class Workbench is loaded, although not imported: magic")

class GridfinityWorkbench(Workbench):
    """
    class which gets initiated at starup of the gui
    """
    MenuText = "Gridfinity"
    ToolTip = "FreeCAD Gridfinity Workbench"
    Icon = os.path.join(ICONPATH, "gridfinity_workbench_icon.svg")
    toolbox = [
        "CreateBinBlank",
        "CreateSimpleStorageBin",
        "CreateBaseplate"]

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        from .commands import CreateBinBlank
        from .commands import CreateSimpleStorageBin
        from .commands import CreateBaseplate
        App.Console.PrintMessage("switching to Gridfinity Workbench\n")

        self.appendToolbar("Tools", self.toolbox)
        self.appendMenu("Tools", self.toolbox)
        Gui.addCommand('CreateBinBlank', CreateBinBlank())
        Gui.addCommand('CreateSimpleStorageBin', CreateSimpleStorageBin())
        Gui.addCommand('CreateBaseplate', CreateBaseplate())

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        pass

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        pass


Gui.addWorkbench(GridfinityWorkbench())
