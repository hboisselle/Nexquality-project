from Nexquality.models import Badge, BadgeUser
from django.contrib.auth.models import User
from conditions import eval_conditions


def give_all_badges():
    for user in User.objects.all():
        give_badges_to_user(user)


def give_badges_to_user(user):
    for badge in Badge.objects.all():
        if eval_conditions(badge, 'conditions', user):
            badge_user = BadgeUser(badge=badge, user=user)
            badge_user.save()
