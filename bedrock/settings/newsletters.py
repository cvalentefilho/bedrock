# If basket isn't responding, use this dictionary of our main newsletters as our
# newsletter list until basket starts working again.
# It would be a good idea to update this now and then from the data in basket.
DEFAULT_NEWSLETTERS = {
    u'about-mozilla': {
        u'active': True,
        u'confirm_message': u'',
        u'description': u'News from the Mozilla Project',
        u'languages': [u'en'],
        u'order': 7,
        u'requires_double_optin': False,
        u'show': False,
        u'title': u'About Mozilla',
        u'vendor_id': u'ABOUT_MOZILLA',
        u'welcome': u'about_welcome'},
    u'mozilla-and-you': {
        u'active': True,
        u'confirm_message': u'',
        u'description': u'A monthly newsletter packed with tips to improve your Firefox experience.',
        u'languages': [u'de',
                       u'en',
                       u'es',
                       u'fr',
                       u'hu',
                       u'id',
                       u'pt-BR',
                       u'ru',
                       u'pl'],
        u'order': 1,
        u'requires_double_optin': True,
        u'show': True,
        u'title': u'Firefox & You',
        u'vendor_id': u'MOZILLA_AND_YOU',
        u'welcome': u'fxandyou_Welcome'},
    u'os': {
        u'active': True,
        u'confirm_message': u'',
        u'description': u'Firefox OS news, tips, launch information and where to buy.',
        u'languages': [u'de',
                       u'en',
                       u'es',
                       u'fr',
                       u'hu',
                       u'id',
                       u'pt-BR',
                       u'ru',
                       u'pl'],
        u'order': 3,
        u'requires_double_optin': True,
        u'show': True,
        u'title': u'Firefox OS',
        u'vendor_id': u'FIREFOX_OS',
        u'welcome': u'OS_welcome'},
}

# Used on the newsletter preference center, included in the "interests" section.
OTHER_NEWSLETTERS = [
    'firefox-desktop',
    'mobile',
    'os',
    'firefox-ios',
    'mozilla-general',
    'firefox-os',
]
