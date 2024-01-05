names = ["felix", "happy", "john", "faraday", "sunday", "betty", "falz"]

def find_characters_with_f(name):
    if name[0] == 'f':
        return name

# USING MAP 
map_name = map(find_characters_with_f, names)
for name in map_name:
     print(name)
"""
Output:
felix
None
None
faraday
None
None
falz
"""
# USING FILTER
filter_name = filter(find_characters_with_f, names)
for name in filter_name:
    print(name)
"""
Ouput:
felix
faraday
falz
"""