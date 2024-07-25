import os
import yaml

config_file = os.getenv('CONFIG_FILE', 'dev-invoke-java-project-local.yaml')

with open(config_file, 'r') as file:
    config_data = yaml.load(file, Loader=yaml.FullLoader)
    print(config_data)

for app in config_data['apps']:
    if app['appId'] == 'target':
        app['appPort'] = 5002
        app['workDir'] = './reply'
        app['command'] = ['java', '-jar', 'target/Reply-0.0.1-SNAPSHOT.jar', '--port=5002']
    elif app['appId'] == 'caller':
        app['appPort'] = 5001
        app['workDir'] = './request'
        app['command'] = ['java', '-jar', 'target/Request-0.0.1-SNAPSHOT.jar', '--port=5001']


updated_data = {
    'project': config_data['project'],
    'apps': config_data['apps'],
    'appLogDestination': config_data.get('appLogDestination', '')
}

with open(config_file, 'w') as file:
    yaml.safe_dump(updated_data, file, default_flow_style=False, sort_keys=False)

print("YAML file has been updated.")


