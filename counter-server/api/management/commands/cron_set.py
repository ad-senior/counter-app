from crontab import CronTab
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Set up cron-job to reset count every month'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with CronTab(user='<username>') as cron:  # Change the username to yours
            job = cron.new(command="curl -X POST -d '{}' "
                                   "http://127.0.0.1:8000/api/counter/reset/")
            job.dow.on(1)
            job.hour.on(0)
            job.minute.on(0)
