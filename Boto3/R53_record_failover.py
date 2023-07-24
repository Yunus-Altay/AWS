#!/usr/bin/python

import boto3

def find_ip(id):
    ec2 = boto3.resource("ec2")
    instance = ec2.Instance(id)
    ip = instance.public_ip_address
    return ip
# Returns a public IP address based on instance ID
          
print("Input the instance ID:")
instance_id = input()
ip_address = find_ip(instance_id)

print("Input the domain name:")
domain = input()

print("Input the hosted zone ID:")
zone_id = input()

# Defines a function that creates a new A record set using the provided information 
def change_route53_record(zone_id, domain, ip):
    """
    Changes Route53 type A record
    """
    r53 = boto3.client("route53")
    response = r53.change_resource_record_sets(
            ChangeBatch={
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': domain,
                        'ResourceRecords': [
                            {
                                'Value': ip,
                            },
                        ],
                        'TTL': 60,
                        'Type': 'A',
                    },
                },
            ],
            'Comment': 'Web server for example.com',
        },
        HostedZoneId=zone_id,
    )

    print("New record type " + domain + " has been created")

change_route53_record(zone_id, domain, ip_address)