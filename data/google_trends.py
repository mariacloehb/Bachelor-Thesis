import pandas as pd
import plotly.express as px
from pytrends.request import TrendReq as UTrendReq
import matplotlib.pyplot as plt
GET_METHOD='get'



headers = {
    'authority': 'trends.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': '__utmc=10102256; __utmz=10102256.1701888901.1.1.utmcsr=trends.google.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmd=1; __utma=10102256.1055119552.1701888810.1701888901.1701888901.2; __utmb=10102256.1.9.1701890954886; CONSENT=PENDING+327; SOCS=CAISHAgCEhJnd3NfMjAyMzA5MjUtMF9SQzIaAmVuIAEaBgiAkOioBg; SEARCH_SAMESITE=CgQIsJkB; SID=dwhaRIFcenVNlkMFqKOzb1fWq1PWUOkj01vg2M9V4Ds7uhZdHr1b2Mq9wEeMzmtisubXWQ.; __Secure-1PSID=dwhaRIFcenVNlkMFqKOzb1fWq1PWUOkj01vg2M9V4Ds7uhZdxlL92GxBcVExe58GIvsqmQ.; __Secure-3PSID=dwhaRIFcenVNlkMFqKOzb1fWq1PWUOkj01vg2M9V4Ds7uhZd0B5WeEVivMUJ2h5-9KHt5w.; HSID=A5P3oUmEMou-njHCW; SSID=AqoYhpWTCJ-x414E6; APISID=KyVuT45XzTLWlgH6/AEvyG9icv74hBoyOW; SAPISID=dDrsUT2mXQio99NY/A8QM1A_T5HWFJiPk_; __Secure-1PAPISID=dDrsUT2mXQio99NY/A8QM1A_T5HWFJiPk_; __Secure-3PAPISID=dDrsUT2mXQio99NY/A8QM1A_T5HWFJiPk_; 1P_JAR=2023-12-4-12; _gid=GA1.3.1993259237.1701888810; OTZ=7326414_52_52_123900_48_436380; AEC=Ackid1ThZuN9OpGH4ki3P_8f6Kkl0QoBMIBVNnNryG1739ufI6ffm573H4o; __Secure-1PSIDTS=sidts-CjEBPVxjSmPVgwKc03T_MXD1FtM3n8C1MtmIQryIP9gccyq8LqnVOVi7KBkWAuSQsNK9EAA; __Secure-3PSIDTS=sidts-CjEBPVxjSmPVgwKc03T_MXD1FtM3n8C1MtmIQryIP9gccyq8LqnVOVi7KBkWAuSQsNK9EAA; NID=511=as2TpQVciWCKaSxaYt-xVe-WG2eQFZT6g1jjudKC1xwGZCj-jXsGvgwCv6Q93Sn68PLPnKHgOD2eETlPFb5AcPWpjYMIHdGuZLaL53FJxiy5Tg-4aMRUFmdzMLgOgPjNz40M76QNiwnui6LyOso5XNIAO_xZhen6_uR0Jy52ByJzIllIHgWkphBJ_CUqsb8-T-ZuAHrc_RoKqBCnzVa8ApGSTlTDWtDQPvbEf5gygka08PSNpsRJraQIVkatvpKyjk75KswNUvQXCqzbS66fE-mzlahXg5iXzAbPeEYRh3k9itXtd0y0MmalmaNTh_7zM6WorkSVrdN7tVYWcSPk1J8Zv--OksAPQ8WJKfdT19xxrYOWLdWrlo9qBLVZSO-L_P5aXFTzhEgO5-ZOnwJAmDHNrNlYWbW1KEv7NB0yfz0WRVLJRNSVGgwIZxZqRqf5lHezLhxUps5qEjxUfeiUksXmbnEA1EMU5Xqqvoab-uOn9yszJc5eNpoYQACTQkkc7Nm80WEgkbVev3x7WPsRAOlwafwM4a7EfXCgAx3Xp8dMssPlAWlqaWwtw3RKGZhIrXuCIHlr-t1FcT9eOhYDS2NJShJKnSFQQQxGV42Qny2XJBpXVnlgJCRg_22EU3S_cVkiiqIbUlgp0pu0u8iNHPqLZ3lrZg2w4_E7PyM-2TxbBQg; _gat_gtag_UA_4401283=1; _ga=GA1.3.1055119552.1701888810; SIDCC=ACA-OxO5Ti3bwvMUNqMQxdVlYSEnhawjszUjxz7idu4PWfCxaniKdh4Ap69FAtjNrl2zGLU4vxE; __Secure-1PSIDCC=ACA-OxP0ZI30TcQVuBlLY89U8e-U3j3hXClGE_ZCsdZWzS2ZbqhZmLPS_BKZBNmGZGLvBzCDbLnC; __Secure-3PSIDCC=ACA-OxMOiEGgVmjpAygY7c5xgM5uiWV62q0quf41TNFDuClfn1_DDqn5FVdTSxn11illV-trrrs; _ga_VWZPXDNJJB=GS1.1.1701890950.2.1.1701890959.0.0.0',
    'referer': 'https://trends.google.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"119.0.6045.159"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.159", "Chromium";v="119.0.6045.159", "Not?A_Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"13.5.1"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-client-data': 'CIi2yQEIpbbJAQipncoBCMv9ygEIkqHLAQiGoM0BCPWxzQEI3L3NAQjpxc0BCLrIzQEIpdzNAQjP380BCLXgzQEI4OHNAQjb480BCMbpzQEIss3EIhjAy8wBGMfhzQEYp+rNAQ==',
}


class TrendReq(UTrendReq):
    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["adidas samba"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='', gprop='')

#1 Interest over Time
#data = pytrends.interest_over_time() 
#data = data.reset_index() 
#print(data.head())

#2 Related Queries
data2 = pytrends.related_queries()
#data2 = data2.reset_index()
print(data2)

#plt.plot(data["date"], data["adidas samba"]) 
#plt.show()
#fig = px.line(data, x="date", y=['Sooners'], title='Keyword Web Search Interest Over Time')
#fig.show() 
