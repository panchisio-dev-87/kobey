

import requests
import json

def obtener_datos_exportados(company: str, query: str, cookies, authorization):

    cookies = {
        'ASP.NET_SessionId': cookies,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-419,es;q=0.9',
        'Authorization': authorization,
        'Cache-Control': 'no-store',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://prd1.xsalesmobile.net',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'ASP.NET_SessionId=fa00e2mrz5r2ag4jwipiopl1',
    }

    
    data = {
            'Catalog': f"{company}_XSS_441_PRD",
            'Query': query,
            'CultureName': 'es-VE',
            'Decimals': ',',
        }
    
    #return json.loads(response.text).get('Data', {}).get('Result', [])


    try:
        response = requests.post(
        f'https://prd1.xsalesmobile.net/{company}/xsm/QueryBD/ExecuteConsult',
        cookies=cookies,
        headers=headers,
        data=data,
        )
    except Exception as exc:
        print("Error en obtener data de api master...")
        
    finally:
        result_list = []
        response_json = json.loads(response.text)
        data = response_json['Data']['Result']

        if len(data) >0:
            result_list.append({'data': data})
        else:
            result_list.append({'data': [{'result': 'No result'}]})

    return result_list


#result = obtener_datos_exportados("MADELI","SELECT TOP 10 * FROM GENERAL","u4xa2wkosrommtiiiih40tct","Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IiIsIm5iZiI6MTc0ODkzMjQwNywiZXhwIjoxNzQ5NTM3MjA3LCJpYXQiOjE3NDg5MzI0MDd9.RlQv6hItI5W4Wr-l1d1r7cV2d_B2X4gZ9ySsc1F5ZYI")
