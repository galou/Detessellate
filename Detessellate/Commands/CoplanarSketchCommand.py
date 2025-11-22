import os, sys
import FreeCAD
import FreeCADGui

class CoplanarSketchCommand:
    def GetResources(self):
        icon_path = os.path.join(
            os.path.dirname(__file__), "..", "Macros", "CoplanarSketch", "coplanarsketch.svg"
        )
        return {
            'Pixmap': icon_path,
            'MenuText': 'Coplanar Sketch',
            'ToolTip': 'Create sketches coplanar to selected faces'
        }

    def Activated(self):
        macro_path = os.path.join(os.path.dirname(__file__), "..", "Macros", "CoplanarSketch")
        macro_path = os.path.abspath(macro_path)
        if macro_path not in sys.path:
            sys.path.append(macro_path)

        try:
            import importlib
            if 'CoplanarSketch' in sys.modules:
                import CoplanarSketch
                importlib.reload(CoplanarSketch)
            else:
                import CoplanarSketch

            # The show_edge_data_collector_docker() runs on import/reload

        except Exception as e:
            FreeCAD.Console.PrintError(f"Error running CoplanarSketch: {e}\n")
            import traceback
            traceback.print_exc()

    def IsActive(self):
        return True
