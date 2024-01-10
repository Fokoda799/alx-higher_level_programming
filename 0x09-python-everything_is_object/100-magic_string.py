# Content of 100-magic_string.py
def magic_string():
    magic_string.count = getattr(magic_string, 'count', -1) + 1
    return "BestSchool, " * magic_string.count + "BestSchool"
