from Nexquality.models import Badge, BadgeUser
from django.contrib.auth.models import User
from conditions import eval_conditions


def attribute_badges():
    for user in User.objects.all():
        attribute_badge_to_user(user)


def attribute_badge_to_user(user):
    for badge in Badge.objects.all():
        if eval_conditions(badge, 'conditions', user):
            try:
                BadgeUser.objects.get(badge=badge, user=user, badge__given_once=True)
            except BadgeUser.DoesNotExist:
                badge_user = BadgeUser(badge=badge, user=user)
                badge_user.save()
                print('Attributed badge {0} to {1}'.format(badge.name, user.get_full_name()))
            except:
                print('Error importing badge' + badge.name)
