from typing import Optional,Any
from Checks.checker import checks



@checks(list)
def check1(value: Optional[Any]=None ,*args):
    ans = value
    return ans


@checks(dict)
def check2(value: Optional[Any]= None,*args):
    ans = value
    return ans


@checks(tuple)
def check3(value: Optional[Any],*args):
    ans = value
    return ans


@checks(set)
def check4(value: Optional[Any] = None,*args):
    ans = value
    return ans


@checks(str)
def check5(value: Optional[Any]=None):
    ans = value
    return ans

@checks(int)
def check6(value:Optional[Any]=None ,*args):
    ans = value
    return ans


@checks(bool)
def check7(value: Optional[Any]=None ,*args):
    ans = value
    return ans

