mystuff={'apple':"I am apples"}
print mystuff['apple']

def apple():
    print "I am an apple"

# this is just a variable
tangerine = "Living reflection of a dream"

class Mystuff(object):
    
    # tan=100
    def __init__(self,lyrices):
        self.lyrices=lyrices
       

    def apple(self):
        print 10*"--"
        print "I am an apple"
        ly=self.lyrices.split(' ')
        # print ly
        for line in ly: 
            print line

        print 10*"**"
        i=0
        while i<len(ly):
            print ly[i]
            i=i+1
        
            
    
thing=Mystuff("you have a friend")
thing.apple()
# print thing.tan

print 10*"**"
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()