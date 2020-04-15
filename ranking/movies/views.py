from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie, MovieScore
from member.decorators import member_only

# Create your views here.
def top5(request):
    return HttpResponse('hello! :)')

@member_only
def score(request):
    #data = Movie.objects.filter(moviescore__member_id__isnull=True, moviescore__member_id=request.session['member_id'])
    movies = Movie.objects.all()
    scores_ = MovieScore.objects.filter(member_id=request.session['member_id'])
    scores = {}
    for scr in scores_:
        scores[scr.movie_id] = scr.score

    return render(request, 'movies/score.html', {'scores': scores, 'movies': movies})
