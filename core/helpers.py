def custom_transform(data):
    list_result = []
    for result in data:
        for response in result['respuesta'][0]['data']:
            #print(response)
            list_result.append(response)
    return [{"respuesta": [{"data": list_result}]}]


def custom_transform_lista(data):
    list_result_response= []
    for result in data:
        list_result = []
        for response in result['respuesta']:
            #print(response)
            list_result.append(response['data'])
        list_result_response.append(list_result)
    return [{"respuesta": [{"data": list_result_response}]}]