# Copyright (C) 2018 The Hunter2 Contributors.
#
# This file is part of Hunter2.
#
# Hunter2 is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Hunter2 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License along with Hunter2.  If not, see <http://www.gnu.org/licenses/>.


from django.db import models
from solo.models import SingletonModel


def file_path(instance, filename):
    return f'site/{filename}'


class Configuration(SingletonModel):
    index_content = models.TextField()
    privacy_policy = models.TextField(blank=True)


class File(models.Model):
    slug = models.SlugField(unique=True)
    file = models.FileField(
        upload_to=file_path,
        help_text='The extension of the uploaded file will determine the Content-Type of the file when served',
    )


class Icon(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField(help_text='The size of the icon (width and height). 0 should be used for scalable (eg. SVG) icons.', unique=True)

    def url(self):
        return self.file.file.url
