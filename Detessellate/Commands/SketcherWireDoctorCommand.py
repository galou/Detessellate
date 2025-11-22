import os, sys
import FreeCAD
import FreeCADGui

class SketcherWireDoctorCommand:
    def GetResources(self):
        icon_path = os.path.join(
            os.path.dirname(__file__), "..", "Macros", "SketcherWireDoctor", "sketcherwiredoctor.svg"
        )
        return {
            'Pixmap': icon_path,
            'MenuText': 'Sketcher Wire Doctor',
            'ToolTip': 'Fix sketch wire issues'
        }

    def Activated(self):
        macro_path = os.path.join(os.path.dirname(__file__), "..", "Macros", "SketcherWireDoctor")
        macro_path = os.path.abspath(macro_path)
        if macro_path not in sys.path:
            sys.path.append(macro_path)

        try:
            import importlib
            if 'SketcherWireDoctor' in sys.modules:
                import SketcherWireDoctor
                importlib.reload(SketcherWireDoctor)
            else:
                import SketcherWireDoctor

            # Call the appropriate function based on the macro

        except Exception as e:
            FreeCAD.Console.PrintError(f"Error running SketcherWireDoctor: {e}\n")
            import traceback
            traceback.print_exc()

    def IsActive(self):
        # Active when a sketch is being edited
        return True #FreeCADGui.activeDocument() is not None and FreeCADGui.ActiveDocument.getInEdit() is not None
