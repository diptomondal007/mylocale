from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from generic.variables import LOGIN_URL

from home.models import Issue, IssueComment, IssueVote
from home.forms import IssueForm, IssueCommentForm


def view(request):
	try:
		context = {}

		# issue = Issue.objects.get(uid=uid)
		# comments = IssueComment.objects.filter(issue_id=uid)

		# context['issue'] = issue
		# context['comments'] = comments

		return render(request, 'home/issue/view.html', context)

	except ObjectDoesNotExist as e:
		return HttpResponse('invalid request')



@login_required(login_url=LOGIN_URL)
def create(request):
	if request.user.is_staff:
		return HttpResponse('You are not allowed to create issue')
	context = {}
	

	form = IssueForm()
	context['form'] = form

	return render(request, 'home/issue/create.html', context)



def list(request):
	context = {}
	issue_list = Issue.objects.all()
	context['issue_list'] = issue_list

	return render(request, 'home/issue/list.html', context)

