class Link:
    def __init__(self,i,dd):
        self.iData = i
        self.dData = dd
        self.next = None

    def displayLink(self): # display ourself
        print '{'  , self.iData , ', ' , self.dData , '} ' ,

class LinkList:
    def __init__(self):
        self.first = None

    def isEmpty(self): 
        return (self.first==None)

    # insert at start of list
    def insertFirst(self,i,  dd):
        # make new link
        newLink = Link(i, dd)
        newLink.next = self.first
        # newLink --> old first
        self.first = newLink

    def deleteFirst(self):
        temp = self.first
        self.first = self.first.next
        return temp
    
    def displayList(self):
        print 'List (first-->last): ' ,
        current = self.first
        while(current != None):
            current.displayLink()
            current = current.next
        print ''

theList = LinkList() # make new list
theList.insertFirst(22,2.99)
theList.insertFirst(44,4.99)
theList.insertFirst(66,6.99)
theList.insertFirst(88,8.99)
theList.displayList()

while( not theList.isEmpty() ): 
    aLink = theList.deleteFirst()
    print 'Deleted ' ,  
    aLink.displayLink()
    print ''
    
theList.displayList()