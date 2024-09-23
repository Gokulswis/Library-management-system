class library:
    def __init__(self):
        self.data={}
        self.issued={}
    def add(self):
        count=int(input("How much book u add: "))
        for i in range(count):
            a=input("Enter the book name: ")
            if a not in self.data:
                self.data[a]=1
            else:
                self.data[a]+=1
        print("your books added successfully")
    def view(self):
        print("press 1 for library books")
        print("press 2 for issued books")
        try:
            sel=int(input("Enter your option: "))
            if sel==1:
                if self.data=={}:
                   print("No Books available in library")
                else:
                   print("The library books are ")
                   for i,j in self.data.items():
                      print("{}={}".format(i,j))
            elif sel==2:
                if self.issued=={}:
                   print("No Books issued")
                else:
                   print("The issued books are ")
                   for x,y in self.issued.items():
                       print("{}={}".format(x,y))
            else:
                print("Enter only 1 or 2")
        except:
            print("String not accepted Press only 1 or 2")
    def issue(self):
        d=input("Enter the book name: ")
        if d in self.data:
            if self.data[d]!=0:
                self.data[d]-=1
                print("your book is issued")
                if d not in self.issued:
                    self.issued[d]=1
                else:
                    self.issued[d]+=1
            else:
                print("That book out of stock")
        else:
            print("Invalid book name")
    def ret(self):
        if self.issued=={}:
            print("You not have books")
        elif self.issued!={}:
            e=input("Enter the book name: ")
            if e in self.issued:
                if self.issued[e]!=0:
                    self.issued[e]-=1
                    print("your book is returned")
                    if self.issued[e]==0:
                        self.issued.pop(e)
                    if e in self.data:
                        self.data[e]+=1
                    else:
                        self.data[e]=1
                else:
                    print("You already return all the books")
            else:
                print("Invalid book name")
    def delete(self):
        if self.data=={}:
            print("NO books available to delete")
        else:
            f=input("Enter the book to delete: ")
            if f in self.data:
                self.data.pop(f)
                print("book is deleted")
            else:
                print("Invalid book name")
            
        
obj=library()
while True:
    print("\n")
    print("Press 1 for Add book")
    print("Press 2 for view books")
    print("Press 3 for Issue books")
    print("Press 4 for Return books")
    print("Press 5 for delete books")
    print("Press 6 for Exit")
    try:
        data=int(input("Enter your choice: "))
        print("\n")
        if data==1:
           obj.add()
        elif data==2:
           obj.view()
        elif data==3:
           obj.issue()
        elif data==4:
           obj.ret()
        elif data==5:
           obj.delete()
        else:
           quit()
    except :
        print("Please enter only 1 to 5 for access library ")

