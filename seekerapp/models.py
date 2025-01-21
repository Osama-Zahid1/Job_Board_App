# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class SeekerManager(BaseUserManager):
#     def create_user(self, username, email, password, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('user_type', 'seeker')

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, email, password, **extra_fields)


# class Seeker(AbstractBaseUser):
#     SEEKER = 'seeker'
#     RECRUITER = 'recruiter'
#     USER_TYPES = [
#         (SEEKER, 'Seeker'),
#         (RECRUITER, 'Recruiter'),
#     ]

#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=250, unique=True)
#     password = models.CharField(max_length=128)
#     degree = models.CharField(max_length=100)
#     skills = models.TextField()
#     experience = models.CharField(max_length=100)
#     resume = models.FileField(upload_to='resumes/', blank=True, null=True)
#     user_type = models.CharField(max_length=20, choices=USER_TYPES, default=SEEKER)

#     objects = SeekerManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username


# class RecruiterManager(BaseUserManager):
#     def create_user(self, username, email, password, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('user_type', 'recruiter')

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, email, password, **extra_fields)


# class Recruiter(AbstractBaseUser):
#     SEEKER = 'seeker'
#     RECRUITER = 'recruiter'
#     USER_TYPES = [
#         (SEEKER, 'Seeker'),
#         (RECRUITER, 'Recruiter'),
#     ]

#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=250, unique=True)
#     password = models.CharField(max_length=128)
#     business_name = models.CharField(max_length=100)
#     business_type = models.CharField(max_length=100)
#     user_type = models.CharField(max_length=20, choices=USER_TYPES, default=RECRUITER)

#     objects = RecruiterManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username


# class Job(models.Model):
#     job_type = models.CharField(max_length=100)
#     description = models.TextField()
#     business_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     skills_required = models.TextField()
#     salary_range = models.CharField(max_length=100)
#     recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='jobs')

#     def __str__(self):
#         return self.job_type


from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Seekermanager(BaseUserManager):
    def seeker(self, username, email, password, degree, experience, **others):
        if not email:
            raise ValueError('Enter email')
        seek = self.model(username=username, email=self.normalize_email(email), degree=degree, experience=experience, **others)
        seek.set_password(password)
        seek.save(using=self._db)
        return seek

    def create_superuser(self, username, email, password, **others):
        others.setdefault("is_active", True)
        others.setdefault("is_staff", True)
        user = self.model(username=username, email=email, **others)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Seekermodel(AbstractBaseUser):
    SEEKER = 'seeker'
    RECRUITER = 'recruiter'
    USERTYPE = [
        (SEEKER, 'Seek'),
        (RECRUITER, 'Recruit')
    ]
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    degree = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    skills = models.CharField(max_length=250)
    pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True)
    usertype = models.CharField(max_length=60, choices=USERTYPE, default=SEEKER)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    objects = Seekermanager()

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Rcruitermanager(BaseUserManager):
    def recruiteruser(self, username, email, password, businessname, businesstype, **others):
        if not email:
            return ("email is must")
        if not username:
            return ("username is must")
        
        rperson = self.model(username=username, email=self.normalize_email(email), businessname=businessname, businesstype=businesstype, **others)
        rperson.set_password(password)
        rperson.save(using=self._db)
        return rperson

    def create_superuser(self, username, email, password, **others):
        others.setdefault("is_active", True)
        others.setdefault("is_staff", True)
        user = self.model(username=username, email=email, **others)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class Recruitermodel(AbstractBaseUser):
    SEEKER = 'seeker'
    RECRUITER = 'recruiter'
    USER_TYPES = [
        (SEEKER, 'Seeker'),
        (RECRUITER, 'Recruit')
    ]
    
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=60, unique=True)
    businessname = models.CharField(max_length=250)
    businesstype = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    usertype = models.CharField(max_length=60, choices=USER_TYPES, default=RECRUITER)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    def has_perm(self, perm, obj=None):
        # For simplicity, let's allow all permissions for now
        return True


    def has_module_perms(self, app_label):
        return True  # Allow all users to view the admin module
    objects= Rcruitermanager()
    
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username

class Jobmodel(models.Model):
    jobtitle=models.CharField(max_length=50)
    jobdesp=models.CharField(max_length=250)
    skillsreq=models.CharField(max_length=50)
    businessadd=models.CharField( max_length=50)
    salary=models.CharField(max_length=50)
    recruiter = models.ForeignKey(Recruitermodel, on_delete=models.CASCADE)  # Ensure this is correctly set
    
    def __str__(self):
        return f"{self.jobtitle}"

    
class Application(models.Model):
    job = models.ForeignKey(Jobmodel, on_delete=models.CASCADE)
    seeker = models.ForeignKey(Seekermodel, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resume/', blank=True)  # You can copy the resume here for record
    status = models.CharField(max_length=50, choices=[('Applied', 'Applied'), ('Interview', 'Interview Scheduled'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Applied')    
    
    
    
        