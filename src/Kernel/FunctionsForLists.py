__author__ = 'luciano'

class FunctionsForLists:

    @staticmethod
    def filterList(functionForFilter,listF):
        return list(filter(functionForFilter, listF))

    @staticmethod
    def mapList(function,listM):
        return list(map(function,listM))

    @staticmethod
    def foldList(function,listM):
        return sum(FunctionsForLists.mapList(function,listM))

    @staticmethod
    def findFirst(functionForFilter,listF):
        return FunctionsForLists.filterList(functionForFilter, listF)[0]

    @staticmethod
    def exists(functionForFilter,listF):
        return FunctionsForLists.filterList(functionForFilter, listF).__len__() > 0