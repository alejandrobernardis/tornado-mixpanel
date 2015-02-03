#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Asumi Kamikaze Inc.
# Licensed under the MIT License.
# Author: Alejandro M. Bernardis
# Email: alejandro (dot) bernardis (at) asumikamikaze (dot) com
# Created: 03/Feb/2015 12:48

from __future__ import absolute_import, division, print_function, with_statement


# Version

version = '0.1-dev'
version_tuple = (0, 1, 0, -1)


# Mixpanel Settings

MIXPANEL_EVENTS = 'events'
MIXPANEL_PEOPLE = 'people'
MIXPANEL_IMPORTS = 'imports'

MIXPANEL_ENDPOINTS = {
    MIXPANEL_EVENTS: 'https://api.mixpanel.com/track',
    MIXPANEL_PEOPLE: 'https://api.mixpanel.com/engage',
    MIXPANEL_IMPORTS: 'https://api.mixpanel.com/import'
}

MIXPANEL_ENDPOINTS_KEYS = frozenset(MIXPANEL_ENDPOINTS.keys())
