from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic

from polls.models import *

#-- Class-based GenericView

import logging
logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def queryset(selfs):
        """최근 생성된 질문 5개를 반환함"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# -- Funtion-based View ---------

def vote(request, question_id):
    logger.debug("vote().question_id: %s" % question_id)
    question = get_object_or_404(Question, pk = question_id )
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        #설문 투표 폼을 다시 보여준다.
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect 를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))



# # Create your views here.
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list' : latest_question_list}
#     return render(request,'polls/index.html',context)
#
# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{'question':question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk = question_id )
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError,Choice.DoesNotExist):
#         #설문 투표 폼을 다시 보여준다.
#         return render(request,'polls/detail.html',{
#             'question':question,
#             'error_message':"You didn't select a choice",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # POST 데이터를 정상적으로 처리하였으면,
#         # 항상 HttpResponseRedirect 를 반환하여 리다이렉션 처리함
#         return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
#
# def results(request,question_id):
#     question = get_object_or_404(Question,pk = question_id)
#     return render(request,'polls/results.html',{'question':question})
#
# def get_name(request):
#     #POST 방식이면, 데이터가 담긴 제출된 폼으로 간주함
#     if request.method =='POST':
#         # request 에 담긴 데이터로, 클래스 폼을 생성함
#         form = NameForm(request.POST)
#         #폼에 담긴 데이터가 유효한지 체크함
#         if form.is_valid():
#             #폼 데이터가 유효할시, 데이터는 cleaned_data 로 복사됨
#             new_name = form.cleaned_data['name']
#             #로직에 따라 추가적인 처리를 함
#             return HttpResponseRedirect('/thanks/')
#
#     # POST 방식이 아닐시(GET 요청임),
#     # 빈 폼을 사용자에게 보여줍니다.
#     else:
#         form = NameForm()
#
#     return render(request,'name.html',{'form' : form})