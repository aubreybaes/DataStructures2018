# EXERCISE NO. 8 -  QUEUES AND DEQUEUES
# Mae Aubrey C. Baes
# github.com/aubreybaes
# maeaubrey.baes@gmail.com
# This program accepts a range of integers and returns the number of even/odd numbers and the list of even/odd numbers in a given range

class ImQueue:
    def __init__(self):
        self.items = (list(range(a,b+1)))
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]


if __name__ =="__main__":

    a = input("Make a list of integers with a range \nfrom: ")
    b = input("to: ")
    s = ImQueue()
    x = 0
    k = (s.size()/2)-1
    hello = input("...OPTIONS... \n1. Get all even numbers\n2. Get all odd numbers\nSelect an action: ")
    if hello == 1:
        if b %2==0:
            while x<=k:
                s.enqueue(s.peek())
                s.dequeue()
                s.dequeue()
                x+=1
            print "\t",sorted(s.items)
            print "\t",a,"to",b,"contains",len(s.items),"even numbers"
        elif a%2==0 and b%2==1:
            while x<=k:
                s.dequeue()
                s.enqueue(s.peek())
                s.dequeue()
                x+=1
            print "\t",sorted(s.items)
            print "\t",a, "to", b, "contains", len(s.items), "even numbers"
        elif a%2==1and b%2==1:
            while x<=k+1:
                s.dequeue()
                s.enqueue(s.peek())
                s.dequeue()
                x+=1
            print "\t",sorted(s.items)
            print "\t",a, "to", b, "contains", len(s.items), "even numbers"

    elif hello == 2:
        if b %2==0:
            while x<=k:
                s.dequeue()
                s.enqueue(s.peek())
                s.dequeue()
                x+=1
            print "\t",sorted(s.items)
            print "\t",a, "to", b, "contains", len(s.items), "even numbers"
        elif a%2==0 and b%2==1:
            while x<=k:
                s.enqueue(s.peek())
                s.dequeue()
                s.dequeue()
                x+=1
            print "\t",sorted(s.items)
            print "\t",a, "to", b, "contains", len(s.items), "even numbers"
        elif a%2==1and b%2==1:
            while x<=k:
                s.enqueue(s.peek())
                s.dequeue()
                s.dequeue()
                x+=1
            print "\t",sorted(s.items)
            print "\t",a, "to", b, "contains", len(s.items), "even numbers"








