
from typing import List


class ListUtils:

    @staticmethod
    def findByAttr(iter :List,itemsAttr,attrValue) -> List:
        return [item for item in iter if getattr(item, itemsAttr) == attrValue]


    @staticmethod
    def countByAttr(iter :List,itemsAttr,attrValue) -> int:
        return len(ListUtils.findByAttr(iter,itemsAttr,attrValue))


    @staticmethod
    def uniqByAttr(inputList :List,itemsAttr,attrValue):
        items = ListUtils.findByAttr(inputList,itemsAttr,attrValue)
        if len(items) > 1:
            raise ValueError("Several items meet the condition ")
        return next(iter(items),None)


    @staticmethod
    def addUniqByAttr(iter :List,item,itemsAttr,attrValue):
        if ListUtils.uniqByAttr(iter,itemsAttr,attrValue) == None:
            iter.append(item)
        else:
            raise Exception("List already contains an item with the {} attribute equals {}".format(
                itemsAttr,
                attrValue
            ))
