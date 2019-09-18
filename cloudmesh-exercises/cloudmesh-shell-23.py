# fa19-516-170 E.Cloudmesh.Shell.2 3

from cloudmesh.common.Shell import Shell

result = Shell.execute("cms", "yanting list")
print(result)

result = Shell.execute("cms", "yanting --file filename")
print(result)

#my command with modifying docopt in yanting.py
result = Shell.execute("cms", "yanting --text Hello")
print(result)