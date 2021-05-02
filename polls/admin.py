from django.contrib import admin
from polls.models import Question,Choice

#Question 및 choice 한 화면에서 변경하기
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline): #테이블 형식으로 보여주기
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text'] #필드 순서 변경

    # 각 필드를 분리해서 보여주기
    fieldsets = [
        ('Question Statement',{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
        # Collapse : 필드 접기
    ]
    inlines = [ChoiceInline] #Choice 모델 클래스 같이보기
    list_display = ('question_text','pub_date') # 레코드 리스트 칼럼 항목 지정
    list_filter = ['pub_date'] #필터 사이드 바 추가
    search_fields = ['question_text'] #검색 박스 추가

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)










