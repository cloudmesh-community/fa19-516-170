from cloudmesh.common.Shell import Shell

result = Shell.pwd()
print("the working directory is in ", result)

print("----------------------------------------------")
result = Shell.ls()
print("the working directory has ", result)

print("----------------------------------------------")
print("check what the contents in cloudmesh-common-1.py are:  ")
result = Shell.execute("cat", "cloudmesh-common-1.py")
print(result)
