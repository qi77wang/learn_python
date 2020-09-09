#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


if __name__ == '__main__':
    g = fib(6)
    while True:
        try:
            x = next(g)
            print("g:",x)
        except StopIteration as e:
            print("generator return value:", e)
            break
