from POM.Register_Page import Reg
from generic_utilities.read_excel import read
u,e,p=read()

def test_case(demo):
    register=Reg(demo)

    register.enter_name(u)
    register.enter_email(e)
    register.enter_pwdd(p)
    register.click_regbtn()










# class sample:
#     def __init__(self,a):
#         self.a=a
#
#     def disp(self,b):
#         print(b)
#
# o=sample(800)
# o.disp(20)




