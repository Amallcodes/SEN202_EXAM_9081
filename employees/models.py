from django.db import models

#Questions answered are 1, 2 & 5
# superuser login details: username: admin, password: admin
# screenshots included in readme
class Staffbase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    def get_role(self):
        return "Staff"

class Manager(Staffbase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Manager)"

    def get_role(self):
        return "Manager"

class Intern(Staffbase):
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='interns')
    internship_end = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Intern)"

    def get_role(self):
        return "Intern"