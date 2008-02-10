
from django import template
from feedme.models import Feed


class FeedmeLastNode (template.Node):
    def __init__(self, format_string):
        self.title = format_string
        try:
            self.last = Feed.objects.get(feed_title=self.title).rss.entries[0]
        except (Feed.DoesNotExist, IndexError, AttributeError):
            self.last = None
        
    def render(self, context):
        context['feedme_last'] = self.last
        return ''



def get_feedme_last (parser, token):
    """
    {% get_feedme_last <feed_title> %}
    
    For the Feed with the suggested title, get the most recent entry.
    Put it in the context as 'get_feedme_last'.
    """

    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, \
            "%r tag requires a single argument" % token.contents[0]

    if not (format_string[0] == format_string[-1] and \
                format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name

    return FeedmeLastNode(format_string[1:-1])

register = template.Library()
register.tag(get_feedme_last)
