#! /usr/bin/python3
import hm_01_引用
gl_name = "qwe"
gl_title = "wsss"

def demo1():
    # global gl_title
    gl_title = 00
    print(gl_title)

def demo2():
    print(gl_title)

demo1()
demo2()