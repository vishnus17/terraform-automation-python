# Terraform Deployment Python Script

Simple Python script to automate your terraform deployment. 

Python's subprocess module is used to run Terraform commands directly.

### Steps to implement

1. Change the value of `terraform_dir` to the corresponding directory path.
2. Initialize and plan your Terraform script by running `py terraform.py`
3. Once you validate the plan, uncomment `apply_terraform()` and run `py terraform.py` to deploy your resources.
4. Uncomment `destroy_terraform()` to delete your resources.
