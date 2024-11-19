import inspect



class A:
    a: int
    def b(self,c):
        pass
def introspection_info(obj):
    d = {}
    d['type'] = type(obj).__name__
    for member in inspect.getmembers(obj):
        print(member)
        print(inspect.ismethod(member[1]), member[1])
    d['methods'] = []
    d['attributes'] = []
    for attr in dir(obj):
        attr_obj =  getattr(obj, attr)
        if callable(attr_obj):
            d['methods'].append(attr_obj)
        else:
            d['attributes'].append(attr_obj)
    d['module'] = inspect.getmodule(obj)
    return d

print(*introspection_info(A()), sep = '\n')