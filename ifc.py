import pprint as pp
import ifcopenshell.util.element

model = ifcopenshell.open("Duplex.ifc")

Spaces = model.by_type("IfcSpace")

#pp.pprint(Spaces)

for space in Spaces:
    print(f'Space: {space.Name}, LongName: {space.LongName}, GUID: {space.GlobalId}')

print()
option = int(input("Enter option number (1/2/3):"))
#option = 3
if option == 1:
    walls = model.by_type("IfcWall")
    for wall in walls:
        print(f'Wall: {wall.Name}, GUID: {wall.GlobalId}')
elif option == 2:
    windows = model.by_type("IfcWindow")
    for window in windows:
        print(f'Window: {window.Name}, GUID: {window.GlobalId}')
elif option == 3:
    doors = model.by_type("IfcDoor")
    for door in doors:
        print(f'Door: {door.Name}, GUID: {door.GlobalId}')
else:
    print("Invalid option number.")


room = Spaces[2]

Pset = ifcopenshell.util.element.get_psets(room)
pp.pprint(Pset)


walls = model.by_type("IfcWall")
print(f"Liczba ścian w modelu: {len(walls)}")

ext = []
for wall in walls:
    Pset = ifcopenshell.util.element.get_psets(wall)
    if Pset["Pset_WallCommon"]["IsExternal"]:
        ext.append(wall)

print(f'Liczba ścian zewnętrznych w modelu: {len(ext)}')

totalvolume = 0
for wall in ext:
    psets = ifcopenshell.util.element.get_psets(wall)
    for psetname, pset_dict in psets.items():
        for name, value in pset_dict.items():
            if name == "NetVolume":
                totalvolume += float(value)

print(f'TotalVolume: {totalvolume:.2f}')





