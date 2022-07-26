from django.db import models


class CreatedModel(models.Model):
    """Abstract model. Create field pub date."""

    publish_date = models.DateTimeField(
        verbose_name='дата (автоматически)', auto_now_add=True, db_index=True
    )

    class Meta:
        abstract = True
