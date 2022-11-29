# delete_all.py
from django.core.management.base import BaseCommand
from posts.models import Post
from pages.models import Clubm, Sportm
import pandas as pd
from datetime import datetime
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Deleting all Unapproved Posts records!')
        df = pd.DataFrame(Clubm.objects.all().values())
        then = df['date']
        now = timezone.now()
        df['duration'] = now - then
        df['duration'] = df['duration'].dt.days
        df1 = df[df['duration'] > 5]
        #df1['dateo'] = [t.strftime('%m/%d/%Y') for t in df1['date']]
        r = list(df1['date'])
        for i in r:

            Clubm.objects.all().filter(approve='No').filter(date = i).delete()
            print('Successfully deleted all Club "No" records!')
            Clubm.objects.all().filter(approve='Pending').filter(date = i).delete()
            print('Successfully deleted all Club "Pending" records!')