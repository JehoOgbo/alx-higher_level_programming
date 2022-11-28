#!/usr/bin/python3
b = " is better than "
i = "If the implementation is easy to explain, it may be a good idea."
n = "never"
print(f"""The Zen of Python, by Tim Peters

Beautiful{b}ugly.
Explicit{b}implicit.
Simple{b}complex.
Complex{b}complicated.
Flat{b}nested.
Sparse{b}dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now{b}{n}.
Although {n} is often{b[3:]}*right* now.
{i[:25]}hard{i[29:44]}'s a bad idea.
{i}
Namespaces are one honking great idea -- let's do more of those!""")
