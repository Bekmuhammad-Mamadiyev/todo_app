from django.contrib import admin
import requests
from todo.models import Todo


def send_task_telegram(self,request,queryset):
    for todo in queryset:
        text = f"{todo.id},{todo.name}"
        text+=f'{todo.description}'
        send_teg_bot(text)



def send_teg_bot(text):
    TOKEN = '6450537541:AAHpVFkCt11KBHLd7WzOTJY54UF3omcZQ-o'
    CHAT_ID = 1564944477
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}'
    requests.get(url)

send_task_telegram.short_description = 'telegramga yuborish'



@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','name','status')
    search_fields = ('name',)
    list_filter = ('status',)

    actions = (send_task_telegram,)