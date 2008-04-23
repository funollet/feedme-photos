from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = """Refreshes every Feed ("Feedme for Django" application.)"""
    
    requires_model_validation = False

    def handle_noargs(self, **options):
        from feedme.models import Feed
        
        feeds = Feed.objects.all()
        for some_feed in feeds:
            some_feed.update (force_update=True)

