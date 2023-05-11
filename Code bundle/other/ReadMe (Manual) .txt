Programs needed:
Python 3.11
PyMol (PyMol2)
UCSF ChimeraX version: 1.5
FreeCAD 0.20.2

Make files named:
ChimeraX alphafold prediction library
Pre-processed trimers
Trimer_map
Finished trimers

Code uses the directory path:
C:\Users\User\Desktop\'name of file above'



Protocol:

Produce sequence of interest for RGNNV virus (1)

Model prediction (2)
ChimeraX - Tools -> structure prediction -> AlphaFold. Paste your sequence in the popup + press predict.
Once folded, file should be in downloads under 'chimeraX' folder. Open 'prediction_1' and 'Best_model.pdb'

Trimer Assembly (3)
load your 'Best_model' (or VLP of interest, must be renamed 'Best_model.pdb') in pymol.
Drag 'Trimer code.py' and drop. Close program. 

Trimer Map transformation (4)
Copy and paste text into chimeraX command line, press enter.
Close program

Steric Clashing (5)
Load FreeCad and Drag 'test_trimer' file into the Comboview window and select WaveOBJ (loading the file from an icon/ folder causes an issue.)
Open Python shell using View -> Panels -> Python console.
Drag 'CAD.PY' into the console