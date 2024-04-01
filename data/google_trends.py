import pandas as pd
from pytrends.request import TrendReq as UTrendReq
import matplotlib.pyplot as plt
GET_METHOD='get'

headers = {
    'authority': 'trends.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '__utmc=10102256; __utmz=10102256.1710249981.2.2.utmcsr=trends.google.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=10102256.1073393946.1710198453.1710440006.1710443659.16; __utmt=1; __utmb=10102256.2.10.1710443659; CONSENT=PENDING+279; 1P_JAR=2024-2-27-15; SOCS=CAISHAgCEhJnd3NfMjAyNDAyMjgtMF9SQzEaAmVuIAEaBgiAnpSvBg; SID=g.a000hQjGqxlzCrdOl_Gsz88KxZ4NiQ6jiy0sfJIA3NAUX3peVyJWtSBJ93MuiPpxmjgoeZQlXQACgYKATgSAQASFQHGX2Mihm4saeLV9122CKP9Aw4fwhoVAUF8yKqwwpLe1B31GmCKv2SF5Gmw0076; __Secure-1PSID=g.a000hQjGqxlzCrdOl_Gsz88KxZ4NiQ6jiy0sfJIA3NAUX3peVyJWJw3JVqgzRhfkyPZI-2lxpgACgYKAXoSAQASFQHGX2MiPLbBODOnKYl7gkg04pG5uxoVAUF8yKpGjiJII09ly5XSzN7S6sMB0076; __Secure-3PSID=g.a000hQjGqxlzCrdOl_Gsz88KxZ4NiQ6jiy0sfJIA3NAUX3peVyJWmeOXjEWmQ5YGFsyVxRNvuQACgYKAc0SAQASFQHGX2MiUrmy3XLfV76FSC4Ko7d8-xoVAUF8yKqWK_ITusVcCVklx0TIuE0L0076; HSID=A8Rwu5BAEeWLvqij3; SSID=Axj-Cje-6uvmD54BT; APISID=l0slnol_hLoEGBd8/AFqSUsBLhjFvjy-Ks; SAPISID=tEFiM45AVeoyuk5b/AgFCu-ms7JLyDqfX5; __Secure-1PAPISID=tEFiM45AVeoyuk5b/AgFCu-ms7JLyDqfX5; __Secure-3PAPISID=tEFiM45AVeoyuk5b/AgFCu-ms7JLyDqfX5; _gid=GA1.3.516185276.1710198454; OTZ=7464908_52_52_123900_48_436380; AEC=Ae3NU9OgHz8_XbBOPaeOnDFMU3-V3ClGTJPPB72l0H8lhDmBRsLa5gtNnQ; NID=512=KKeYEuMxmeWGUW7pTZsAPUcBUHEaAgtss0TziqwVCi3tnIGIuLLT5L9oMiTKc1CUdg0JuYD1lSopq-6b-PQujDDgtRFWASUmQqzw0RmjtuxeGJQHDHd9EiPPBcLACcMAmrZZ2oZilY-CA1Bny7BiOHSSUvs2bVVD2qDzK_zGOvslpujKXHSPkV_3zPNVbKPF2I_raKdhUl6JVOUIIy3gZyCAQoj118cHzSoAsOTxU0i-pAIi3S69lDdgVSD4qDP-f3-eCMIFX41CIyDOL_BiPbDgGP5EdNUmRk_Xz3EKeNg7IOi6eluT9FIb7jHxeGgx5Oi1bFL-fzLNsPElc9iqnel9Fq2_nKL6MccSlRFlzGK52q_tNVk0; __Secure-1PSIDTS=sidts-CjEBYfD7Z-zleApCI-VKnrAPlKqbiPbCzB2RwLmerTOctt4W4Xi74v-BNXL1TE8YcWm4EAA; __Secure-3PSIDTS=sidts-CjEBYfD7Z-zleApCI-VKnrAPlKqbiPbCzB2RwLmerTOctt4W4Xi74v-BNXL1TE8YcWm4EAA; _ga=GA1.3.1073393946.1710198453; _gat_gtag_UA_4401283=1; _dd_s=logs=1&id=c99f5ebf-feda-4baf-8607-df032db07831&created=1710443658919&expire=1710444599648; _ga_VWZPXDNJJB=GS1.1.1710443658.17.1.1710443699.0.0.0; SIDCC=AKEyXzXrHO_G1JCATRUZ6HzZvCrhStcJibs85OZmSi2cZepNZXkoNIIJjcz8xhIS7GwElB6m4G4; __Secure-1PSIDCC=AKEyXzVMbL8ZYrK0JKeSzj8aUIDvXPrscte4hobshHDjPjhdmfMaaS7pdYdoJ20lGwSRLwHmVPPM; __Secure-3PSIDCC=AKEyXzWC10-pnr0Apzqhx5kphuh-Ota_BH_qyRV-_ss9vv2WWrnIIDdknB_gS-TrjG1fFqea_bc',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"122.0.6261.69"',
    'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.69", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.69"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"13.4.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-client-data': 'CIu2yQEIo7bJAQipncoBCMvuygEIlaHLAQiGoM0BCM7uzQEI5vXNAQjq980BCOn7zQEI2P/NAQjBgM4BGMHLzAEYnfjNARjK+M0B',
}

# Extend the default class
class TrendReq(UTrendReq):
    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)


def get_google_trends_data(keywords, timeframe='today 5-y', geo='', gprop=''):
    # Initialize a pytrends request object
    pytrends = TrendReq(hl='en-US', tz=360)

    # Build the payload
    pytrends.build_payload(kw_list=keywords, timeframe=timeframe, geo=geo, gprop=gprop)

    # Fetch the interest over time
    df = pytrends.interest_over_time()
    df = df.reset_index() 
    # If the dataframe is empty, return None
    if df.empty:
        return None

    # Drop the 'isPartial' column if it exists
    if 'isPartial' in df.columns:
        df = df.drop(columns='isPartial')

    return df

# # Plotting results
# start, end = timeframe.split()
# plt.plot(data[kw_list[0]], label=kw_list[0])
# # Ucomment if plotting two items
# #plt.plot(data[kw_list[1]], label=kw_list[1])
# plt.title(f"Popularity over time for: {kw_list[0]}")
# plt.ylabel("Popularity")
# plt.xlabel("Time")
# plt.xticks([0, len(data[kw_list[0]])], [start, end])
# plt.legend()
# plt.show()


