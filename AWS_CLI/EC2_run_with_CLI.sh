#!/bin/bash
# set -x
export AWS_PROFILE=Simaox

read -p "Enter region: " region
read -p "Enter instance type: " instancetype
read -p "Enter pem file name: " pem
read -p "Enter a tag-value: " tag

# retrieves the latest linux 2023 AMI ID from AWS Systems Manager (SSM)
ami=$(aws ssm get-parameters --names "//aws\service\ami-amazon-linux-latest\al2023-ami-kernel-default-x86_64" --region us-east-1 --query "Parameters[0].Value" --output text) 

# ami=ami-06ca3ca175f37dd66
# secgrpid=sg-02c4a792c0262ad1a

aws ec2 run-instances --image-id $ami --count 1 --instance-type $instancetype --key-name $pem --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$tag}]" > /dev/null

# read -p "Enter security group id: " secgrpid
# read -p "Enter subnet id: " subnetid

# --subnet-id $subnetid

# aws ec2 create-tags --resources i-5203422c --tags Key=Name,Value=MyInstance

echo "$(aws ec2 describe-instances --filters "Name=tag-value,Values=$tag" "Name=instance-state-name,Values=pending" --query "Reservations[].Instances[].InstanceId" --output text) will be ready in minutes."

sleep 2
echo "Here is the public ip address: $(aws ec2 describe-instances --filters "Name=tag-value,Values=$tag" --query Reservations[].Instances[].NetworkInterfaces[].Association[].PublicIp --output text)"

# aws ec2 wait instance-status-ok --instance-ids $id

# # aws ec2 terminate-instances --instance-ids $id

# aws ec2 describe-instances --query "Reservations[*].Instances[*].PublicIpAddress" --output text

# ssh -i $pem ec2-user@publicip

# sed -i -e 's/\r$//' create-ec2.sh
