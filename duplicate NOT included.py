
def byedupli():
    aubrey = input("Enter numbers: ")
    aubrey = list(aubrey)
    aub = []
    bree = []
    for i in aubrey:
        aubrey.count(i)
        if aubrey.count(i) != 1:
                aub.append(i)
        elif aubrey.count(i) == 1:
                bree.append(i)
    set(bree)
    print bree
    return(byedupli())
byedupli()
