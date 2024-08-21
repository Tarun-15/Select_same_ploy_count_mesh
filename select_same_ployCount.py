import maya.cmds as cmds

def select_same_poly_count():
    selection = cmds.ls(sl = True)
    
    if not selection:
        print("Nothing Selected")
        return
    
    poly_count = cmds.polyEvaluate(selection[0], vertex=True)
    
    all_meshes = cmds.ls(type='mesh')
    same_poly_count_meshes = [mesh for mesh in all_meshes if cmds.polyEvaluate(mesh, vertex=True) == poly_count]
    
    cmds.select(same_poly_count_meshes)

select_same_poly_count()