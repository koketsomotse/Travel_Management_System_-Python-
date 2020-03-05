#Travel Management System (Python)
#Created by Koketso Motseothata

from tkinter import *
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox


class Travel:

    def __init__(self,root):
        self.root = root
        self.root.title("Travel Management System.")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='black')

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%y"))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        #variables we will be using
        
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()
        var13=IntVar()

        #information about the traveler 

        FirstName=StringVar()
        Surname=StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Telephone=StringVar()
        Mobile=StringVar()
        Email=StringVar()

        AirportTax =StringVar()
        Killometres=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()

        Standard=StringVar()
        Economy=StringVar()
        FirstClass=StringVar()

        #initialization
        AirportTax.set("0")
        Killometres.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")
        Standard.set("0")
        Economy.set("0")
        FirstClass.set("0")

        #====================================================Define Functions===============#
        def iExit():
            iExit=tkinter.messagebox.askyesno(" Travel Management System "," Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            AirportTax.set("0")
            Killometres.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")
            Standard.set("0")
            Economy.set("0")
            FirstClass.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set("0")
            var12.set("0")
            var13.set("0")

        

            FirstName.set('')
            Surname.set('')
            Address.set('')
            PostCode.set('')
            Telephone.set('')
            Mobile.set('')
            Email.set('')

            
            PaidTax.set("0")
            SubTotal.set("0")
            TotalCost.set("0")
            self.txtReceipt.delete('1.0',END)

            Standard.set(0)
            Economy.set("0")
            FirstClass.set("0")

            self.cboDeparture.current(0)
            self.cboDestination.current(0)
            self.cboAccomodation.current(0)

            self.txtAirportTax.configure(state=DISABLED)
            self.txtKillometres.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)

            self.txtStandard.configure(state=DISABLED)
            self.txtEconomy.configure(state=DISABLED)
            self.txtFirstClass.configure(state=DISABLED)
            
        def Receipt():
            self.txtReceipt.delete("1.0",END)
            x=random.randint(10853,500831)
            randomRef=str(x)
            Receipt_Ref.set("Travel Bill " + randomRef)

            self.txtReceipt.insert(END,'Receipt Ref:\t\t\t\t\t'+ Receipt_Ref.get() + '\n')
            self.txtReceipt.insert(END,'Date:\t\t\t\t\t'+ DateofOrder.get() + '\n')
            self.txtReceipt.insert(END,'Flight:\t\t\t\t\t'+ "Travelling Details \n")
            self.txtReceipt.insert(END,'First Name:\t\t\t\t\t'+ FirstName.get() + "\n")
            self.txtReceipt.insert(END,'Surname:\t\t\t\t\t'+ Surname.get() + "\n")
            self.txtReceipt.insert(END,'Address:\t\t\t\t\t'+ Address.get() + "\n")
            self.txtReceipt.insert(END,'Post Code:\t\t\t\t\t'+ PostCode.get() + "\n")
            self.txtReceipt.insert(END,'Telephone:\t\t\t\t\t'+ Telephone.get() + "\n")
            self.txtReceipt.insert(END,'Mobile:\t\t\t\t\t'+ Mobile.get() + "\n")
            self.txtReceipt.insert(END,'Email:\t\t\t\t\t'+ Email.get() + "\n")
            self.txtReceipt.insert(END,'Standard:\t\t\t\t\t'+ Standard.get() + "\n")
            self.txtReceipt.insert(END,'Standard:\t\t\t\t\t'+ var11.get() + "\n")
            self.txtReceipt.insert(END,'Economy:\t\t\t\t\t'+ Economy.get() + "\n")
            self.txtReceipt.insert(END,'Economy:\t\t\t\t\t'+ var12.get() + "\n")
            self.txtReceipt.insert(END,'FirstClass:\t\t\t\t\t'+ FirstClass.get() + "\n")
            self.txtReceipt.insert(END,'FirstClass:\t\t\t\t\t'+ var13.get() + "\n")
            self.txtReceipt.insert(END,'PaidTax:\t\t\t\t\t'+ PaidTax.get() + "\n")
            self.txtReceipt.insert(END,'SubTotal:\t\t\t\t\t'+ str(SubTotal.get()) + "\n")
            self.txtReceipt.insert(END,'TotalCost:\t\t\t\t\t'+ str(TotalCost.get()) + "\n")

        def Total_Paid():
            if (var1.get() == 1 and var2.get()==1 and var3.get()==1 and var4.get()==1 and var5.get()==1 and var11.get()=='' and var12.get()=='' and var13.get()=="1"):

                q1 = float(45)
                q2 = float(63)
                q3 = float(334.59)
                q4 = float(274.90)

                Cost_of_Fare = q1 + q2+q3+q4

                Tax= "R" + str('%.2f'%((Cost_of_Fare) * 0.09))
                ST="R" + str('%.2f'%((Cost_of_Fare)))
                TT= "R" + str('%.2f'%((Cost_of_Fare + ((Cost_of_Fare * 0.09)))))

                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
        

        
        #===================================================================================#
        MainFrame=Frame(self.root)
        MainFrame.grid()

        Tops = Frame(MainFrame, bd=20,width=1350,relief=RIDGE)
        Tops.pack(side=TOP)

        self.lblTitle=Label(Tops,font=('arial',73,'bold'),text=" Travel Management System. ")
        self.lblTitle.grid()
        #===================================================================================#
        CustomerDetailsFrame=LabelFrame(MainFrame,width=1350,height=500,bd=20,pady=5,relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM)
        
        FrameDetails=Frame(CustomerDetailsFrame,width=880,height=400,bd=10,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        CustomerName=LabelFrame(FrameDetails,width=300,height=250,bd=10,font=('arial',12,'bold'),text='Customer Name',relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        TravelFrame=LabelFrame(FrameDetails,width=300,bd=10,height=250,font=('arial',12,'bold'),text='Travel Details',relief=RIDGE)
        TravelFrame.grid(row=0,column=1)

        Ticket_Frame=LabelFrame(FrameDetails,width=300,height=150,relief=FLAT)
        Ticket_Frame.grid(row=1,column=0)

        CostFrame=LabelFrame(FrameDetails,width=150,height=150,relief=FLAT)
        CostFrame.grid(row=1,column=1)

        #===================================================================================#
        Receipt_ButtonFrame=Frame(CustomerDetailsFrame,width=450,height=400,bd=10,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        ReceiptFrame=LabelFrame(Receipt_ButtonFrame,width=300,height=300,bd=10,font=('arial',12,'bold'),text='Receipt',relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_ButtonFrame,width=300,height=100,bd=5)
        ButtonFrame.grid(row=1,column=0)

        #=================================CustomerName===================================#
        self.lblFirstName=Label(CustomerName,font=('arial',14,'bold'),text="First Name",bd=7)
        self.lblFirstName.grid(row=0,column=0,sticky = W)
        self.txtFirstName=Entry(CustomerName,font=('arial',14,'bold'),textvariable=FirstName,bd=7,insertwidth=2,justify=RIGHT)
        self.txtFirstName.grid(row=0,column=1)

        self.lblSurname=Label(CustomerName,font=('arial',14,'bold'),text="Surname",bd=7)
        self.lblSurname.grid(row=1,column=0,sticky = W)
        self.txtSurname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Surname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1)

        self.lblAddress=Label(CustomerName,font=('arial',14,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=2,column=0,sticky = W)
        self.txtAddress=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Address,bd=7,insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)

        self.lblPostCode=Label(CustomerName,font=('arial',14,'bold'),text="Post Code",bd=7)
        self.lblPostCode.grid(row=3,column=0,sticky = W)
        self.txtPostCode=Entry(CustomerName,font=('arial',14,'bold'),textvariable=PostCode,bd=7,insertwidth=2,justify=RIGHT)
        self.txtPostCode.grid(row=3,column=1)

        self.lblTelephone=Label(CustomerName,font=('arial',14,'bold'),text="Telephone",bd=7)
        self.lblTelephone.grid(row=4,column=0,sticky = W)
        self.txtTelephone=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Telephone,bd=7,insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)


        self.lblMobile=Label(CustomerName,font=('arial',14,'bold'),text="Mobile",bd=7)
        self.lblMobile.grid(row=5,column=0,sticky = W)
        self.txtMobile=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Mobile,bd=7,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=5,column=1)
            
        self.lblEmail=Label(CustomerName,font=('arial',14,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=6,column=0,sticky = W)
        self.txtEmail=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Email,bd=7,insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)
        #===================================================================================#

        self.lblDeparture=Label(TravelFrame,font=('arial',14,'bold'),text="Departure",bd=7)
        self.lblDeparture.grid(row=0,column=0,sticky = W)
        self.cboDeparture=ttk.Combobox(TravelFrame,textvariable=var11, state='readonly',font=('arial',20,'bold'),width=14)
        self.cboDeparture['value']=('','OR Tambo','Bloemfontain Airport','King Shaka International','CapeTown Int','East London Airport')
        self.cboDeparture.current(0)
        self.cboDeparture.grid(row=0,column=1)




        self.lblDestination=Label(TravelFrame,font=('arial',14,'bold'),text="Destination",bd=7)
        self.lblDestination.grid(row=1,column=0,sticky = W)
        self.cboDestination=ttk.Combobox(TravelFrame,textvariable=var12, state='readonly',font=('arial',20,'bold'),width=14)
        self.cboDestination['value']=('','OR Tambo','Bloemfontain Airport','King Shaka International','CapeTown Int','East London Airport')
        self.cboDestination.current(0)
        self.cboDestination.grid(row=1,column=1)


        self.lblAccomodation=Label(TravelFrame,font=('arial',14,'bold'),text="Accomodation",bd=7)
        self.lblAccomodation.grid(row=2,column=0,sticky = W)
        self.cboAccomodation=ttk.Combobox(TravelFrame,textvariable=var13, state='readonly',font=('arial',20,'bold'),width=14)
        self.cboAccomodation['value']=('','1','2','3','4','5')
        self.cboAccomodation.current(0)
        self.cboAccomodation.grid(row=2,column=1)
        #=====================================Flight Details==============================#
        self.chkAirportTax=Checkbutton(TravelFrame,text="Airport Tax",variable=var1,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=3,column=0,sticky=W)
        self.txtAirportTax=Entry(TravelFrame,font=('arial',14,'bold'),textvariable=AirportTax,bd=7,insertwidth=2,state=DISABLED,justify=RIGHT)
        self.txtAirportTax.grid(row=3,column=1)

        self.chkKillometres=Checkbutton(TravelFrame,text="Killometres",variable=var2,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=4,column=0,sticky=W)
        self.txtKillometres=Entry(TravelFrame,font=('arial',14,'bold'),textvariable=Killometres,bd=7,insertwidth=2,state=DISABLED,justify=RIGHT)
        self.txtKillometres.grid(row=4,column=1)

        self.chkTravel_Ins=Checkbutton(TravelFrame,text="Travelling Insurence",variable=var3,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=5,column=0,sticky=W)
        self.txtTravel_Ins=Entry(TravelFrame,font=('arial',14,'bold'),textvariable=Travel_Ins,bd=7,insertwidth=2,state=DISABLED,justify=RIGHT)
        self.txtTravel_Ins.grid(row=5,column=1)

        self.chkLuggage=Checkbutton(TravelFrame,text="Luggage",variable=var4,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=6,column=0,sticky=W)
        self.txtLuggage=Entry(TravelFrame,font=('arial',14,'bold'),textvariable=Luggage,bd=7,insertwidth=2,state=DISABLED,justify=RIGHT)
        self.txtLuggage.grid(row=6,column=1)
        
        #=================================Payment Information=====================================#

        self.lblPaidTax=Label(CostFrame,font=('arial',14,'bold'),text="Paid Tax\t\t",bd=7)
        self.lblPaidTax.grid(row=0,column=2,sticky = W)
        self.txtPaidTax=Entry(CostFrame,font=('arial',14,'bold'),textvariable=PaidTax,bd=7,width=26,justify=RIGHT)
        self.txtPaidTax.grid(row=0,column=3)

        self.lblSubTotal=Label(CostFrame,font=('arial',14,'bold'),text="Sub Total\t\t",bd=7)
        self.lblSubTotal.grid(row=1,column=2,sticky = W)
        self.txtSubTotal=Entry(CostFrame,font=('arial',14,'bold'),textvariable=SubTotal,bd=7,width=26,justify=RIGHT)
        self.txtSubTotal.grid(row=1,column=3)

        self.lblTotalCost=Label(CostFrame,font=('arial',14,'bold'),text="Total Cost\t\t",bd=7)
        self.lblTotalCost.grid(row=2,column=2,sticky = W)
        self.txtTotalCost=Entry(CostFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7,width=26,justify=RIGHT)
        self.txtTotalCost.grid(row=2,column=3)
        #=================================Ticket Information=====================================#
        self.chkStandard=Checkbutton(Ticket_Frame,text="Standard",variable=var5,onvalue=1,offvalue=0,font=('arial',14,'bold')).grid(row=0,column=0)
        self.txtStandard=Entry(Ticket_Frame,font=('arial',14,'bold'),textvariable=Standard,bd=5,width=6,state=DISABLED,justify=RIGHT)
        self.txtStandard.grid(row=0,column=1)

        self.chkSingle=Checkbutton(Ticket_Frame,text="Single",variable=var6,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=0,column=2,sticky=W)
        
        self.chkEconomy=Checkbutton(Ticket_Frame,text="Economy",variable=var7,onvalue=1,offvalue=0,font=('arial',14,'bold')).grid(row=1,column=0)
        self.txtEconomy=Entry(Ticket_Frame,font=('arial',14,'bold'),textvariable=Economy,bd=5,width=6,state=DISABLED,justify=RIGHT)
        self.txtEconomy.grid(row=1,column=1)

        self.chkReturn=Checkbutton(Ticket_Frame,text="Return",variable=var8,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=1,column=2,sticky=W)

        self.chkFirstClass=Checkbutton(Ticket_Frame,text="First Class",variable=var8,onvalue=1,offvalue=0,font=('arial',14,'bold')).grid(row=2,column=0)
        self.txtFirstClass=Entry(Ticket_Frame,font=('arial',14,'bold'),textvariable=FirstClass,bd=5,width=6,state=DISABLED,justify=RIGHT)
        self.txtFirstClass.grid(row=2,column=1)

        self.chkReturn=Checkbutton(Ticket_Frame,text="Return",variable=var9,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=1,column=2,sticky=W)

        self.chkSpecialNeeds=Checkbutton(Ticket_Frame,text="Special Needs",variable=var10,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=2,column=2,sticky=W)
        #=================================Receipt Information=====================================#

        self.txtReceipt=Text(ReceiptFrame,width=60,height=21,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=0,column=0)


        #=================================Buttons=====================================#
        self.btnTotal=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,text='Total',command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,text='Receipt',command=Receipt).grid(row=0,column=1)
        self.btnReset=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,text='Reset',command=Reset).grid(row=0,column=2)
        self.btnExit=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,text='Exit',command=iExit).grid(row=0,column=3)


if __name__=='__main__':
    
    root=Tk()
    application=Travel(root)
    root.mainloop()
