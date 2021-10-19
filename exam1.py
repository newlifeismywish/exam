import urllib.parse
import urllib.request

url="https://cn.investing.com/instruments/HistoricalDataAjax"

headers = {
    'Cookie': 'SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226408%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A28%3A%22%2Fequities%2Fapple-computer-inc%22%3B%7D%7D%7D%7D; geoC=TW; adBlockerNewUserDomains=1632443275; udid=f5c282639193f707b19265267e9d33c8; __cflb=0H28uxmf5JNxjDUC6WDvQUEoJyvKUTs1a69GqfM1jtG; protectedMedia=2; __gads=ID=a6aa00f6c4e08974:T=1632443275:S=ALNI_MZW4u5xtkYWOiA1MjX-HJ9XXSetdg; _ga=GA1.2.2041554735.1632443276; _gid=GA1.2.1222823550.1632443278; G_ENABLED_IDPS=google; adsFreeSalePopUp=3; PHPSESSID=bllm8f50vre78tnor92uqng4s8; StickySession=id.1833530997.488cn.investing.com; logglytrackingsession=98050507-0adc-468b-b3d6-84f36b36e8d8; smd=f5c282639193f707b19265267e9d33c8-1632462931; nyxDorf=MzRjMTZgN3UwZD01YzAwLDdnYzE1MWB8YWJnbA%3D%3D; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1632457405,1632459372,1632462935,1632463215; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1632463215',
    'Origin': 'https://cn.investing.com',
    'Referer': 'https://cn.investing.com/equities/apple-computer-inc-historical-datae',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}


values={'curr_id': '6408',
        'smlID': '1159963',
        'header': 'AAPL历史数据',
        'st_date': '2021/08/20',
        'end_date': '2021/09/14',
        'interval_sec': 'Daily',
        'sort_col': 'date',
        'sort_ord': 'DESC',
        'action': 'historical_data'
       }

data = urllib.parse.urlencode(values).encode('utf-8') # data should be bytes

req = urllib.request.Request(url, data=data, headers=header)
response = urllib.request.urlopen(req)
page = response.read().decode("utf-8")
print("test")
