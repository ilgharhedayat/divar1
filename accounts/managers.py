from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("this field is required")

        user = self.model(phone_number=phone_number)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number=phone_number, password=password)
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_admin(self, phone_number, password):
        user = self.create_user(phone_number=phone_number, password=password)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user
