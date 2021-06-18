# class BoecAccountManger(BaseUserManager):
#     def create_user(self, email, first_name, last_name, password=None):
#         if not email:
#             raise ValueError('Este es un campo requerido')
#         if not first_name:
#             raise ValueError('Este es un campo requerido')
#         if not last_name:
#             raise ValueError('Este es un campo requerido')

#         user = self.model(
#             email=self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user