def display_good(fn):
    def wrapper(st):
        print("OutPut :", end='!!!')
        fn(st+'!!!')
    return wrapper


@display_good
def display(st):
    print(st)


display('Python')
display('Calsoft')
