#!/usr/bin/python3
# -*- coding: utf-8 -*-

import uuid
from django.db import models
from workflow.models import Program, Office, Stakeholder, Site
from .case import Case

class StartEndDates(models.Model):
    """
    Abstract Base Class to implement start/end dates fields
    """
    # TODO move to its own place
    # TODO Check the start_date < end_date and throw adequate error if else
    # TODO Will we need the same for a Slug field? Does Django offer one?
    start_date = models.CharField(max_length=255, null=True, blank=True)
    end_date = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

class CreatedModifiedDates(models.Model):
    "Mixins for created/modified timestamps"
    # This is the naming used in other models
    create_date = models.DateTimeField(
        null=False, blank=False, auto_now_add=True)
    edit_date = models.DateTimeField(null=False, blank=False, auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Create/Edit dates in UTC timezone
        """
        if self.create_date is None:
            self.create_date = datetime.utcnow()
        self.edit_date = datetime.utcnow()
        super().save(*args, **kwargs)

# class CreatedModifiedBy(models.Model):
#     # ? Can this work with OneToOne field
#     created_by = models.ForeignKey(ActivityUser, null=False, related_name="creator")

class Service(StartEndDates):
    """
    Abstract base class for all kinds of offered services.
    Spec: https://github.com/hikaya-io/activity/issues/412
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=550, null=True, blank=True)
    program = models.OneToOneField(
        Program, null=True, blank=True, on_delete=models.SET_NULL)
    office = models.ForeignKey(
        Office, null=True, blank=True, on_delete=models.SET_NULL)
    site = models.ForeignKey(
        Site, null=True, blank=True, on_delete=models.SET_NULL)
    implementer = models.OneToOneField(
        Stakeholder, null=True, blank=True, on_delete=models.SET_NULL)
    cases = models.ForeignKey(
        Case, null=True, blank=True, on_delete=models.SET_NULL)
    form_verified_by = models.CharField(max_length=255, null=True, blank=True)
    form_filled_by = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def total_individuals_supported(self):
        """
        Number of Individuals, excluding Households, supported by the service
        """
        # TODO Check all individuals, and households and their individuals
        return 0

    @property
    def total_households_supported(self):
        """
        Number of Households, supported by the service
        """
        # TODO Check all individuals, and households and their individuals
        return 0

    @property
    def total_supported(self):
        """
        Number of Individuals, including Households, supported by the service
        """
        # TODO Check all individuals, and households and their individuals
        return 0