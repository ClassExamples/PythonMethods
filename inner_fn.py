def hello(name="World"):

    def print_name():
        print("Hello ",name)   

    return print_name

if __name__ == "__main__":
    v = hello()
    print(v)
    v()
    hello("Test ")()