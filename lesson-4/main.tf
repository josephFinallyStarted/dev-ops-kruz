provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "web" {
  ami           = "ami-09191d47657c9691a"
  instance_type = "t3.micro"

  tags = {
    Name = "HelloWorld"
    Environment = "dev"
  }
}

variable "test" {

}