from colorful.fields import RGBColorField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager


class Color(models.Model):

    name = models.CharField(_('Name'), max_length=140)
    color = RGBColorField()

    def __unicode__(self):
        return self.name

    def color_display(self):
        return '<span style="display: inline-block; width: 13px; height: 13px; background-color: %(c)s; border: 1px solid #000; margin-right: 7px;"></span> %(c)s' % {'c': self.color, }
    color_display.allow_tags = True
    color_display.short_description = _('Color')

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')
        ordering = ['name', ]


class Calendar(models.Model):

    name = models.CharField(_('Name'), max_length=140)
    slug = models.SlugField(_('Slug'), unique=True, db_index=True)

    color = models.ForeignKey(Color)

    def __unicode__(self):
        return self.name

    def color_display(self):
        return '<span style="display: inline-block; width: 13px; height: 13px; background-color: %(c)s; border: 1px solid #000; margin-right: 7px;"></span>' % {'c': self.color.color, }
    color_display.allow_tags = True
    color_display.short_description = _('Color')

    class Meta:
        verbose_name = _('Calendar')
        verbose_name_plural = _('Calendars')
        ordering = ['name', ]


# Also known as Type, didn't want to use because of naming
# conflicts; classification was the best I could come up with.
class Classification(models.Model):

    name = models.CharField(_('Name'), max_length=140)
    slug = models.SlugField(_('Slug'))
    description = models.TextField(_('Description'), blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Classification')
        verbose_name_plural = _('Classifications')
        ordering = ['name', ]


class Event(models.Model):

    # Base Fields
    calendar = models.ForeignKey(Calendar)
    name = models.CharField(_('Name'), max_length=140)
    slug = models.SlugField(_('Slug'))
    description = models.TextField(_('Description'), blank=True, null=True)

    # Date Time Fields
    start_date_time = models.DateTimeField(_('Start Date Time'))
    end_date_time = models.DateTimeField(_('End Date Time'), blank=True, null=True)
    all_day_event = models.BooleanField(_('All Day Event'), default=False)

    # Classification
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        date_format = '%Y-%m-%d %I:%M %p'
        if self.all_day_event:
            date_format = '%Y-%m-%d'
        return '%(n)s (%(d)s)' % {'n': self.name, 'd': self.start_date_time.strftime(date_format), }

    def active(self):
        if self.start_date_time and self.end_date_time:
            t = timezone.now()
            return self.start_date_time <= t and self.end_date_time >= t
        return False
    active.boolean = True
    active.short_description = _('Active')

    def calendar_color(self):
        return '<span style="display: inline-block; width: 13px; height: 13px; background-color: %(c)s; border: 1px solid #000; margin-right: 7px;"></span> %(cn)s' % {'c': self.calendar.color.color, 'cn': self.calendar.name, }
    calendar_color.allow_tags = True
    calendar_color.short_description = _('Calendar')

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


class EventClassification(models.Model):

    event = models.ForeignKey(Event)
    classification = models.ForeignKey(Classification)

    def __unicode__(self):
        return '%(e)s: %(c)s' % {'e': self.event.name, 'c': self.classification.name}

    class Meta:
        verbose_name = _('Event Classification')
        verbose_name_plural = _('Event Classifications')
