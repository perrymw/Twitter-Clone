from twitterclone.notifications.models import *
from twitterclone.twitterusers.models import *
from twitterclone.tweets.models import *
from twitterclone.notifications.models import *

"""
This is a dirty hack because Django does not want to read models that are not
in the base directory of the application. This just ensures that Django will
always be able to see the models that we modify / create.
~ Joe
"""