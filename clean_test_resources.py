from anylearn.config import AnylearnConfig, init_sdk
from anylearn.interfaces import Project
from anylearn.interfaces.resource import Algorithm, Dataset, Model

TARGET = ["SDK_QUICKSTART", "SDK_QUICK_TRAINING"]

init_sdk("http://192.168.10.22:31888", "xlearn", "123456")

algos = Algorithm.get_list()
dsets = Dataset.get_list()
models = Model.get_list()
projects = Project.get_list()

for objs in [algos, dsets, models, projects]:
    [o.delete() for o in objs if o.description in TARGET]

AnylearnConfig.clear_workspace()
