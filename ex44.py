class Parent(object):
    def implicit(self):
        print "Parent function"

class Boy(Parent):
    
    def implicit(self):
        super(Boy,self).implicit()
        print "Boy function"


dad=Parent()
boy=Boy()

dad.implicit()
boy.implicit()

class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()