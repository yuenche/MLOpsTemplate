import sys, os
import mlflow
from azureml.core import Workspace
from azureml.core.authentication import AzureCliAuthentication

cli_auth = AzureCliAuthentication()

ws = Workspace(subscription_id="191c696b-4f52-4038-9b9b-27cf6086fa00",
               resource_group="mtcs-ezmldev-rg",
               workspace_name="ezmldev9aml",
               auth=cli_auth)

print("Found workspace {} at location {}".format(ws.name, ws.location))
#ws = Workspace.from_config()

#print("SDK version:", azureml.core.VERSION)
#print("MLflow version:", mlflow.version.VERSION)
#print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')
mlflow_tracking_uri= 'azureml://westeurope.api.azureml.ms/mlflow/v1.0/subscriptions/191c696b-4f52-4038-9b9b-27cf6086fa00/resourceGroups/mtcs-ezmldev-rg/providers/Microsoft.MachineLearningServices/workspaces/ezmldev9aml' 

mlflow.set_tracking_uri(mlflow_tracking_uri)

experiment_name = "train-project-amlcompute"
mlflow.set_experiment(experiment_name)

# dictionary
backend_config = {"COMPUTE": "ezmldev9cxec", "USE_CONDA": True}

remote_mlflow_run = mlflow.projects.run(uri=".", 
                                    parameters={"alpha":0.3},
                                    backend = "azureml",
                                    backend_config = backend_config, 
                                    )
