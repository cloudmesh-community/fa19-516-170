from cloudmesh.common.dotdict import dotdict

color = {"red": 255, "blue": 255, "green": 255, "alpha": 0}
color = dotdict(color)

print("A RGB color: ", color.red, color.blue, color.green, color.alpha)