#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter

# example 1
# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

CONSUMER_KEY = '8J4ChDgB4TENiLeO2gXcmQGzK'
CONSUMER_SECRET = 'wQBzpNpqgKzwk1gCItcJ30270dzJiAgQHv6n9QcF5f4KoodGgg'
OAUTH_TOKEN = '23399092-hPluWow97IVPNenB3ycbAbklvv8i9CyRfVvtnBjxz'
OAUTH_TOKEN_SECRET = 'EJ7GOsacvmZsDikgPzAaoSbw7SWYV1I4dzv2y5EcVzjil'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print(twitter_api)

# example2
# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print(world_trends)
print(us_trends)

# example 3
import json

print(json.dumps(world_trends, indent=1))
print(json.dumps(us_trends, indent=1))

# example 4
world_trends_set = set([trend['name']
                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name']
                     for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

print(common_trends)

# example 5
