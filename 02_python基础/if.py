#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    height = 1.75
    weight = 80.5

    bmi = weight/(height*height)
    print(bmi)

    if bmi < 18.5:
        print("过轻")
    elif 18.5 <= bmi < 20.5:
        print("正常")
    elif 20.5 <= bmi < 28:
        print("过重")
    else:
        print("肥胖")