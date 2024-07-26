provider "aws" {
  region = "ap-south-1"
}
resource "aws_s3_buc" "my_bucket" {
  bucket = "s3-test-terraform"
}
