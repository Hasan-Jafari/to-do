from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError



class UserManager(BaseUserManager):
    def create_user(self, phone_number, password):
        if not phone_number:
            raise ValidationError('phone number is "0"!')
        
        user = self.model(phone_number=phone_number)
        
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
            
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user