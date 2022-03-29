from tkinter import *
from Member import Member
from MemberDAO import MemberDAO
class TennisGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.memberDAOConn = MemberDAO()

        self.studentList = []
        
        self.label1 = Label(master, text="Enter your Firstname")
        self.label1.pack()

        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Enter your Surname")
        self.label2.pack()

        self.entry2 = Entry()
        self.entry2.pack()

        self.label3 = Label(master, text="Date of Birth")
        self.label3.pack()

        self.entry3 = Entry()
        self.entry3.pack()

        self.label4 = Label(master, text="Member Level")
        self.label4.pack()

        self.entry4 = Entry()
        self.entry4.pack()


        self.addMemberButton = Button(master, text="Add Member", command=self.addMember)
        self.addMemberButton.pack()

        self.showMembersButton = Button(master, text="Show All Members", command=self.showAllMembers)
        self.showMembersButton.pack()

        self.txtBox = Text(master, height=10, width=30)
        self.txtBox.pack()
        

    def addMember(self):
        self.clearScreen()
        firstname = self.entry1.get()
        surname = self.entry2.get()
        dob = self.entry3.get()
        membertype = self.entry4.get()
        newMember = Member(firstname,surname,dob,membertype)
        self.memberDAOConn.saveMember(newMember)
        self.txtBox.insert(END,"New Member Added")

    def showAllMembers(self):
        self.clearScreen()
        memberList = self.memberDAOConn.getAllMembers()
        for thisMember in memberList:
            self.txtBox.insert(END, thisMember.getFirstname() + "\t" + thisMember.getSurname() + "\t" + thisMember.getMemberType()+ "\n")

    def clearScreen(self):
        self.txtBox.delete(1.0,END)
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)
        
    def close(self):
        root.destroy()

root = Tk()
my_gui = TennisGUI(root)
root.dooneevent()
