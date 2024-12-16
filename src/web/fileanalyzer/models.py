from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.


class FinderObject(models.Model):
    class Types(models.TextChoices):
        FILE = "F", _("File")
        FOLD = "FD", _("Folder")
        UNKNOWN = "U", _("Unknown")

    class FileTypes(models.TextChoices):
        IMAGE = "I", _("Image")
        TEXT = "T", _("Text")
        VIDEO = "V", _("Video")
        AUDIO = "A", _("Audio")
        ARCHIVE = "Z", _("Archive")
        EXECUTABLE = "E", _("Executable")
        SCRIPT = "S", _("Script")
        WEB = "W", _("Web")
        DATA = "D", _("Data")
        UNKNOWN = "U", _("Unknown")

    type = models.CharField(max_length=2, choices=Types.choices, default=Types.UNKNOWN)
    file_type = models.CharField(
        max_length=2, choices=FileTypes, default=None, null=True, blank=True
    )
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255, unique=True)
    size = models.BigIntegerField(default=0)
    extension = models.CharField(max_length=255, default=None, blank=True)
    last_access = models.DateTimeField()
    last_modified = models.DateTimeField()
    width = models.IntegerField(null=True, default=None, blank=True)
    height = models.IntegerField(null=True, default=None, blank=True)
    pages_count = models.IntegerField(null=True, default=None, blank=True)

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nPath: {self.path}\nExtension: {self.extension}"

    def clean(self):
        super().clean()
        if self.type == "FD":
            if self.file_type:
                raise ValidationError("Fold can't have file type")
            if self.extension:
                raise ValidationError("Fold can't have extension")

        if self.type == "F" and not self.file_type:
            raise ValidationError("File must have file type")
