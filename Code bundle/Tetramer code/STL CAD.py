#create shape from mesh 
import Part
import Mesh

# fills holes of the 4 monomers
App.activeDocument().getObject("Best_cloneB_pdb_map_2_surface").Mesh.fillupHoles(3)
App.activeDocument().getObject("Best_cloneC_pdb_map_2_surface").Mesh.fillupHoles(3)
App.activeDocument().getObject("Best_cloneA_pdb_map_2_surface").Mesh.fillupHoles(3)
App.activeDocument().getObject("Best_cloneD_pdb_map_2_surface").Mesh.fillupHoles(3)
App.ActiveDocument.recompute()

#smooth objects
Gui.runCommand('Mesh_Smoothing',0)
App.ActiveDocument.recompute()

#making 1 mesh for each map provided (4 total)
App.getDocument('Unnamed').addObject('Part::Feature', 'Best_cloneC_pdb_map_2_surface001')
__shape__ = Part.Shape()
__shape__.makeShapeFromMesh(FreeCAD.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface').Mesh.Topology, 0.100000, False)
FreeCAD.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface001').Shape = __shape__
FreeCAD.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface001').purgeTouched()
del __shape__
App.getDocument('Unnamed').addObject('Part::Feature', 'Best_cloneA_pdb_map_2_surface001')
__shape__ = Part.Shape()
__shape__.makeShapeFromMesh(FreeCAD.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface').Mesh.Topology, 0.100000, False)
FreeCAD.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface001').Shape = __shape__
FreeCAD.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface001').purgeTouched()
del __shape__
App.getDocument('Unnamed').addObject('Part::Feature', 'Best_cloneB_pdb_map_2_surface001')
__shape__ = Part.Shape()
__shape__.makeShapeFromMesh(FreeCAD.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface').Mesh.Topology, 0.100000, False)
FreeCAD.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface001').Shape = __shape__
FreeCAD.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface001').purgeTouched()
del __shape__
App.getDocument('Unnamed').addObject('Part::Feature', 'Best_cloneD_pdb_map_2_surface001')
__shape__ = Part.Shape()
__shape__.makeShapeFromMesh(FreeCAD.getDocument('Unnamed').getObject('Best_cloneD_pdb_map_2_surface').Mesh.Topology, 0.100000, False)
FreeCAD.getDocument('Unnamed').getObject('Best_cloneD_pdb_map_2_surface001').Shape = __shape__
FreeCAD.getDocument('Unnamed').getObject('Best_cloneD_pdb_map_2_surface001').purgeTouched()
del __shape__

#Produces solid out of mesh
import Part
__s__=App.ActiveDocument.Best_cloneC_pdb_map_2_surface001.Shape.Faces
__s__=Part.Solid(Part.Shell(__s__))
__o__=App.ActiveDocument.addObject("Part::Feature","Best_cloneC_pdb_map_2_surface001_solid")
__o__.Label="Best_cloneC_pdb_map_2_surface001_solid"
__o__.Shape=__s__
del __s__, __o__
__s__=App.ActiveDocument.Best_cloneA_pdb_map_2_surface001.Shape.Faces
__s__=Part.Solid(Part.Shell(__s__))
__o__=App.ActiveDocument.addObject("Part::Feature","Best_cloneA_pdb_map_2_surface001_solid")
__o__.Label="Best_cloneA_pdb_map_2_surface001_solid"
__o__.Shape=__s__
del __s__, __o__
__s__=App.ActiveDocument.Best_cloneB_pdb_map_2_surface001.Shape.Faces
__s__=Part.Solid(Part.Shell(__s__))
__o__=App.ActiveDocument.addObject("Part::Feature","Best_cloneB_pdb_map_2_surface001_solid")
__o__.Label="Best_cloneB_pdb_map_2_surface001_solid"
__o__.Shape=__s__
del __s__, __o__
__s__=App.ActiveDocument.Best_cloneD_pdb_map_2_surface001.Shape.Faces
__s__=Part.Solid(Part.Shell(__s__))
__o__=App.ActiveDocument.addObject("Part::Feature","Best_cloneD_pdb_map_2_surface001_solid")
__o__.Label="Best_cloneD_pdb_map_2_surface001_solid"
__o__.Shape=__s__
del __s__, __o__

############################################################################## EVERYTHING ABOVE EDITED FOR TETRAMERS
#WANT A-B, C-D and B-C
#     2-3, 1-4 and 1-3
#intersection of Monomer 1 and 4
App.activeDocument().addObject("Part::MultiCommon","Common")
App.activeDocument().Common.Shapes = [App.activeDocument().Best_cloneC_pdb_map_2_surface001_solid,App.activeDocument().Best_cloneD_pdb_map_2_surface001_solid,]
Gui.activeDocument().Best_cloneC_pdb_map_2_surface001_solid.Visibility=False
Gui.activeDocument().Best_cloneD_pdb_map_2_surface001_solid.Visibility=False
App.getDocument('Unnamed').getObject('Common').ViewObject.ShapeColor=getattr(App.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface001_solid').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('Unnamed').getObject('Common').ViewObject.ShapeColor)
App.getDocument('Unnamed').getObject('Common').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface001_solid').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Common').ViewObject.DisplayMode)
App.ActiveDocument.recompute()

#intersection of Monomer 2 and 3
App.activeDocument().addObject("Part::MultiCommon","Common001")
App.activeDocument().Common001.Shapes = [App.activeDocument().Best_cloneA_pdb_map_2_surface001_solid,App.activeDocument().Best_cloneB_pdb_map_2_surface001_solid,]
Gui.activeDocument().Best_cloneA_pdb_map_2_surface001_solid.Visibility=False
Gui.activeDocument().Best_cloneB_pdb_map_2_surface001_solid.Visibility=False
App.getDocument('Unnamed').getObject('Common001').ViewObject.ShapeColor=getattr(App.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface001_solid').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('Unnamed').getObject('Common001').ViewObject.ShapeColor)
App.getDocument('Unnamed').getObject('Common001').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface001_solid').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Common001').ViewObject.DisplayMode)
App.ActiveDocument.recompute()

#intersection of Monomer 1 and 3
App.activeDocument().addObject("Part::MultiCommon","Common002")
App.activeDocument().Common002.Shapes = [App.activeDocument().Best_cloneB_pdb_map_2_surface001_solid,App.activeDocument().Best_cloneC_pdb_map_2_surface001_solid,]
Gui.activeDocument().Best_cloneB_pdb_map_2_surface001_solid.Visibility=False
Gui.activeDocument().Best_cloneC_pdb_map_2_surface001_solid.Visibility=False
App.getDocument('Unnamed').getObject('Common002').ViewObject.ShapeColor=getattr(App.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface001_solid').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('Unnamed').getObject('Common002').ViewObject.ShapeColor)
App.getDocument('Unnamed').getObject('Common002').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface001_solid').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Common002').ViewObject.DisplayMode)
App.ActiveDocument.recompute()

App.ActiveDocument.Common.Shape.Volume
App.ActiveDocument.Common001.Shape.Volume
App.ActiveDocument.Common002.Shape.Volume

#Makes trimer invisible AND removes the original map
FreeCAD.ActiveDocument.removeObject("Best_cloneB_pdb_map_2_surface")
FreeCAD.ActiveDocument.removeObject("Best_cloneA_pdb_map_2_surface")
FreeCAD.ActiveDocument.removeObject("Best_cloneC_pdb_map_2_surface")
FreeCAD.ActiveDocument.removeObject("Best_cloneD_pdb_map_2_surface")

Gui.Selection.clearSelection()
Gui.Selection.addSelection('Unnamed','Best_cloneC_pdb_map_2_surface001')
Gui.Selection.addSelection('Unnamed','Best_cloneA_pdb_map_2_surface001')
Gui.Selection.addSelection('Unnamed','Best_cloneB_pdb_map_2_surface001')
Gui.Selection.addSelection('Unnamed','Best_cloneD_pdb_map_2_surface001')
Gui.runCommand('Std_ToggleVisibility',0)

intersectvol = App.ActiveDocument.Common.Shape.Volume+App.ActiveDocument.Common001.Shape.Volume+App.ActiveDocument.Common002.Shape.Volume
tetramervol = App.ActiveDocument.Best_cloneC_pdb_map_2_surface001.Shape.Volume+App.ActiveDocument.Best_cloneA_pdb_map_2_surface001.Shape.Volume+App.ActiveDocument.Best_cloneB_pdb_map_2_surface001.Shape.Volume+App.ActiveDocument.Best_cloneD_pdb_map_2_surface001.Shape.Volume
clashing = intersectvol/tetramervol*100

print("Total volume of tetramer intersect = {} Units ".format(intersectvol))
print("Total volume of the tetramer = {} Units".format(tetramervol))
print("Steric Clashing = {} %".format(clashing))