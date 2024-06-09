from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from user_panel.models import UserProfile


class Command(BaseCommand):
    help = 'Create missing user profiles for users without one'

    def handle(self, *args, **options):
        # 获取所有没有关联用户个人资料的用户
        users_without_profile = User.objects.filter(userprofile__isnull=True)
        print(users_without_profile)
        # 遍历这些用户，为每个用户创建一个用户个人资料
        for user in users_without_profile:
            UserProfile.objects.create(user=user, full_name=user.username, phone_number='')

        self.stdout.write(self.style.SUCCESS('Successfully created missing user profiles'))
