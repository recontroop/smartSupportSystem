from django.db import models
from django.contrib.auth.models import User

# For the customer table
class Customer(models.Model):
    CID = models.AutoField(primary_key=True)
	FirstName = models.CharField(max_length=32)
	LastName = models.CharField(max_length=32)
	Email = models.EmailField()
	PhoneNumber = models.CharField(max_length=16)

	def __str__(self):
		return str(self.CID)

# For the Ticket table
class Tickets(models.Model):
    TicketID = models.AutoField(primary_key=True)
    CID = models.ForeignKey(Customer,on_delete=models.CASCADE)
    UID = models.ForeignKey(User,on_delete=models.CASCADE)
	Subject = models.CharField(max_length=32)
	Description = models.CharField(max_length=512)
	Status = models.IntegerField() #open = 0 , in progress = 1, closed = 2
	Skill = models.CharField(max_length=16)
    Timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.TicketNumber)

# For the ChangeControl table
'''
    When a ticket is created it is created with:
        ChangeNumber: from automated
        TicketNumber: from ticket table
        Log         : CUSTOMER Description + Subject +
        ChangeStatus: Created
        TimeStamp   : Time
'''

# To log history of the status
class Log(models.Model):
    ChangeNumber = models.AutoField(primary_key=True)
	TicketNumber = models.ForeignKey(Tickets,on_delete=models.CASCADE)
	Body = models.CharField(max_length=256)
	ChangeStatus = models.IntegerField()
	Timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
		return str(self.ChangeNumber)

# Status: open = 0 , in progress = 1, closed = 2
class Status(models.Model):
    StatusID = models.IntegerField(primary_key=True)
	StatusName = models.CharField(max_length = 16)

    def __str__(self):
		return str(self.StatusID)
