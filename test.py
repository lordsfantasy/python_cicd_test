import os
import ast

print(ast.literal_eval("1+15"))
print(ast.literal_eval("os.getcwd()"))
print(ast.literal_eval("os.chmod('%s', 0777)" % 'test.txt'))


# A user-defined method named "eval" should not get flagged.
class Test(object):
    def eval(self):
        print("hi")
    def foo(self):
        self.eval()

Test().eval()
