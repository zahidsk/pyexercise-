class  Method:
    def __init__(self):
        Method.obj_count += 1

    @classmethod
    def display(cls):
        print(cls.obj_count)
