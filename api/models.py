import mimetypes
import os.path
from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from django.core.files import File
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit


class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)
    image_file = models.ImageField(upload_to='images', blank=True, default=None)
    image_web = ImageSpecField(source='image_file',
                               processors=[ResizeToFit(width=1024)],
                               format='JPEG',
                               options={'quality': 88})
    image_mobile = ImageSpecField(source='image_file',
                                  processors=[ResizeToFit(width=320)],
                                  format='JPEG',
                                  options={'quality': 84})

    def get_image(self):
        if not self.image_url:
            print(f'Image URL is empty.')
            return False

        try:
            # Request the image URL
            response = urlopen(self.image_url)

            # Check the response code
            if response.status != 200:
                print(f'Response is unsuccessful: {self.image_url}')
                return False

            # Check the content type is image
            content_type = response.headers['content-type']
            extension = mimetypes.guess_extension(content_type)
            if not content_type.startswith('image'):
                print(f'Invalid image: {self.image_url}')
                return False

            # Save the response to file
            content = response.read()
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(content)
            img_temp.flush()
            self.image_file.save(f"image_{self.pk}{extension}", File(img_temp))
            print(f'Successfully saved: {self.image_url}')
            return True
        except Exception:
            print(f'Can not pull the image: {self.image_url}')
            return False

    def delete(self, *args, **kwargs):
        if self.image_file and os.path.isfile(self.image_file.path):
            os.remove(self.image_file.path)
        super(Car, self).delete(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.title}'
