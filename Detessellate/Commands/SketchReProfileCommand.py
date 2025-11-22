import os, sys
import FreeCAD
import FreeCADGui

class SketchReProfileCommand:
    def GetResources(self):
        icon_path = os.path.join(
            os.path.dirname(__file__), "..", "Macros", "SketchReProfile", "sketchreprofile.svg"
        )
        return {
            'Pixmap': icon_path,
            'MenuText': 'Sketch ReProfile',
            'ToolTip': 'Reprocess sketch profiles - converts construction lines to circles, arcs, and splines'
        }

    def Activated(self):
        macro_path = os.path.join(os.path.dirname(__file__), "..", "Macros", "SketchReProfile")
        macro_path = os.path.abspath(macro_path)
        if macro_path not in sys.path:
            sys.path.append(macro_path)

        try:
            import importlib
            if 'SketchReProfile' in sys.modules:
                import SketchReProfile
                importlib.reload(SketchReProfile)
            else:
                import SketchReProfile

            # Call the main function
            SketchReProfile.final_sketcher_main()

        except Exception as e:
            FreeCAD.Console.PrintError(f"Error running SketchReProfile: {e}\n")
            import traceback
            traceback.print_exc()

    def IsActive(self):
        # Active when a sketch is being edited
        try:
            doc = FreeCADGui.activeDocument()
            if doc is None:
                return False

            edit_obj = doc.getInEdit()
            if edit_obj is None:
                return False

            # Check if it's a sketch object
            if hasattr(edit_obj, 'Object'):
                obj = edit_obj.Object
                return hasattr(obj, 'TypeId') and 'Sketch' in obj.TypeId

            return False
        except:
            return False
