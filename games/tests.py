# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .views import last_and_next, league_standings, games_team, results_list, fixture_list,\
    full_results, full_fixtures, season_archive, season_overview, season_team
from django.core.urlresolvers import resolve


# Test the display of the most recent results and next scheduled fixtures.
class LastNextTest(TestCase):

    fixtures = ['games', 'teams']

    def test_last_and_next_resolves(self):
        results_latest = resolve('/scores/')
        self.assertEqual(results_latest.func, last_and_next)

    def test_last_and_next_code(self):
        results_latest = self.client.get('/scores/')
        self.assertEqual(results_latest.status_code, 200)

    def test_last_and_next_content(self):
        results_latest = self.client.get('/scores/')
        self.assertTemplateUsed(results_latest, 'games_latest.html')


# Test the display of the league standings.
class LeagueStandingsTest(TestCase):

    fixtures = ['teams']

    def test_league_standings_resolves(self):
        standings = resolve('/standings/')
        self.assertEqual(standings.func, league_standings)

    def test_league_standings_code(self):
        standings = self.client.get('/standings/')
        self.assertEqual(standings.status_code, 200)

    def test_league_standings_content(self):
        standings = self.client.get('/standings/')
        self.assertTemplateUsed(standings, 'season_standings.html')


# Test the display of individual team's schedule of games.
class GamesTeamTest(TestCase):

    fixtures = ['games', 'teams']

    def test_games_team_resolves(self):
        scores_team = resolve('/scores/london/')
        self.assertEqual(scores_team.func, games_team)

    def test_games_team_code(self):
        scores_team = self.client.get('/scores/london/')
        self.assertEqual(scores_team.status_code, 200)

    def test_games_team_content(self):
        scores_team = self.client.get('/scores/london/')
        self.assertTemplateUsed(scores_team, 'games_team.html')


# Test the view which shows details of all past games in paginated format.
class FullResultsTest(TestCase):

    fixtures = ['teams']

    def test_full_results_resolves(self):
        more_results = resolve('/scores/results/')
        self.assertEqual(more_results.func, full_results)

    def test_full_results_code(self):
        more_results = self.client.get('/scores/results/')
        self.assertEqual(more_results.status_code, 200)

    def test_full_results_content(self):
        more_results = self.client.get('/scores/results/')
        self.assertTemplateUsed(more_results, 'results_full.html')


# Test the view which shows details of future past games in paginated format.
class FullFixturesTest(TestCase):

    fixtures = ['teams']

    def test_full_fixtures_resolves(self):
        more_fixtures = resolve('/scores/fixtures/')
        self.assertEqual(more_fixtures.func, full_fixtures)

    def test_full_fixtures_code(self):
        more_fixtures = self.client.get('/scores/fixtures/')
        self.assertEqual(more_fixtures.status_code, 200)

    def test_full_fixtures_content(self):
        more_fixtures = self.client.get('/scores/fixtures/')
        self.assertTemplateUsed(more_fixtures, 'fixtures_full.html')


# Test the display of a full list of past games on single page.
class ResultsListTest(TestCase):

    fixtures = ['teams']

    def test_results_list_resolves(self):
        all_results = resolve('/scores/results/all/')
        self.assertEqual(all_results.func, results_list)

    def test_results_list_code(self):
        all_results = self.client.get('/scores/results/all/')
        self.assertEqual(all_results.status_code, 200)

    def test_results_list_content(self):
        all_results = self.client.get('/scores/results/all/')
        self.assertTemplateUsed(all_results, 'results_list.html')


# Test the display of a full list of future games on single page.
class FixtureListTest(TestCase):

    fixtures = ['teams']

    def test_fixture_list_resolves(self):
        all_fixtures = resolve('/scores/fixtures/all/')
        self.assertEqual(all_fixtures.func, fixture_list)

    def test_fixture_list_code(self):
        all_fixtures = self.client.get('/scores/fixtures/all/')
        self.assertEqual(all_fixtures.status_code, 200)

    def test_fixture_list_content(self):
        all_fixtures = self.client.get('/scores/fixtures/all/')
        self.assertTemplateUsed(all_fixtures, 'fixture_list.html')


# Test the archive home page.
class SeasonArchiveTest(TestCase):

    fixtures = ['teams']

    def test_season_archive_resolves(self):
        archive_index = resolve('/archive/')
        self.assertEqual(archive_index.func, season_archive)

    def test_season_archive_code(self):
        archive_index = self.client.get('/archive/')
        self.assertEqual(archive_index.status_code, 200)

    def test_season_archive_content(self):
        archive_index = self.client.get('/archive/')
        self.assertTemplateUsed(archive_index, 'season_archive.html')


# Test the single season archive pages.
class SeasonOverviewTest(TestCase):

    fixtures = ['games', 'teams']

    def test_season_overview_resolves(self):
        past_season = resolve('/archive/2000/')
        self.assertEqual(past_season.func, season_overview)

    def test_season_overview_code(self):
        past_season = self.client.get('/archive/2000/')
        self.assertEqual(past_season.status_code, 200)

    def test_season_overview_content(self):
        past_season = self.client.get('/archive/2000/')
        self.assertTemplateUsed(past_season, 'season_overview.html')


# Test the team season archive pages.
class SeasonTeamTest(TestCase):

    fixtures = ['games', 'teams']

    def test_season_team_resolves(self):
        team_season = resolve('/archive/2000/cardiff/')
        self.assertEqual(team_season.func, season_team)

    def test_season_team_code(self):
        team_season = self.client.get('/archive/2000/cardiff/')
        self.assertEqual(team_season.status_code, 200)

    def test_season_team_content(self):
        team_season = self.client.get('/archive/2000/cardiff/')
        self.assertTemplateUsed(team_season, 'season_team.html')
