def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)   
    lst = list()
    for line in handle:
        line = line.strip()
        if line.startswith("From "):
            words = line.split()
            email = words[1]
            lst.append(email)

    dct = dict()
    for email in lst:
        dct[email] = dct.get(email,0)+1

    bigcount = None
    bigword = None
    for email, dct in dct.items():
        if bigcount is None or dct > bigcount:
            bigcount = dct
            bigword = email

    print(bigword, bigcount)


        
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countEmail()
