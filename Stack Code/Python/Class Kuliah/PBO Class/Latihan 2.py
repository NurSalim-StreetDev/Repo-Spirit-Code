
from abc import ABC,abstractmethod

class Button(ABC):

    @abstractmethod
    def __init__(self,set_link):
        self.link = set_link

    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass


class PushButton(Button):
    def click(self):
        print("Go To: {}".format(self.link))

    @Button.link.setter
    def link(self,input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link



tombol1 = PushButton("Sistem Informasi")
tombol1.click()