def camel_sub(name):
    components = name.split('_')
    return print(components[0] + ''.join(x.title() for x in components[1:]))
