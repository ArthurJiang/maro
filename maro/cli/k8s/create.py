# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.


import yaml

from maro.cli.k8s.executors.k8s_azure_executor import K8sAzureExecutor
from maro.utils.exception.cli_exception import ParsingError


def create(deployment_path: str, **kwargs):
    with open(deployment_path, 'r') as fr:
        create_deployment = yaml.safe_load(fr)

    try:
        if create_deployment['mode'] == 'k8s':
            if create_deployment['cloud']['infra'] == 'azure':
                K8sAzureExecutor.build_cluster_details(create_deployment=create_deployment)
                executor = K8sAzureExecutor(cluster_name=create_deployment['name'])
                executor.create()
            else:
                raise ParsingError(f"Deployment is broken: Invalid infra: {create_deployment['cloud']['infra']}")
        else:
            raise ParsingError(f"Deployment is broken: Invalid mode: {create_deployment['mode']}")
    except KeyError as e:
        raise ParsingError(f"Deployment is broken: Missing key: '{e.args[0]}'")
