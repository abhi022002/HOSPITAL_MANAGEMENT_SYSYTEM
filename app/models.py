# from django.db import models

# # Create your models here.


# class procedure(models.Model):
#     Code = models.IntegerField(primary_key= True)
#     Name = models.CharField(max_length=100)
#     Cost = models.IntegerField(default = 0)
#     class Meta:
#         db_table = "procedure"

from django.db import models

class procedure(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = "procedure"


class physician(models.Model):
    employeeid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mail = models.EmailField()
    class Meta:
        db_table = "physician"

class patient(models.Model):
    ssn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.DecimalField(max_digits = 4, decimal_places=0)
    pcp = models.ForeignKey('physician',on_delete=models.CASCADE)
    class Meta:
        db_table = "patient"

class patients(models.Model):
    ssn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.DecimalField(max_digits = 4, decimal_places=0)
    pcp = models.ForeignKey('physician',on_delete=models.CASCADE)
    class Meta:
        db_table = "patients"

class tested_patient(models.Model):
    ssn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = "tested_patient"

class fdo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mail = models.EmailField()
    class Meta:
        db_table = "fdo"

class dba(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "dba"

class room(models.Model):
    no = models.IntegerField(primary_key=True)
    class Meta:
        db_table = "room"

class stay(models.Model):
    stayid = models.IntegerField(primary_key=True)
    roomno = models.ForeignKey('room',on_delete=models.CASCADE)
    patientid = models.ForeignKey('patient',on_delete=models.CASCADE)
    class Meta:
        db_table = "stay"

class appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    physicianid = models.ForeignKey('physician',on_delete=models.CASCADE)
    patientid = models.ForeignKey('patient',on_delete=models.CASCADE)
    class Meta:
        db_table = "appointment"

class prescribes(models.Model):
    id = models.IntegerField(primary_key=True)
    dose = models.TextField()
    physicianid = models.ForeignKey('physician',on_delete=models.CASCADE)
    patientid = models.ForeignKey('patient',on_delete=models.CASCADE)
    class Meta:
        db_table = "prescribes"

class count(models.Model):
    id = models.IntegerField(primary_key=True,default=1)
    countu = models.IntegerField(default=0)
    countdeo = models.IntegerField()
    countfdo = models.IntegerField()
    countp = models.IntegerField(default=0)
    counta = models.IntegerField(default=0)
    countr = models.IntegerField(default=0)
    countpr = models.IntegerField(default=0)
    countT = models.IntegerField(default=0)
    class Meta:
        db_table = "count"

class completed(models.Model):
    id = models.IntegerField(primary_key=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    physicianid = models.ForeignKey('physician',on_delete=models.CASCADE)
    patientid = models.ForeignKey('patient',on_delete=models.CASCADE)
    class Meta:
        db_table = "completed"

class admitted(models.Model):
    id = models.IntegerField(primary_key=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    physicianid = models.ForeignKey('physician',on_delete=models.CASCADE)
    patientid = models.ForeignKey('patient',on_delete=models.CASCADE)
    class Meta:
        db_table = "admitted"


class deo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    pasw = models.CharField(max_length=100)
    mail = models.EmailField()
    class Meta:
        db_table = "deo"



class treatments(models.Model):
    treatment_id = models.IntegerField(primary_key=True)
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length=100)
    symptoms = models.TextField(blank=True, null=True)
    treatments = models.TextField(blank=True, null=True)
    test_results = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='treatment_images/', blank=True, null=True)
