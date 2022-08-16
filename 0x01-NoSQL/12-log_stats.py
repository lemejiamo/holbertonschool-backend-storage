#!/usr/bin/env python3
""" Python script that provides some stats
    about  Nginx logs stored in MongoDB
"""

if __name__ == "__main__":

    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    print("{} logs".format(log_collection.count_documents({})))
    logs = log_collection.find()
    METHODS = {'GET': 0,
               'POST': 0,
               'PUT': 0,
               'PATCH': 0,
               'DELETE': 0}
    status: int = 0

    for log in logs:
        if log.get('method') == 'GET':
            METHODS['GET'] = METHODS['GET'] + 1
            if log.get('path') == '/status':
                status = status + 1
        if log.get('method') == 'POST':
            METHODS['POST'] = METHODS['POST'] + 1
        if log.get('method') == 'PUT':
            METHODS['PUT'] = METHODS['PUT'] + 1
        if log.get('method') == 'PATCH':
            METHODS['PATCH'] = METHODS['PATCH'] + 1
        if log.get('method') == 'DELETE':
            METHODS['DELETE'] = METHODS['DELETE'] + 1

    print('Methods:')
    print('\tmethod GET: {}'.format(METHODS['GET']))
    print('\tmethod POST: {}'.format(METHODS['POST']))
    print('\tmethod PUT: {}'.format(METHODS['PUT']))
    print('\tmethod PATCH: {}'.format(METHODS['PATCH']))
    print('\tmethod DELETE: {}'.format(METHODS['DELETE']))
    print('{} status check'.format(status))
