#create shape from mesh 
import Part
import Mesh

# fills holes of the 3 monomers
App.activeDocument().getObject("Best_cloneB_pdb_map_2_surface").Mesh.fillupHoles(3)
App.activeDocument().getObject("Best_cloneC_pdb_map_2_surface").Mesh.fillupHoles(3)
App.activeDocument().getObject("Best_cloneA_pdb_map_2_surface").Mesh.fillupHoles(3)
App.ActiveDocument.recompute()

#smooth objects
Gui.runCommand('Mesh_Smoothing',0)
App.ActiveDocument.recompute()

#making 1 mesh for each map provided (3 total)
App.getDocument('Unnamed').addObject('Part::Feature', 'Best_cloneC_pdb_map_2_surface001')
__shape__ = Part.Shape()
__shape__.makeShapeFromMesh(FreeCAD.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface').Mesh.Topology, 0.100000, False)
FreeCAD.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface001').Shape = __shape__
FreeCAD.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface001').purgeTouched()
del __shape__
App.getDocument('Unnamed').addObject('Part::Feature', 'Best_cloneA_pdb_map_2_surface002')
__shape__ = Part.Shape()
__shape__.makeShapeFromMesh(FreeCAD.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface').Mesh.Topology, 0.100000, False)
FreeCAD.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface002').Shape = __shape__
FreeCAD.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface002').purgeTouched()
del __shape__
App.getDocument('Unnamed').addObject('Part::Feature', 'Best_cloneB_pdb_map_2_surface003')
__shape__ = Part.Shape()
__shape__.makeShapeFromMesh(FreeCAD.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface').Mesh.Topology, 0.100000, False)
FreeCAD.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface003').Shape = __shape__
FreeCAD.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface003').purgeTouched()
del __shape__

#Produces solid out of mesh
import Part
__s__=App.ActiveDocument.Best_cloneC_pdb_map_2_surface001.Shape.Faces
__s__=Part.Solid(Part.Shell(__s__))
__o__=App.ActiveDocument.addObject("Part::Feature","Best_cloneC_pdb_map_2_surface001_solid")
__o__.Label="Best_cloneC_pdb_map_2_surface001_solid"
__o__.Shape=__s__
del __s__, __o__
__s__=App.ActiveDocument.Best_cloneA_pdb_map_2_surface002.Shape.Faces
__s__=Part.Solid(Part.Shell(__s__))
__o__=App.ActiveDocument.addObject("Part::Feature","Best_cloneA_pdb_map_2_surface002_solid")
__o__.Label="Best_cloneA_pdb_map_2_surface002_solid"
__o__.Shape=__s__
del __s__, __o__
__s__=App.ActiveDocument.Best_cloneB_pdb_map_2_surface003.Shape.Faces
__s__=Part.Solid(Part.Shell(__s__))
__o__=App.ActiveDocument.addObject("Part::Feature","Best_cloneB_pdb_map_2_surface003_solid")
__o__.Label="Best_cloneB_pdb_map_2_surface003_solid"
__o__.Shape=__s__
del __s__, __o__

#intersection of Monomer 1 and 2
App.activeDocument().addObject("Part::MultiCommon","Common")
App.activeDocument().Common.Shapes = [App.activeDocument().Best_cloneC_pdb_map_2_surface001_solid,App.activeDocument().Best_cloneA_pdb_map_2_surface002_solid,]
Gui.activeDocument().Best_cloneC_pdb_map_2_surface001_solid.Visibility=False
Gui.activeDocument().Best_cloneA_pdb_map_2_surface002_solid.Visibility=False
App.getDocument('Unnamed').getObject('Common').ViewObject.ShapeColor=getattr(App.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface001_solid').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('Unnamed').getObject('Common').ViewObject.ShapeColor)
App.getDocument('Unnamed').getObject('Common').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Best_cloneC_pdb_map_2_surface001_solid').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Common').ViewObject.DisplayMode)
App.ActiveDocument.recompute()

#intersection of Monomer 2 and 3
App.activeDocument().addObject("Part::MultiCommon","Common001")
App.activeDocument().Common001.Shapes = [App.activeDocument().Best_cloneA_pdb_map_2_surface002_solid,App.activeDocument().Best_cloneB_pdb_map_2_surface003_solid,]
Gui.activeDocument().Best_cloneA_pdb_map_2_surface002_solid.Visibility=False
Gui.activeDocument().Best_cloneB_pdb_map_2_surface003_solid.Visibility=False
App.getDocument('Unnamed').getObject('Common001').ViewObject.ShapeColor=getattr(App.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface002_solid').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('Unnamed').getObject('Common001').ViewObject.ShapeColor)
App.getDocument('Unnamed').getObject('Common001').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Best_cloneA_pdb_map_2_surface002_solid').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Common001').ViewObject.DisplayMode)
App.ActiveDocument.recompute()

#intersection of Monomer 1 and 3
App.activeDocument().addObject("Part::MultiCommon","Common002")
App.activeDocument().Common002.Shapes = [App.activeDocument().Best_cloneB_pdb_map_2_surface003_solid,App.activeDocument().Best_cloneC_pdb_map_2_surface001_solid,]
Gui.activeDocument().Best_cloneB_pdb_map_2_surface003_solid.Visibility=False
Gui.activeDocument().Best_cloneC_pdb_map_2_surface001_solid.Visibility=False
App.getDocument('Unnamed').getObject('Common002').ViewObject.ShapeColor=getattr(App.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface003_solid').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('Unnamed').getObject('Common002').ViewObject.ShapeColor)
App.getDocument('Unnamed').getObject('Common002').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Best_cloneB_pdb_map_2_surface003_solid').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Common002').ViewObject.DisplayMode)
App.ActiveDocument.recompute()

App.ActiveDocument.Common.Shape.Volume
App.ActiveDocument.Common001.Shape.Volume
App.ActiveDocument.Common002.Shape.Volume

#Makes trimer invisible AND removes the original map
FreeCAD.ActiveDocument.removeObject("Best_cloneB_pdb_map_2_surface")
FreeCAD.ActiveDocument.removeObject("Best_cloneA_pdb_map_2_surface")
FreeCAD.ActiveDocument.removeObject("Best_cloneC_pdb_map_2_surface")

Gui.Selection.clearSelection()
Gui.Selection.addSelection('Unnamed','Best_cloneC_pdb_map_2_surface001')
Gui.Selection.addSelection('Unnamed','Best_cloneA_pdb_map_2_surface002')
Gui.Selection.addSelection('Unnamed','Best_cloneB_pdb_map_2_surface003')
Gui.runCommand('Std_ToggleVisibility',0)

#Outputs trimer, intersection and steric clashing values
intersectvol = App.ActiveDocument.Common.Shape.Volume+App.ActiveDocument.Common001.Shape.Volume+App.ActiveDocument.Common002.Shape.Volume
trimervol = App.ActiveDocument.Best_cloneC_pdb_map_2_surface001.Shape.Volume+App.ActiveDocument.Best_cloneA_pdb_map_2_surface002.Shape.Volume+App.ActiveDocument.Best_cloneB_pdb_map_2_surface003.Shape.Volume
clashing = intersectvol/trimervol*100

print("Total volume of trimer intersect = {} Units ".format(intersectvol))
print("Total volume of the trimer = {} Units".format(trimervol))
print("Steric Clashing = {}%".format(clashing))

#saves file
App.getDocument("Unnamed").saveAs(u"C:/Users/User/Desktop/Finished trimers/Finished Trimer.FCStd")

#App.getDocument('Unnamed').getObject(Best_cloneC_pdb_map_2_surface0001).ViewObject.ShapeColor = (0.4, 0.5, 0.3, 1.0) colour commands