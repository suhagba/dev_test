# Part 6: Cloud computing

This sections tests some general cloud computing knowledge to do with AWS and cloud infra in general.
It is expected that you will need to find the answers to some of these questions via Google.

Please write your answers in this file.

### Question 6.1

Which AWS region is the closest to Melbourne?

```
Answer

Asia Pacific (Sydney) Region

```

### Question 6.2

What is the name of a cheap AWS EC2 instance that offers _at least_ 12 CPU cores and 16GB of RAM?
What are its specs (CPU cores, RAM) and cost per hour?

```
Answer

a1.4xlarge is the cheapest on demand option.
it offers 16 vCPU, 32 GB RAM and has EBS only instance storage and costs $0.408 per hour

```


How much will it cost to run this instance for two weeks?

```
Answer

1 instances x 0.408 USD x 336 hours  = $137.08800

some additional cost such as intra region data transfer, EBS storage and snapshot storage cost might be incured 
```

### Question 6.3

Provide the AWS CLI command to copy all the contents of a S3 bucket to another S3 bucket on the same account.
The source bucket may contain nested files within "folders".

Source bucket: s3://mysource
Destination bucket: s3://mydest

### Answer

we can use sync which will recursively copy 
```bash
aws s3 sync s3://mysource s3://mydest
```

### Question 6.4

Link to a section of library documentation showing how to stop an AWS EC2 instance using a Python client library (can be a howto, API reference, or tutorial).

### Answer

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html

### Question 6.5

Describe, in 1-3 sentences

- What an AMI is and why it is useful for running EC2 instances
```

An Amazon Machine Image (AMI) is a template that contains a software configuration (for example, an operating system, an application server, and applications). From an AMI, you launch an instance, which is a copy of the AMI running as a virtual server in the cloud. You can launch multiple instances of an AMI, as shown in the following figure.

```

- What IAM is and why it is useful when administering AWS

```

AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

IAM is a feature of your AWS account offered at no additional charge. You will be charged only for use of other AWS services by your users.


```

- Where you would add your SSH public key onto an EC2 instance in order to log in as the "ubuntu" user

```
 typically the ssh public key will be stored in the

  /root/.ssh/authorized_keys folder on the ec2 instance.


```

### Question 6.6

Create a new SSH key and paste both the public and private key into this file.

public key
```
---- BEGIN SSH2 PUBLIC KEY ----
Comment: "rsa-key-20210315"
AAAAB3NzaC1yc2EAAAABJQAAAQEAhrqdR3IYrlubh5sQcxFHAVFl1w3NOHTD2tIw
bOK4BHrAyHIBeItvZQJtd/213s1o0y0WOctP+8CPKjlhHpSxwuiZlw5ccoSMt5BI
hk0m4qlyTc54wKfxP8wLs6hJ416dmJk4iMzLRTBPTgeVELxOWKhBbK92+NM7/Fvq
j+jdqQr2WlEveHFjovo37Wwncyxgsp+J7Nqd5XRFtzdtjfSrXY9a+GiIkayHOaTk
Zs++9hjzk2alZ59pXQvYj8lai0cXMl2Y/mL3+v2xOK7U3vrG2+daydsiCE5z5dCb
cmYR+hyciHHr3pc2szUvNOMPx15B2FzjUzFvRgUTheTycybIyw==
---- END SSH2 PUBLIC KEY ----

```

private key

```
PuTTY-User-Key-File-2: ssh-rsa
Encryption: none
Comment: rsa-key-20210315
Public-Lines: 6
AAAAB3NzaC1yc2EAAAABJQAAAQEAhrqdR3IYrlubh5sQcxFHAVFl1w3NOHTD2tIw
bOK4BHrAyHIBeItvZQJtd/213s1o0y0WOctP+8CPKjlhHpSxwuiZlw5ccoSMt5BI
hk0m4qlyTc54wKfxP8wLs6hJ416dmJk4iMzLRTBPTgeVELxOWKhBbK92+NM7/Fvq
j+jdqQr2WlEveHFjovo37Wwncyxgsp+J7Nqd5XRFtzdtjfSrXY9a+GiIkayHOaTk
Zs++9hjzk2alZ59pXQvYj8lai0cXMl2Y/mL3+v2xOK7U3vrG2+daydsiCE5z5dCb
cmYR+hyciHHr3pc2szUvNOMPx15B2FzjUzFvRgUTheTycybIyw==
Private-Lines: 14
AAABAGX1AWZ/21ODmErx4u9LWFQGPzr1sA8MQS/5Ag018wpPDm4swtfDduSn5CNz
45PZtxxZeJpwWDQjBI6n9ngB0qFWE12OU8xIodcFZ1DgcHQtM+fahOTSHlnK2GxI
AJBjRtRYRnVctYB3lfXcOXRy04Fcu+OLs/qSA+GRqpZrCJuYcDR8gGFg90X8nFzc
uu4ntjj5b5QdMhT8+2ILwon/ormhHhADBwbLL/w+YvNYFYBd7JSGDoIxcehw1xFV
zLgLRHEXjHVEDHm8CI9lwcL7QYRe9dqZXK3BDWzLtiEeOg6Z089Pbth5NSO/wlLg
naiKbx5KOT9mzOcIR6tooWx2R60AAACBAP/XFdR59exM1uj/mqzZa0LsaCNCjTGK
00GqIxEQClQI1O0b3sJ9BIFIxeANbbj5xtedx3CVe4TqFPSOPBFbWk5JdY7NDrjA
SxHQ9rcjT71oH6c2VwA9YMwDGDgoYV0hxsTaQFPZpMZt8s95lJUxXFlR6iTv2MSn
M9TlyKlQ5WlLAAAAgQCG0CkfEBbC3joSl63Munpasck3yybX43dKJvKJIv0butxh
kIXF8EAY0UNvTq2gbh8jVe4PXPTXEhijPO4xhd3lU3ai34N34vomYRY5HpXglyWl
jhTnUwn6t4agVRzDji8kXD98ZuSOnymMqTfzZQHVsLU74dn3SPQEfZsqrlvugQAA
AIEAw3AkGD95laA4sQ0OTzVhzonkofxOHQKYbUQ3u1F9vpUpXouDceo3vSKZ/p3s
uednSWRsT6Jw67gf7Qy2TEWU0bwf9OUB4VQ/oTKKfPNUMew9RGE38M3y7kLxeYTy
yRkyVOw0e2SgXcBQiQFyGKKQYbYJ/6AWzoarWGkFYZIOCpg=
Private-MAC: 37c0148841336854c6ec6ab0bf804e281a615e04

```

### Question 6.7

Write a bash one liner to create a new file called `foo.txt` which contains the text "Hello World!", followed by a newline

```bash
echo "Hello World!\n" >> foo.txt
```

### Question 6.8

Write a bash one liner to create a new file which contains the text "Hello World!", followed by a newline, on a remote machine via SSH.

Remote machine hostname is `foo.com` and the user is `bar`. Assume you have all your SSH keys set up correctly on your machine and the target server.

```bash
ssh bar@foo.com "echo 'Hello World!\n' >> foo.txt"
```

### Question 6.9

Buildkite it a self-hosted CI system. Referring to the documentation via Google, is it possible to run a scheduled build at 2pm every Tuesday? Please link to the URL of the documentation where you found your answer.


```

yes you can have a schedule build at 2pm every tuesday using buildkite 

here is the refer to the documenation 
https://buildkite.com/docs/pipelines/scheduled-builds#main

```
### Question 6.10

GitHub Actions is a CI system provided by GitHub, Referring to the documentation via Google, what is an environment variable that you could use to determine whether your bash script is running inside a Github Action?

What kind of value would indicate that your script is running inside a GitHub Action?

```
GITHUB_ACTIONS is the environment variable that can be set to TRUE for running the bash scripts on github actions.

 You can use this variable to differentiate when tests are being run locally or by GitHub Actions.

 
```
