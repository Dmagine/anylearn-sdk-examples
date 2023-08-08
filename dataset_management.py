from anylearn.config import init_sdk, print_config
from anylearn.interfaces.resource import Dataset, Resource

init_sdk('http://x-y.z:1234', 'foo', 'bar')

# Create a dataset record
print("****** Create a dataset ******")
new_dataset = Dataset(name="test_dset_sdk", description="test",
                      filename="testdset.csv",
                      public=False)
new_dataset.save()
new_dataset.get_detail()
print(new_dataset)
print("------\n")

# Upload the dataset file
print("****** Upload dataset file ******")
Resource.upload_file(resource_id=new_dataset.id,
                     file_path="examples/testdset.csv")
# Wait till file ready in backend
while not new_dataset.file_path:
    new_dataset.get_detail()
print("File uploaded successfully")
print("------\n")

# Retrieve all datasets
print("****** Get all datasets ******")
datasets = Dataset.get_list()
for i, d in enumerate(datasets):
    print(f"{i} => {repr(d)}")
print("------\n")

# Find out the recently created dataset
print("****** Get my dataset from list ******")
my_dataset = next(d for d in datasets if d.name == "test_dset_sdk")
print(my_dataset)
print("------\n")

# Check the uploaded file
print("****** Get file structure ******")
print(Resource.list_dir(resource_id=my_dataset.id))
print("------\n")

# Upload description and visibility
print("****** Update my dataset ******")
my_dataset.description = "Sample dataset created with SDK"
my_dataset.public = True
result = my_dataset.save()
print(f"Updated ? {'yes' if result else 'no'}")
# Refresh detail info
my_dataset.get_detail()
print(my_dataset)
print("------\n")

# Delete my dataset
print("****** Delete my dataset ******")
my_dataset.delete()
print(f"Deleted ? {'yes' if result else 'no'}")
print("------\n")
