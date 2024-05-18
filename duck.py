class pychaem:
    def execute(self):
        print("comiling")
        print("running")

class myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")

class laptop:
    def code(self,ide):
        ide.execute()
ide = myeditor()
lap1=laptop()
lap1.code(ide)

