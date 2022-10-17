from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.


class AppUserManager(UserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))         


        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Account(AbstractUser):
    email=models.EmailField(max_length=255,unique=True,verbose_name="email")
    username=models.CharField(max_length=100,blank=True,null=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    profile_image=models.ImageField(upload_to='profile_image',blank=True,null=True)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects=AppUserManager()

    def __str__(self):
        return self.first_name



class ProfileUser(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    photo=models.ImageField(upload_to='profile') 

class Status(models.Model):
    user=models.ForeignKey(ProfileUser,on_delete=models.CASCADE,related_name='status')
    file=models.FileField(upload_to='status')           

    # def has_perm(self,perm,obj=None):
    #     return self.username

    # def has_module_perms(self,app_label):
    #     return True


# class PublicChatRoom(models.Model):
#     title=models.CharField(max_length=255,unique=True,blank=False)
#     user=models.ManyToManyField(Accounts,blank=True,help_text="users who are connected to the chat")

#     def __str_(self):
#         return self.title

# def conect_user(self,user):
#     ''' 
#     return True if user is present in the user list
#     '''
#     is_user_added=False
#     if not user in self.user.all():
#         self,users.add(user)
#         self.save() 
#         is_used_added=True
#     elif user in seld.user.all():
#         is_user_added=True
#     return is_user_added

# def disconnect_user(self,user):
#     '''
#     return True if user is removed from user list
#     '''
#     is_user_added=False
#     if user in self.user.all():
#         self,users.remove(user)
#         self.save() 
#         is_used_added=True
#     return is_user_remove

# @property
# def group_name(self):
#     '''
#     Returns the channelsgroup name that sockets should subscribe to and get sent messages as they are generated
#     '''    
#     return f"PublicChatRoom-{self.id}"

# class PublicChatRoomMessageManager(models.Manager):
#     def by_room(self,room):
#         qs=PublicRoomChar=tMessage.objects.filter(room=room).order_by("-timestamp")
#         return qs


# class PublicChatMessages(models.Model):
#     '''
#     Chat messages created by a user inside a public chat room {foreignKey}
#     '''
#     user= models .ForeignKey(Accounts,on_delete=models.CASCADE)
#     room=models.ForeignKey(PublicChatRoom,on_delete=models.CASCADE)
#     timestamp=models.DateTimeField(auto_now_add=True)
#     content=models.TextField(unique=True,blank=False)

#     objects=PublicChatRoomMessageManager()

#     def __str__(self):
#         return self.content



