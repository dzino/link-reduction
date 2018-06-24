#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class main:

    def __init__(self):
        pass

    def generation(self, old_url):
        ":type  old_url: str"
        array = old_url.split("://")
        return array[1]

if __name__ == '__main__':
    obj = main()
    new_url = obj.generation("https://yandex.ru")
    del(obj)
