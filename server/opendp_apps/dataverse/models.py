from django.db import models


class RegisteredDataverse(models.Model):
    """
    Dataverses that are allowed to use the OpenDP App
    """
    name = models.CharField(unique=True, max_length=255)
    dataverse_url = models.URLField(unique=True,
                                    help_text='No trailing slash.')
    active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, help_text='optional')

    def __str__(self):
        return '%s (%s)' % (self.name, self.dataverse_url)

    def save(self, *args, **kwargs):
        # remove any trailing slashes
        while self.dataverse_url.endswith('/'):
            self.dataverse_url = self.dataverse_url[:-1]

        self.dataverse_url = self.dataverse_url.lower()

        super(RegisteredDataverse, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)


class DataverseFile(models.Model):
    """
    Placeholder so we can have a foreign key
    in the Session object.
    """

    # TODO: Many2Many relationship with DPRequests

    # Defines the privacy budget, set by depositor
    epsilon = models.FloatField(null=False, blank=False)
