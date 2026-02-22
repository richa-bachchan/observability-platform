terraform {
  backend "s3" {
    bucket         = "my-observability-tfstate-1234567"
    key            = "observability/terraform.tfstate"
    region         = "eu-west-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
