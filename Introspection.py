import inspect



class A:
    a: int
    def __init__(self):
        self.a = 10
    def b(self,c):
        pass
def introspection_info(obj):
    d = {}
    d['type'] = type(obj).__name__
    d['attributes'] = []
    d['methods'] = []
    for i in inspect.getmembers(obj):
        if inspect.ismethod(getattr(obj, i[0])):
            d['methods'].append(i[0])
        elif inspect.isbuiltin(getattr(obj, i[0])):
            d['methods'].append(i[0])
        elif inspect.isfunction(getattr(obj, i[0])):
            d['methods'].append(i[0])
        elif inspect.ismethodwrapper(getattr(obj, i[0])):
            d['methods'].append(i[0])
        else:
            d['attributes'].append(i[0])
    d['module'] = getattr(obj, '__module__')
    return d

print(introspection_info(A()), sep = '\n')