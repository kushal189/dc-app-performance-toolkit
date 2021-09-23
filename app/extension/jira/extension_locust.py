import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401
import logging

logger = init_logger(app_type='jira')


@jira_measure("locust_app_specific_action")
@run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
#     r = locust.get('/rest/tenable/1.0/?product=io', catch_response=True)  # call app-specific GET endpoint
#     content = r.content.decode('utf-8')   # decode response content
#     logging.error("content get" + content)
#     logging.info("content get" + content)
#     logger.locust_info("content get" + content)
#     logger.error("content get" + content)
    
    body = {"accessKey": "f4235a42ea1e4bc2051ffdf1249877ed2ffa9392fcc53767e66943ce998605c1",
            "address": "cloud.tenable.com",
            "assignee": "unassigned",
            "buttonClicked": "save",
            "customQuery": "undefined",
            "enableSync": "true",
            "encryptedSecretKey": "ZTNkOGMwOTFlNGNjNGQ3NTA0NGUwNzMzOGQ1MzBjZDNlMzJlMmVkMTgxMjFkOGRmNDA1MmIwYTRlY2Q3OTNjYgk=",
            "interval": "60", 
            "product": "io", 
            "project": "TESTIO", 
            "proxyPassword": "",
            "proxySetup": "no",
            "proxyUrl": "",
            "proxyUsername": "",
            "reporter": "admin",
            "severity": "info", 
            "syncSince": "08/18/2021 15:01",
            "verifySSL": "undefined"
           }
    r_put = locust.client.put('/rest/tenable/1.0', body, catch_response=True)
    #content_put = r_put.content.decode('utf-8')
    content_put = r_put
    logging.error("content put" + content_put)
    logging.info("content put" + content_put)
    logger.locust_info("content put" + content_put)
    logger.error("content put" + content_put)
    
#     token_pattern_example = '"token":"(.+?)"'
#     id_pattern_example = '"id":"(.+?)"'
#     token = re.findall(token_pattern_example, content)  # get TOKEN from response using regexp
#     id = re.findall(id_pattern_example, content)    # get ID from response using regexp

#     logger.locust_info(f'token: {token}, id: {id}')  # log info for debug when verbose is true in jira.yml file
#     if 'assertion string' not in content:
#         logger.error(f"'assertion string' was not found in {content}")
#     assert 'assertion string' in content  # assert specific string in response content

#     body = {"id": id, "token": token}  # include parsed variables to POST request body
#     headers = {'content-type': 'application/json'}
#     r = locust.post('/app/post_endpoint', body, headers, catch_response=True)  # call app-specific POST endpoint
#     content = r.content.decode('utf-8')
#     if 'assertion string after successful POST request' not in content:
#         logger.error(f"'assertion string after successful POST request' was not found in {content}")
#     assert 'assertion string after successful POST request' in content  # assertion after POST request
