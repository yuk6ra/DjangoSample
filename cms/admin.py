from django.contrib import admin

from cms.models import Habit, Record, SmallGoal


class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'habit_name', 'goal', 'start_date')  # 一覧に出したい項目
    list_display_links = ('id', 'habit_name',)  # 修正リンクでクリックできる項目


admin.site.register(Habit, HabitAdmin)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'name', 'comment', 'count')
    list_display_links = ('id', 'name',)


admin.site.register(Record, RecordAdmin)


class SmallGoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'goal_name', 'date')
    list_display_links = ('id', 'goal_name',)


admin.site.register(SmallGoal, SmallGoalAdmin)
