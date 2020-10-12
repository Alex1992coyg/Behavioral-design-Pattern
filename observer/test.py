#!/usr/bin/env python3

from observer.observer_example import *

subject = ConcreteSubject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.business_logic()
subject.business_logic()

subject.detach(observer_a)

subject.business_logic()
