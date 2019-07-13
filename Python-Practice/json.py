
import json

x = {"name":"Shital", "surname":"bhandare", "age":23,"bacherlor":True}
#print(json.dumps(x, indent = 3, separators = (", "," = "), sort_keys = True))
y = json.dumps(x, indent = 3, separators = (", "," = "), sort_keys = True)
print(y)


p = json.dumps([1, 2, (4, 5)])
z = json.loads(p)
print(z[0])


Output =>
{
   "age" = 23, 
   "bacherlor" = true, 
   "name" = "Shital", 
   "surname" = "bhandare"
}
1