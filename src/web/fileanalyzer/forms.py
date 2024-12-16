from django import forms


class UploadFolderForm(forms.Form):
    folder_path = forms.CharField(label="Вставьте абсолютный путь к дирректории")
