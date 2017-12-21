# -*- coding:utf-8 -*-
from __future__ import absolute_import, print_function

import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="I1XowkiqMs94Ac72fEp2CXPv0"
consumer_secret="drfnZHVUQrq1dyeqepCrbKyq7HBGWeYJCeTFQZpkLcXkgKFw3P"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="936432882482143235-jNLGPKcasCpZaSqR1D2WarSEshgQcyi"
access_token_secret="YF4ddleSgGxj8BsfmH2eJE50DErFeLr7TsNNKAp08ZvqC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

q = '南海问题'
lang = 'zh'
rpp = 5
print(api.search(q=q, lang=lang, rpp=rpp))
# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status(status='Updating using OAuth authentication via Tweepy!')