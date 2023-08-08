import time

from anylearn.applications.hpo_experiment import HpoExperiment
from anylearn.config import init_sdk
from anylearn.interfaces import Project

init_sdk('http://192.168.10.22:31888', 'xlearn', '123456')

print("Create a project first...")
project = Project(
    name=f"TEST_SDK_HPO_{int(time.time())}",
    description="SDK_HPO_EXPERIMENT",
    datasets=['DSET3b9ae2f511ebaba35e9e5b63a5ec'],
)
project.save()

print("Create HPO...")
hpo = HpoExperiment(
    project_id=project.id,
    algorithm_id='ALGOcc0ad87c11eb92956a66e48fa05c',
    dataset_id='DSET3b9ae2f511ebaba35e9e5b63a5ec',
    dataset_hyperparam_name='data-path',
    hpo_search_space={
        'batch-size': {'_type': "choice", '_value': [32, 64, 128]},
        'epochs': {'_type': "choice", '_value': [3, 6, 12]},
        'learning-rate': {'_type': "choice", '_value': [0.001, 0.01]}
    },
    hpo_max_runs=5,
)
hpo.save()

while not hpo.hpo_id:
    time.sleep(2)
    hpo.get_detail()

print("HPO created on Anylearn:")
print(hpo)

while not hpo.tasks:
    print("Waiting for first trial finish...")
    time.sleep(30)
    hpo.get_detail()

print("Get some meta log (nnimanager.log), not really helpful...")
meta_log = hpo.get_log()
[print(l) for i, l in enumerate(meta_log) if i < 5]

print("Get some more detailed trial logs (trial.log, stderr, stdout), which could be helpful sometimes...")
trial_logs = hpo.get_trial_logs()
[print(l) for i, l in enumerate(trial_logs[list(hpo.tasks.keys())[0]]['log']) if i < 10]

print("Transform the current best model")
model = hpo.transform_best_model(model_name=f"TEST_SDK_HPO_INCUMBENT_{int(time.time())}")
print(model)
