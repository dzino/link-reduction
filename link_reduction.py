#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class LinkReduction:

    def __init__(self):
        pass

    @staticmethod
    def generation(old_url):
        ":type  old_url: str"
        array = old_url.split("://")
        return array[1]


if __name__ == '__main__':
    obj = LinkReduction()
    new_url = obj.generation("https://yandex.ru")
    del obj
    print(new_url)
