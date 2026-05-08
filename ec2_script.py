import boto3
import sys

# Create EC2 client
ec2 = boto3.client('ec2')

# Replace with your instance ID
INSTANCE_ID = "i-0f76f24b9221d4754"

if len(sys.argv) < 2:
    print("Usage: python ec2_script.py start|stop|delete")
    exit()

action = sys.argv[1]

if action == "start":
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print("✅ Instance started")

elif action == "stop":
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print("✅ Instance stopped")

elif action == "delete":
    ec2.terminate_instances(InstanceIds=[INSTANCE_ID])
    print("✅ Instance terminated")

else:
    print("❌ Invalid input")
