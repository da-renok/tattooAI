from django.conf import settings
from django.db import models


class Style(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ArtistProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="artist_profile",
        limit_choices_to={"role": "artist"},
    )
    display_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="artists/", blank=True)
    experience_years = models.PositiveSmallIntegerField(default=0)
    styles = models.ManyToManyField(Style, related_name="artists", blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_name"]

    def __str__(self):
        return self.display_name


class PortfolioWork(models.Model):
    artist = models.ForeignKey(
        ArtistProfile, on_delete=models.CASCADE, related_name="works"
    )
    style = models.ForeignKey(
        Style,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="works",
    )
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="portfolio/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or f"Work #{self.pk}"


class Sketch(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sketches",
    )
    style = models.ForeignKey(
        Style,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sketches",
    )
    prompt = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="sketches/")
    is_saved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "sketches"

    def __str__(self):
        return f"Sketch #{self.pk}"


class TattooRequest(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        ACCEPTED = "accepted", "Accepted"
        DECLINED = "declined", "Declined"
        CANCELLED = "cancelled", "Cancelled"
        COMPLETED = "completed", "Completed"

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="tattoo_requests",
    )
    artist = models.ForeignKey(
        ArtistProfile,
        on_delete=models.PROTECT,
        related_name="tattoo_requests",
    )
    sketches = models.ManyToManyField(
        Sketch, related_name="tattoo_requests", blank=True
    )
    description = models.TextField()
    placement = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=50, blank=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.NEW
    )
    artist_comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Request #{self.pk}"


class RequestReference(models.Model):
    request = models.ForeignKey(
        TattooRequest, on_delete=models.CASCADE, related_name="references"
    )
    image = models.ImageField(upload_to="references/")

    def __str__(self):
        return f"Reference #{self.pk}"


class Appointment(models.Model):
    request = models.OneToOneField(
        TattooRequest, on_delete=models.CASCADE, related_name="appointment"
    )
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()

    class Meta:
        ordering = ["starts_at"]

    def __str__(self):
        return f"Appointment #{self.pk}"