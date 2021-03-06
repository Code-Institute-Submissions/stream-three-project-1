# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Sponsor
from news.models import Item
from .forms import MessageForm
from django.template.context_processors import csrf
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


# Create your views here.
# The default home page view.
def home_page(request):

    user = request.user
    news = Item.objects.exclude(category_id=6).order_by('-created_date')
    sponsors = Sponsor.objects.all()
    extra_news = news[7:12]
    headlines = news[:7]

    # The page is neither an archive page nor a team page.
    archive = False
    team = False

    # If a user is logged in and has a favourite team set, show additional news relevant to that team.
    # Otherwise, just show more general news stories instead.
    if user.is_authenticated and user.favourite_team:
        favourite_team = user.favourite_team
        team_news = Item.objects.filter(teams=user.favourite_team.id).order_by('-created_date')[:5]
        return render(request, "home.html", {"news_headlines": headlines, "favourite_team": favourite_team,
                                             "extra_news": team_news, "sponsors": sponsors,
                                             "archive": archive, "team": team})

    else:
        favourite_team = False
        return render(request, "home.html", {"news_headlines": headlines, "extra_news": extra_news,
                                             "sponsors": sponsors, "archive": archive, "team": team,
                                             "favourite_team": favourite_team})


# The contact form view.
def contact(request):

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent!")

        return redirect(reverse('home'))

    else:
        form = MessageForm()

    # The page is neither an archive page nor a team page.
    archive = False
    team = False

    args = {
        'form': form,
        'button_text': 'Send Message',
        'archive': archive,
        'team': team
    }
    args.update(csrf(request))

    return render(request, 'contact.html', args)
