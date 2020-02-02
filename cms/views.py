from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from cms.models import Habit, Record
from cms.forms import HabitForm, RecordForm


def habit_list(request):
    """habit list"""
    # return HttpResponse('書籍の一覧')
    habits = Habit.objects.all().order_by('id')

    return render(request, 'cms/habit_list.html', {'habits': habits})


def habit_edit(request, habit_id=None):
    """書籍の編集"""
    # return HttpResponse('書籍の編集')
    if habit_id:   # Habit_id が指定されている (修正時)
        habit = get_object_or_404(Habit, pk=habit_id)
    else:         # book_id が指定されていない (追加時)
        habit = Habit()

    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            habit = form.save(commit=False)
            habit.save()
            return redirect('cms:habit_list')
    else:    # GET の時
        form = HabitForm(instance=habit)  # book インスタンスからフォームを作成

    return render(request, 'cms/habit_edit.html', dict(form=form, habit_id=habit_id))

def habit_del(request, habit_id):
    """書籍の削除"""
    # return HttpResponse('書籍の削除')
    habit = get_object_or_404(Habit, pk=habit_id)
    habit.delete()
    return redirect('cms:habit_list')


class RecordList(ListView):
    """感想の一覧"""
    context_object_name='records'
    template_name='cms/record_list.html'
    paginate_by = 10  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        habit = get_object_or_404(Habit, pk=kwargs['habit_id'])  # 親の書籍を読む
        records = habit.records.all().order_by('id')   # 書籍の子供の、感想を読む
        self.object_list = records

        context = self.get_context_data(object_list=self.object_list, habit=habit)
        return self.render_to_response(context)

def record_edit(request, habit_id, record_id=None):
    """感想の編集"""
    habit = get_object_or_404(Habit, pk=habit_id)  # 親の書籍を読む
    if record_id:   # impression_id が指定されている (修正時)
        record = get_object_or_404(Record, pk=record_id)
    else:               # impression_id が指定されていない (追加時)
        record = Record()

    if request.method == 'POST':
        form = RecordList(request.POST, instance=record)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            record = form.save(commit=False)
            record.habit = habit  # この感想の、親の書籍をセット
            record.save()
            return redirect('cms:record_list', habit_id=habit_id)
    else:    # GET の時
        form = RecordForm(instance=record)  # impression インスタンスからフォームを作成

    return render(request,
                  'cms/record_edit.html',
                  dict(form=form, habit_id=habit_id, record_id=record_id))

def record_del(request, habit_id, record_id):
    """感想の削除"""
    record = get_object_or_404(Record, pk=record_id)
    record.delete()
    return redirect('cms:record_list', habit_id=habit_id)

