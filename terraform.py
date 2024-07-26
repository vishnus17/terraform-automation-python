import os
import subprocess

# Change the working directory to the Terraform configuration directory
terraform_dir = os.path.join(os.path.dirname(__file__), '/path/to/terraform/files')

def init_terraform():
    print("Initializing Terraform")
    out = subprocess.run(['terraform', 'init'], cwd=terraform_dir)
    if out.returncode == 0:
        print("Terraform init succeeded")
    else:
        print("Terraform init failed")
        

def plan_terraform():
    print("Planning Terraform")
    out = subprocess.run(['terraform', 'plan', '-out=plan.out'], cwd=terraform_dir)
    if out.returncode == 0:
        print("Terraform plan succeeded")
    else:
        print("Terraform plan failed")

def apply_terraform():
    print("Applying Terraform")
    out = subprocess.run(['terraform', 'apply', 'plan.out'], cwd=terraform_dir)
    if out.returncode == 0:
        print("Terraform apply succeeded")
    else:
        print("Terraform apply failed")

def destroy_terraform():
    print("Destroying Terraform")
    out = subprocess.run(['terraform', 'destroy', '-auto-approve'], cwd=terraform_dir)
    if out.returncode == 0:
        print("Terraform destroy succeeded")
    else:
        print("Terraform destroy failed")

def main():
    init_terraform()
    plan_terraform()
    # apply_terraform()
    # destroy_terraform()

if __name__ == "__main__":
    main()