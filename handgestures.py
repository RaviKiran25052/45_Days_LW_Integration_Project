import cv2
import os
import time
import uuid
from cvzone.HandTrackingModule import HandDetector
import text_to_speech as ts
import speechregonition as sr
import boto3

def ec2():
    os.system("aws ec2 run-instances --image-id ami-057752b3f1d6c4d6c --instance-type t2.micro")
    os.system("start msedge https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Instances:")
    time.sleep(3)
def s3(UUID):
    x = str(UUID)
    os.system(f"aws s3 mb s3://mybucket123{x} --region ap-south-1")
    os.system("start msedge https://s3.console.aws.amazon.com/s3/home?region=ap-south-1")
    time.sleep(3)

ec2_client = boto3.client('ec2', 'ap-south-1')
ebs_volume = boto3.resource('ec2')

def ec2_ebs(ami,name):
    
    images = {
        'amazon':'ami-0d13e3e640877b0b9',
        'redhat':'ami-05c8ca4485f8b138a',
        'ubuntu':'ami-0f5ee92e2d63afc18',
        'centos':'ami-0763cf792771fe1bd'
    }
    instance_type = 't2.micro'
    image_id = images[ami]
    key_name = "my_os_key"
    instance_name = name

    response = ec2_client.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        KeyName=key_name,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    },
                ]
            },
        ]
    )
    instance_id = response['Instances'][0]['InstanceId']
    availability_zone = response['Instances'][0]['Placement']['AvailabilityZone']
    return instance_id,instance_name,availability_zone

def isRunning(instance):
    while True:
        instance.reload()
        if instance.state['Name'] == 'running':
            ts.say("Instance is now running.")
            break
        ts.say("Waiting for the instance to be running...")
        time.sleep(7)

def ebs():
    ts.say("Which instance do you want to create?")
    ami = sr.myspeechrecognition(2)
    ts.say("By what name you want to launch your instance?")
    name = sr.myspeechrecognition(2)
    instance_id,instance_name,az = ec2_ebs(ami,name)
    
    volume = ebs_volume.create_volume(
        AvailabilityZone = az,
        Size = 5,
        VolumeType='gp2'
    )
    instance = ebs_volume.Instance(instance_id)
    
    isRunning(instance)
    
    response = instance.attach_volume(
        VolumeId = volume.id,
        Device='/dev/xvdf'
    )
    ts.say("Volume created and attached sucessfully!")
    os.system("start msedge https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Instances:")
    
    
def notification():
    ts.say("Sending Notifications in 3.. 2... 1...")
    os.system("start msedge https://r85e5zdyid.execute-api.ap-south-1.amazonaws.com/emaill/email")
    time.sleep(3)


def hand():
    Handmodel = HandDetector(maxHands=1)
    cap = cv2.VideoCapture(0)
    while True:
        UUID  = uuid.uuid1().int
        status, photo = cap.read()
        hand,image = Handmodel.findHands(photo)
        cv2.imshow("myphoto", image)
        if hand:
            fingers = Handmodel.fingersUp(hand[0])
            if fingers == [1,0,0,0,0]:
                ebs()
            if fingers == [0,1,1,1,0]:
                s3(UUID)
            if fingers == [0,1,1,0,0]:
                ec2()
            if fingers == [0,1,1,1,1]:
                notification()
            if fingers == [0,0,0,0,1]:
                break
        if cv2.waitKey(1) == 13:
            break
    cv2.destroyAllWindows()
    cap.release()