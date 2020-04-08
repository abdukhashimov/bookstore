from django.db.models.signals import post_save, post_delete
from rx import Observable
from django.db import models
from threading import Thread
from timeit import default_timer as timer


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class Book(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tracker(Singleton, object):
    def __init__(self, *args, **kwargs):
        self.__count = self.__get_count()

    def __get_count(self):
        print("Retreiving from Database")
        t1 = timer()
        count = Book.objects.all().count()
        t2 = timer()
        print("Retreived in {} seconds".format(t2 - t1))
        return count

    @property
    def count(self):
        print("Getting Counter")
        return self.__count

    @count.setter
    def set_count(self, count):
        print("Setting Counter")
        self.__count = count


def threaded_function():
    print("Counting All Objects")
    t1 = timer()
    tracker = Tracker()
    tracker.set_count = Book.objects.all().count()
    t2 = timer()
    print("Finished Counting")
    print("Time: ", t2 - t1)
    print("I have finished")
    return 0


def update_record_count(sender, **kwargs):
    print("Action: Save/Delete")
    thread = Thread(target=threaded_function)
    thread.start()
    print("Main thread")


post_save.connect(update_record_count, sender=Book)
post_delete.connect(update_record_count, sender=Book)

tracker = Tracker()
