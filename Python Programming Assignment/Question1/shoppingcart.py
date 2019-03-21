import pickle
import os

class Products:
    def __init__(self,Name,Group,Subgroup,Price):
        if os.path.isfile("product.pickle"):
            try:
                infile = open("product.pickle","rb")
                prods = pickle.load(infile)
                infile.close()
                ids = prods.keys()
                self.__id = max(ids) + 1
            except:
                self.__id=1
            else:
                self.__id=1
                self._Name=Name
                self._Group=Group
                self._Subgroup=Subgroup
                self._Price=Price
#Value Getters and setters
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id

    def getName(self):
        return self._Name
    def setName(self,Name):
        self._Name=Name

    def getPrice(self):
        return self._Price
    def setPrice(self,Price):
        self._Price=Price
    
    def getGroup(self):
        return self._Group
    def setGroup(self,Group):
        self._Group=Group

    def getSubgroup(self):
        return self._Subgroup
    def setSubgroup(self,Subgroup):
        self._Subgroup=Subgroup



class Admin:
    def __init__(self,Name):
        self.__id=1
        self.__Name=Name

#Value Getters and setters
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id

    def getName(self):
        return self.__Name
    def setName(self,Name):
        self.__Name=Name

    def AddProduct(self):
        try:
            Name = raw_input("Enter Product Name: ")
            Price = int(raw_input("Enter Product Price: "))
            Group = raw_input("Enter Product Group: ")
            Subgroup = raw_input("Enter Product Subgroup: ")
            p = Products(Name,Group,Subgroup,Price)
            prods = {1:Products}
            prods.clear()
            
            if os.path.isfile("product.pickle"):
                try:
                    infile = open("product.pickle","rb")
                    prods = pickle.load(infile)
                    infile.close()
                    prods[p.getId()] = p
                    infile = open("product.pickle","wb")
                    pickle.dump(prods,infile)
                    infile.close()
                except:
                    prods[p.getId()] = p
                    infile = open("product.pickle", 'wb')
                    pickle.dump(prods,infile)
                    infile.close()
            else:
                prods[p.getId()] = p
                infile = open("product.pickle", 'wb')
                pickle.dump(prods,infile)
                infile.close()

            print "Product added successfully...!"
        except:
            print "Enter Integer Value...!"
    

    def Product_view(self):
        if os.path.isfile("product.pickle"):
            try:
                infile = open("product.pickle","rb")
                prods = pickle.load(infile)
                infile.close()
                if prods:
                    print " Product-List \n "
                    for i in prods:
                        print prods[i].getId(),prods[i].getName(),prods[i].getPrice(),prods[i].getGroup(),prods[i].getSubgroup()

                    print "\n\n"

                else:
                    print "No Product with this name...!"
            except:
                print "No Product with this name...!"
        else:
            print "No Product with this name...!"

    
    def DeleteProduct(self):
        if os.path.isfile("product.pickle"):
            try:
                infile = open("product.pickle","rb")
                prods = pickle.load(infile)
                infile.close()
                if prods:
                    try:
                        id = int(raw_input("Enter Product Id to delete: "))
                        if id in prods:
                            del prods[id]
                            infile = open("product.pickle","wb")
                            pickle.dump(prods,infile)
                            infile.close()
                            print "Product Deleted successfully...!"

                        else:
                            print "Id not exist...!"
                    except:
                        print "Please Enter Valid ID"
                else:
                   print "Already Empty List...!"
            except:
                print "Already Empty List...!"
        else:
            print "Already Empty List...!"

class Customer:
    def __init__(self,Name,Address,phone):
        if os.path.isfile("customer.pickle"):
            try:
                infile = open("customer.pickle","rb")
                custss = pickle.load(infile)
                infile.close()
                ids = custss.keys()
                self.__id=max(ids)+1
            except:
                self.__id=1
        else:
            self.__id=1
        self._Name=Name
        self._Address=Address
        self._phone=phone

#Value Getters and setters
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id

    def getName(self):
        return self._Name
    def setName(self,Name):
        self._Name=Name

    def getAddress(self):
        return self._Address
    def setAddress(self,Address):
        self._Address = Address

    def getphone(self):
        return self._phone
    def setphone(self,phone):
        self._phone = phone

    def Product_view(self):
        if os.path.isfile("product.pickle"):
            try:
                infile = open("product.pickle","rb")
                prods = pickle.load(infile)
                infile.close()

                if prods:
                    print " Product-List \n"
                    for i in prods:
                        print prods[i].getId(),prods[i].getName(),prods[i].getPrice(),prods[i].getGroup(),prods[i].getSubgroup()

                else:
                    print "No product with this Id...!"
            except:
                print "No product with this Id...!"
        else:
            print "No product with this Id...!"


    def Product_Purchase(self):
        if os.path.isfile("product.pickle"):
            try:
                infile = open("product.pickle","rb")
                prods = pickle.load(infile)
                infile.close()
                try:
                    id = int(raw_input("Enter Product ID: "))
                    if id in prods:
                        self.PayUsingCard(id,prods)
                    else:
                        print "Enter Valid  Product ID...!"
                except:
                    print "Enter Valid  Product ID...!"
            except:
                print "No product with this Id...!"
        else:
            print "No product with this Id...!"

    
    def PayUsingCard(self,id,prods):
        print "Please pay ",prods[id].getPrice()," Amount"
        CT = raw_input("Enter Card Type: ")
        CNO = raw_input("Enter Card Number: ")

        py = Payment(prods[id].getName(),CT,CNO)
        if os.path.isfile("payment.pickle"):
            try:
                infile = open("payment.pickle","rb")
                paymentss = pickle.load(infile)
                infile.close()
                paylist  = paymentss[self.__id]
                paylist.append(py)
                paymentss[self.__id] = paylist
                infile = open("payment.pickle","wb")
                pickle.dump(paymentss,infile)
                infile.close()
                print "Payment Completed...!"
            except:
                pay = []
                pay.append(py)
                paymentss = {1:pay}
                paymentss.clear()
                paymentss[self.__id] = pay
                infile = open("payment.pickle","wb")
                pickle.dump(paymentss,infile)
                infile.close()
                print "Payment Completed...!"
        else:
            pay = []
            pay.append(py)
            paymentss = {1:pay}
            paymentss.clear()
            paymentss[self.__id] = pay
            infile = open("payment.pickle","wb")
            pickle.dump(paymentss,infile)
            infile.close()
            print "Payment Completed"

        if os.path.isfile("cart.pickle"):
            try:
                infile = open("cart.pickle","rb")
                lss = pickle.load(infile)
                infile.close()     
                ct = lss[self.__id]
                pList = ct.getProductList()
                f=0
                for item in pList:
                    if item.getId() == id:
                        f=1
                        break
                if f==1:
                    self.DeleteFromCart(id)
            except:
                pass

    def AddToCart(self):
        if os.path.isfile("product.pickle"):
            try:
                infile = open("product.pickle","rb")
                prods = pickle.load(infile)
                infile.close()
                x = []
                lss = {1:x}
                lss.clear()
                if prods:
                    try:
                        id = int(raw_input("Enter Product Id to add to cart: "))
                        if id in prods:
                            p = prods[id]
                            if os.path.isfile("cart.pickle"):
                                try:
                                    infile = open("cart.pickle","rb")
                                    lss = pickle.load(infile)
                                    infile.close()
                                    if lss:
                                        ct = lss[self.__id]
                                        x = ct.getProductList()
                                        total = ct.getTotal() + p.getPrice()
                                        Number = ct.getNOP()+1
                                        x.append(p)
                                        ct.setProductList(x)
                                        ct.setTotal(total)
                                        ct.setNOP(Number)
                                        lss[self.__id] = ct
                                        infile = open("cart.pickle","wb")
                                        pickle.dump(lss,infile)
                                        infile.close()
                                    else:
                                        x.append(p)
                                        total = p.getPrice()
                                        ct = Cart(1,total,x,self.__id)
                                        lss[self.__id] = ct
                                        infile = open("cart.pickle","wb")
                                        pickle.dump(lss,infile)
                                        infile.close()
                                except:
                                    x.append(p)
                                    total = p.getPrice()
                                    ct = Cart(1,total,x,self.__id)
                                    lss[self.__id] = ct
                                    infile = open("cart.pickle","wb")
                                    pickle.dump(lss,infile)
                                    infile.close()
                            else:
                                x.append(p)
                                total = p.getPrice()
                                ct = Cart(1,total,x,self.__id)
                                lss[self.__id] = ct
                                infile = open("cart.pickle","wb")
                                pickle.dump(lss,infile)
                                infile.close()
                        else:
                            print "Id not exist...!"
                    except:
                        print "Please Enter Valid ID...!"
                else:
                    print "No product with this Id...!"
            except:
                print "No product with this Id...!"

        else:
            print "No product with this Id...!"


    def ShowMyCart(self):
        if os.path.isfile("cart.pickle"):
            try:
                infile = open("cart.pickle","rb")
                lss = pickle.load(infile)
                infile.close()
                if lss:
                    ct = lss[self.__id]
                    x = ct.getProductList()
                    if x:
                        print " My Cart \n"
                        for i in x:
                            print i.getId(),i.getName(),i.getGroup(),i.getSubgroup(),i.getPrice()
                        print "Total amount to be paid: ",ct.getTotal()
                    else:
                        print "No item in your cart...!"
                else:
                    print "No item in your cart...!"
            except:
                print "No item in your cart...!"
        else:
            print "No item in your cart...!"

    
    def DeleteFromCart(self,id=0):
        if os.path.isfile("cart.pickle"):
            try:
                infile = open("cart.pickle","rb")
                lss = pickle.load(infile)
                infile.close()
                if lss:
                    ct = lss[self.__id]
                    x = ct.getProductList()
                    if x:
                        try:
                            if id==0:
                                id = int(raw_input("Enter Product Id to delete cart item: "))
                            f=0
                            for item in x:
                                if item.getId() == id:
                                    p=item
                                    f=1
                                    break
                            if f>0:
                                x.remove(p)
                                number = ct.getNOP()-1
                                total = ct.getTotal() - p.getPrice()
                                ct.setTotal(total)
                                ct.setNOP(number)
                                ct.setProductList(x)
                                lss[self.__id] = ct
                                infile = open("cart.pickle","wb")
                                pickle.dump(lss,infile)
                                infile.close()

                            else:
                                print "Id not exist...!"
                        except:
                            print "Enter valid Id to delete...!"
                    else:
                        print "Empty cart...!"
                else:
                    print "Empty cart...!"
            except:
                print "Empty cart...!"
        else:
            print "Empty cart...!"

    def BuyCart(self):
        if os.path.isfile("cart.pickle"):
            try:
                infile = open("cart.pickle","rb")
                lss = pickle.load(infile)
                infile.close()
                if lss:
                    if lss[self.__id]:
                        ct = lss[self.__id]
                        print "Total amount to be paid: Rs ",ct.getTotal()
                        CT = raw_input("Enter Card Type: ")
                        CNO = raw_input("Enter Card Number: ")
                        plist = ct.getProductList()
                        listname=""
                        for pname in plist:
                            if listname=="":
                                listname = pname.getName()
                            else:
                                listname = listname +","+ pname.getName()
                        py = Payment(listname,CT,CNO)
                        if os.path.isfile("payment.pickle"):
                            try:
                                infile = open("payment.pickle","rb")
                                paymentss = pickle.load(infile)
                                infile.close()
                                paylist  = paymentss[self.__id]
                                paylist.append(py)
                                paymentss[self.__id] = paylist
                                infile = open("payment.pickle","wb")
                                pickle.dump(paymentss,infile)
                                infile.close()
                                print "Payment Completed...!"
                                
                            except:
                                    pay = []
                                    pay.append(py)
                                    paymentss = {1:pay}
                                    paymentss.clear()
                                    paymentss[self.__id] = pay
                                    infile = open("payment.pickle","wb")
                                    pickle.dump(paymentss,infile)
                                    infile.close()
                                    print "Payment Completed...!"
                        else:
                            pay = []
                            pay.append(py)
                            paymentss = {1:pay}
                            paymentss.clear()
                            paymentss[self.__id] = pay
                            infile = open("payment.pickle","wb")
                            pickle.dump(paymentss,infile)
                            infile.close()
                            print "Payment Completed"
                        del lss[self.__id]
                        infile = open("cart.pickle","wb")
                        pickle.dump(lss,infile)
                        infile.close()
                    else:
                        print "Empty cart...!"
                else:
                    print "Empty cart...!"
            except:
                print "Empty cart...!"
        else:
            print "Empty cart...!"
    
    # def CompletePaymentHistory(self):
    #     if os.path.isfile("payment.pickle"):
    #         try:
    #             infile = open("payment.pickle","rb")
    #             paymentss = pickle.load(infile)
    #             infile.close()
    #             paylist  = paymentss[self.__id]
    #             if paylist:
    #                 print " History \n\n"
    #                 for item in paylist:
    #                     print item.getName(),item.getCardType(),item.getCardNo()

    #             else:
    #                 print "Not Found...!"
    #         except:
    #             print "Not Found...!"
    #     else:
    #         print "Not Found...!"


class Cart:   
    def __init__(self,NOP,Total,ProductList,customer_id):
        self.__id=1
        self.customer_id=customer_id
        self._NOP = NOP
        self._Total = Total
        self.ProductList=ProductList
#Value getters and setters
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id = id

    def getNOP(self):
        return self._NOP
    def setNOP(self,NOP):
        self._NOP = NOP

    def getTotal(self):
        return self._Total
    def setTotal(self,Total):
        self._Total = Total

    def getProductList(self):
        return self.ProductList
    def setProductList(self,ProductList):
        self._ProductList = ProductList


class Payment:
    def __init__(self,Name,CardType,CardNo):
        self.__id=1
        self.Name = Name
        self.__CardType = CardType
        self.__CardNo = CardNo

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id

    def getName(self):
        return self.Name
    def setName(self,Name):
        self.__Name=Name

    def getCardType(self):
        return self.__CardType
    def setCardType(self,CardType):
        self.__CardType=CardType

    def getCardNo(self):
        return self.__CardNo
    def setCardNo(self,CardNo):
        self.__CardNo=CardNo

class Guest:
    
    def Products_view(self):
        if os.path.isfile("product.pickle"):
            try:
                infile = open("product.pickle","rb")
                prods = pickle.load(infile)
                infile.close()

                if prods:
                    print " Product-List \n\n"
                    for i in prods:
                        print prods[i].getId(),prods[i].getName(),prods[i].getPrice(),prods[i].getGroup(),prods[i].getSubgroup()

                else:
                    print "Empty List...!"
            except:
                print "Empty List...!"
        else:
            print "Empty List...!"

    def GetRegistered(self):
        Name = raw_input("Enter Customer Name: ")
        phone = raw_input("Enter Mobile: ")
        Address = raw_input("Enter Address: ")

        c = Customer(Name,Address,phone)
        custss = {1:Customer}
        custss.clear()
        
        if os.path.isfile("customer.pickle"):
            infile = open("customer.pickle","rb")
            custss = pickle.load(infile)
            infile.close()
            custss[c.getId()] = c
            infile = open("customer.pickle","wb")
            pickle.dump(custss,infile)
            infile.close()

        else:
            custss[c.getId()] = c
            infile = open("customer.pickle", 'wb')
            pickle.dump(custss,infile)
            infile.close()

        print  "Your ID - ",c.getId()
        print "Must Remember"
        # for i in custss:
        #     print custss[i].getName()
        
while 1:
    print "Press 1: Admin Mode "
    print "Press 2: Customer Mode "
    print "Press 3: Guest Mode "
    print "Press 9: Exit Online Store "
    try:
        ch = int(raw_input())
        if ch == 1:
            name = raw_input("Enter Admin Name: ")
            a = Admin(name)
            while 1:
                print "Press 1: Add Product to cart: "
                print "Press 2: Show Product: "
                print "Press 3: Product Delete: "
                print "Press 9: Exit Menu "
                temp1 = int(raw_input())
                if temp1 == 1:
                    a.AddProduct()
                elif temp1 == 2:
                    a.Product_view()
                elif temp1 == 3:
                    a.Product_view()
                    a.DeleteProduct()
                elif temp1 == 9:
                    break
                else:
                    print "Enter valid choice...!"
        elif ch == 2:
            id = int(raw_input("Enter Customer Id: "))
            infile = open("customer.pickle","rb")
            custss = pickle.load(infile)
            infile.close()
            c = custss[id]
            if c:
                while 1:
                    print "Press 1: Product Buy "
                    print "Press 2: Show Product "
                    print "Press 3: Add to Cart "
                    print "Press 4: Delete from Cart "
                    print "Press 5: Buy Cart Products "
                    print "Press 6: Transactional History "
                    print "Press 7: Show Cart Items "
                    print "Press 0: Exit Menu "
                    tempo = int(raw_input())
                    if tempo == 1:
                        c.Product_view()
                        c.Product_Purchase()
                    elif tempo == 2:
                        c.Product_view()
                    elif tempo == 3:
                        c.Product_view()
                        c.AddToCart()
                    elif tempo == 4:
                        c.ShowMyCart()
                        c.DeleteFromCart()
                    elif tempo == 5:
                        c.ShowMyCart()
                        c.BuyCart()
                    elif tempo == 6:
                        c.CompletePaymentHistory()
                    elif tempo == 7:
                        c.ShowMyCart()
                    elif tempo == 0:
                        break
                    else:
                        print "Enter valid choice...!"
            else:
                print "Not a Registered Customer!!!"
        elif ch == 3:
            g = Guest()
            while 1:
                print "Press 1: Show Products "
                print "Press 2: Get Registered "
                print "Press 9: Exit Menu "
                choose = int(raw_input())
                if choose == 1:
                    g.Products_view()
                elif choose == 2:
                    g.GetRegistered()
                    break
                elif choose == 9:
                    break
                else:
                    print "Enter valid choice...!"
        elif ch == 9:
            break
        else:
            print "Enter valid choice...!"
    except:
        print "Enter valid choice...!"
