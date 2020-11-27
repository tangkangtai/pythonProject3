class Dict(dict):
    def __init__(self,**kw):
        #父函数  ()
        super().__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError("'Dict' object has no attribute '%s'" % item)


    def __setattr__(self, key, value):
        self[key] = value

# d = Dict()
# value = d.empty
# print(value)