from apiclient import discovery

flow = client.flow_from_clientsecrets('client_secret.json', scope= SERVICE_SCOPE)

credentials = flow.step2_exchange(auth_code)

service = discovery.build('iam', 'v1', credentials=credentials)

service.projects().serviceAccount().create(name='', serviceaccountdata)