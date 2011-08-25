import rfc2616
from qwer import *
from untwisted import rfc5234

cookieName = rule('rfc2616.token')

# US-ASCII characters excluding CTLs, whitespace DQUOTE, comma,
# semicolon, and backslash
cookieOctet = qwer('[!#-+--:<-[\]-~]')

cookieValue = qwer('(?:(?:', rule('cookieOctet'), ')*|(?:', rule('rfc5234.DQUOTE'), '(?:', rule('cookieOctet'), ')*', rule('rfc5234.DQUOTE'), '))')
cookiePair = qwer(rule('cookieName'), '=', rule('cookieValue'))
cookieString = qwer(rule('cookiePair'), '(?:; ', rule('cookiePair'), ')*')
