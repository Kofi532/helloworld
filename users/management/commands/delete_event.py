# delete_all.py
from django.core.management.base import BaseCommand
from posts.models import Post
from pages.models import Clubm, Sportm
from approve.models import Cals
import pandas as pd
from datetime import datetime
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Deleting all Event records!')
        Cals.objects.all().filter(act = 'Yes').delete()
        print('Successfully deleted all Event records!')
