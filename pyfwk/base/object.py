#!/usr/bin/env python

"""
  object.py: instance methods for extending data objects
"""


# -----------------------ABSTRACT-BASE-CLASS-OBJECT-----------------------#
class Object:
    def alloc(self):
        return self

    def name(self):
        return self.__class__.__name__

    def dict(self):
        odc = self.__dict__
        dct = {}
        for key in odc:
            obj = odc[key]
            if (isinstance(obj, unicode)):
                dct[key] = obj
            elif (isinstance(obj, int)):
                dct[key] = str(obj)
            else:
                obj = odc[key]
                dct[key] = obj.dict()
        return dct


# ---------------------------------EXPORT---------------------------------#
__all__ = ['Object']


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
