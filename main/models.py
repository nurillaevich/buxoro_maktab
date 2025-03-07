from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Teacher(BaseModel):
    full_name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    fit_back = models.TextField()
    image = models.ImageField(upload_to='teacher/%Y/%m/%d')

    def __str__(self):
        return self.full_name


class AboutUs(BaseModel):
    about = RichTextUploadingField()

    def __str__(self):
        return self.about


class       Category(BaseModel):
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Course(BaseModel):
    title = models.CharField(max_length=212)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='course/%Y/%m/%d')

    def __str__(self):
        return self.title


class News(BaseModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField('news/%Y/%m/%d')
    date = models.CharField(max_length=212)

    def __str__(self):
        return self.title


class Contact(BaseModel):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactUs(BaseModel):
    email = models.EmailField()
    phone_number = models.CharField(max_length=212)
    address = models.CharField(max_length=212)

    def __str__(self):
        return self.email
