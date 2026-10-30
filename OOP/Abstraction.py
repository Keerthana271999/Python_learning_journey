# machine: Laptop actual duck but other bird has feature is a duck. gateway as chose in between the options


# So in both cases you can write either
# machine gateway
# machine: Laptop gateway: Payment


# So choose machine for options, machine: Laptop expected but there are other options scenario


# Abstraction - hiding complex implementation details from the use
# ABC - abstract base class

# importng ABC class and abstractmethod from abc package
from abc import ABC, abstractmethod
# ABC - abstract: not able to create object for that class
# base: you inherit
# class: class


class College(ABC):
    @abstractmethod
    def name(self):
        pass


class Surana(College):
    def name(self):
        print("College name: Surana")


class PES(College):
    def name(self,):
        print("College name: PES")


class Exam:
    def __init__(self, cn):
        self.cn = cn

    def name(self):
        print("Exam done")
        self.cn.name()


surana = Surana()
pes = PES()
exam = Exam(pes)
exam.name()
