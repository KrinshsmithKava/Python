from abc import ABC, abstractmethod


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


# Example of Duck Typing

class Dog:
    def speak(self):
        print("Bark")


class Person:
    def speak(self):
        print("Hello")


def make_sound(obj):
    obj.speak()   # Python doesn't care what obj is


make_sound(Dog())
make_sound(Person())
