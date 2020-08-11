#!/usr/bin/env python3
# Amazon Linux 2

def say_hi():
    print("Hello World!")
    return {"Hello World!\n"}


def main():
    say_hi()


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
