from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
  def create_user(self, email, name, password, **extra_fields):
    if not email:
      return ValueError('Users must have an email address')
  
    user = self.model(
      email=self.normalize_email(email),
      name=name,
      # liked_events=liked_events.set(),
      # fav_tags=fav_tags.set(),
      **extra_fields,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user


  def create_superuser(self, email, password, name='admin', **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')
    return self.create_user(name, email, password, **extra_fields)