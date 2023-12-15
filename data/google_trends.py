import pandas as pd
from pytrends.request import TrendReq as UTrendReq
import matplotlib.pyplot as plt
GET_METHOD='get'

headers = {
    'authority': 'trends.google.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': '__utmc=10102256; __utmz=10102256.1702486274.4.3.utmcsr=trends.google.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmd=1; __utmt=1; __utma=10102256.1055119552.1701888810.1702495683.1702486274.6; __utmb=10102256.2.10.1702486274; CONSENT=PENDING+327; SOCS=CAISHAgCEhJnd3NfMjAyMzA5MjUtMF9SQzIaAmVuIAEaBgiAkOioBg; SEARCH_SAMESITE=CgQIsJkB; SID=dwhaRIFcenVNlkMFqKOzb1fWq1PWUOkj01vg2M9V4Ds7uhZdHr1b2Mq9wEeMzmtisubXWQ.; __Secure-1PSID=dwhaRIFcenVNlkMFqKOzb1fWq1PWUOkj01vg2M9V4Ds7uhZdxlL92GxBcVExe58GIvsqmQ.; __Secure-3PSID=dwhaRIFcenVNlkMFqKOzb1fWq1PWUOkj01vg2M9V4Ds7uhZd0B5WeEVivMUJ2h5-9KHt5w.; HSID=A5P3oUmEMou-njHCW; SSID=AqoYhpWTCJ-x414E6; APISID=KyVuT45XzTLWlgH6/AEvyG9icv74hBoyOW; SAPISID=dDrsUT2mXQio99NY/A8QM1A_T5HWFJiPk_; __Secure-1PAPISID=dDrsUT2mXQio99NY/A8QM1A_T5HWFJiPk_; __Secure-3PAPISID=dDrsUT2mXQio99NY/A8QM1A_T5HWFJiPk_; OTZ=7326414_52_52_123900_48_436380; AEC=Ackid1TYBkzxqJoY_EJT0sWvtbG0vYobLhDkMXLrlbf4qNngJZLwhUH_1ko; 1P_JAR=2023-12-13-11; _gid=GA1.3.1303719259.1702469588; _ga=GA1.3.1055119552.1701888810; NID=511=gf2qsKHYoXTbkvAJG3s22k9TVcK8gkYaGHag_I-T4WSVUl9HRPEVzktLKuRDPbmXwrH-2MdjysXD-B0Y355wF63x87MfILvn6ztJN9ZrSLkqWcK8UW-9jhR0MdInMarx_18yHCB60qp95sIANX2ty4QXUfTyfc7L--muTlUoU6kcCoCWFbdeP3TZ_Mz4GlmWGW5u_LzhnXLfsLyPpT_qVEKOC9z11m6IJewrgYhVDyLIv5mB3mxUb3ynK9nm4HrH9IEGYAWBa2-nwi7RcUg2abP_pc8TkgtmIy77g6RR222yTrSOaefAuTx8YrU1uePE4HCI9_ewCNWLhjTm-IFugQlkXGLkEXsgNMl5EdfjFnhfnXhYl7NDuxBYdUI9q5UWjZFUWIyIQek69xtr3ZYsiO-aJ8Wmte-uVC7xrrMD9wpSNep9BRK6HQTieaYuvWi--Foa42k0fXu3YjR4GwQJp29SDLz5kWGxbAlcVG9Rfma7WGmwsGD9U-7y_P_fWGuIRvUbOgIITu3GNMg0_TINpm3w5k-ptiD5ZvLlixOQmQQ2wbtm9UvQQkHsLqnhU67BRnz-f8GPVQCJ1RcO9glhOVwNPgXjaiUIj2B--sdEqRxq11C-719xVojlcrwcTeKk54whplejl-oKGSxLWvl3HFEF1-p-oQxK5oI1rICDvWLwutgcZTZ9; __Secure-1PSIDTS=sidts-CjEBPVxjSmT_vG7h8uS2OygdqI_lLZQTV2M70qlEybNSHaR0FhwFUuUrj9GAWvRKCGBIEAA; __Secure-3PSIDTS=sidts-CjEBPVxjSmT_vG7h8uS2OygdqI_lLZQTV2M70qlEybNSHaR0FhwFUuUrj9GAWvRKCGBIEAA; _ga_VWZPXDNJJB=GS1.1.1702566267.7.0.1702566267.0.0.0; _gat_gtag_UA_4401283=1; SIDCC=ACA-OxMQgrgIHEvmPqEJCrrriy2gIQkXoYet-bq4ybrwZ9niD8ps1INXWuBdHvMQ0m15rclwuDU; __Secure-1PSIDCC=ACA-OxPGjmhd1J99wbJb87JzLQmRKVv14YFtfhPXxUM2AcMFDLFpYk5L8ZKFu2QGQzi3reoOzyY3; __Secure-3PSIDCC=ACA-OxNdJr8HTRYp4FA4_wEuhK3kJXBAjy3YCS4LBNAvt8bKPvusLpzVZX1UFruhDnQ6H_xxFYk',
    'referer': 'https://trends.google.com/trends/explore?date=2021-01-01%202023-12-14&q=prada%20nylon%20bag&hl=en-GB',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"119.0.6045.199"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.199", "Chromium";v="119.0.6045.199", "Not?A_Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"13.5.1"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-client-data': 'CIi2yQEIpbbJAQipncoBCMv9ygEIlKHLAQiGoM0BCPWxzQEI3L3NAQjpxc0BCLrIzQEI49rNAQil3M0BCM/fzQEIteDNAQjg4c0BCNvjzQEIxunNAQiyzcQiGMDLzAEYx+HNARin6s0B',
}

# Extend the default class
class TrendReq(UTrendReq):
    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)

#Modifiable filters
timeframe='2021-01-01 2023-01-12'
kw_list = ["vetements", "miu miu"]


# Instantiate the pytrends class and build the payload
pytrends = TrendReq(retries=0,hl='en-US', tz=360)
pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='', gprop='')

#1 Interest over Time
data = pytrends.interest_over_time() 
data = data.reset_index() 
print(data.head())

#2 Related Queries
# data2 = pytrends.related_queries()
#data2 = data2.reset_index()
#print(data2)

# Plotting results
start, end = timeframe.split()
plt.plot(data[kw_list[0]], label=kw_list[0])
# Ucomment if plotting two items
plt.plot(data[kw_list[1]], label=kw_list[1])
plt.title(f"Popularity over time for: {kw_list[0]}")
plt.ylabel("Popularity")
plt.xlabel("Time")
plt.xticks([0, len(data[kw_list[0]])], [start, end])
plt.legend()
plt.show()
