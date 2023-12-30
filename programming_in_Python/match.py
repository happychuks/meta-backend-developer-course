http_status_code = 200

match http_status_code:
    case 200 | 201:
        print('Success!')
    case 400:
        print('Bad request')
    case 404:
        print('Not found')
    case 500 | 501:
        print('Internal Server Error')
    case _:
        print('Unknown error')