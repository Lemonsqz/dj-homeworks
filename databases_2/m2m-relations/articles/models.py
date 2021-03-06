from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.TextField()
    articles = models.ManyToManyField(
        Article,
        related_name='divs',
        through='Elements'

    )

    def __str__(self):
        return self.name


class Elements(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Раздел")

    general = models.BooleanField(default=False, verbose_name="Основной")

