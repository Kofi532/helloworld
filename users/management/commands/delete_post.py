# delete_all.py
from django.core.management.base import BaseCommand
from posts.models import Post
import pandas as pd
from datetime import datetime
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Deleting all Unapproved Posts records!')
        df = pd.DataFrame(Post.objects.all().values())
        then = df['date']
        now = timezone.now()
        df['duration'] = now - then
        df['duration'] = df['duration'].dt.days
        df1 = df[df['duration'] > 5]
        #df1['dateo'] = [t.strftime('%m/%d/%Y') for t in df1['date']]
        r = list(df1['date'])
        for i in r:

            Post.objects.all().filter(approve='No').filter(date = i).delete()
            print('Successfully deleted all Post "No" records!')
            Post.objects.all().filter(approve='Pending').filter(date = i).delete()
            print('Successfully deleted all Post "Pending" records!')