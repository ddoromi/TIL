from django.db import models
from django_extensions.db.models import TimeStampedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from faker import Faker


faker = Faker()
class Post(TimeStampedModel):
    content = models.CharField(max_length=140)

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            Post.objects.create(content=faker.text(120))


class Image(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
        blank=True,
        upload_to='posts/images',
        processors=[ResizeToFill(600, 600, upscale=False)],
        format='JPEG',
        options={'quality': 90}
    )