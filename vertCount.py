import bpy

for obj in bpy.context.selected_objects :
    print("\n")
    print("Object Name: ", obj.name)
    print("Vert Count: ", len(obj.data.vertices))
        