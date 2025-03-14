from pathlib import Path # Path is is an class

path=Path("classes")
print(path.exists())

path=Path("fun")
path.rmdir()
path.mkdir()



path=Path()
for item in path.glob("*.py"):  #type "*.* "
    print(item)

