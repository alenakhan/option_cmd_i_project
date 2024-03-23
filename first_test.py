def hello(name):
    print(f'Hello, {name}!')


hello('April')


# изменения в коде


def sum(a, b):
    print(a + b)


sum(3, 8)


# Hello! It's me.

# Hello! This is my first commit

password = "hello123@1"
is_valid = True


for c in password:
    if c in "@_*":
        is_valid = False
        break
if is_valid:
    print("good password")
else:
    print("bad password")