#/usr/bin/python

def scan(string):

    dict={'direction':['north','south','west','east','down','up','left','right'],
    'verb':['go','stop','kill','eat'],
    'stop':['the','in','of','from','at','it'],
    'noun':['door','bear','princess','cabinet']}
    
    words=string.split()
    # print "Your scetence have been split to:",words
    result=[]
    
    for word in words:
        flag=False 
        if word.isdigit():
            flag=True
            result.append(('number',int(word)))
        else:
            for word_key,word_values in dict.items():
                if word in word_values:
                    flag=True
                    result.append((word_key,word))
                    
        if flag==False:
            result.append(('error',word))
    
    # print result
    return result
    
    
# scan("you name bear in go 123 from")

