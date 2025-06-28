
#XSS
import concurrent

from core.api_master import obtener_datos_exportados
from core.supabase_helper import supabase_get_session_by_company_base


def data_default_xss(company_name, query_list):
    try:
        query = query_list[0]['query']
        master = supabase_get_session_by_company_base(company_name['name'])
        #master = mongo_get_session_by_company_base(company_name['name'])
        x = obtener_datos_exportados(master['company_base'], query, master['cookie'], master['authorization'])
        #print(x)
    except Exception as exc:
        x = [{"data": [{"respuesta": f"{company_name['name']} error"}]}]

    return {"zonal":company_name['name'],"respuesta":x}


def get_defaul_xss_data(company_list, query_list):
    info = []    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for company in company_list:
            futures.append(
                executor.submit(
                    data_default_xss, company_name=company , query_list=query_list
                )
            )
        for future in concurrent.futures.as_completed(futures): 
            info.append(future.result())           
            #print(future.result())
    return info

