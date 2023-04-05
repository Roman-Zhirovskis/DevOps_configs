from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Women(models.Model):
    title = models.CharField(max_length=255, default=True, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Контент")
    photo = models.ImageField(upload_to="my_app/image", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Fomous women"
        verbose_name_plural = "Fomous women"
        ordering = ["-time_create", "title"]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Профессиональная деятельность")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Катя Горева"
        ordering = ["id"]
