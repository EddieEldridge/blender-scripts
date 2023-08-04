import bpy

for obj in bpy.context.selected_objects :
    for uvmap in  obj.data.uv_layers :
        print("\n")
        print("Renaming UV Map: ", uvmap.name)
        uvmap.name = 'UVMap'
        print("New Name: ", uvmap.name)
