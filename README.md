# integrating-aws-with-the-sdk
Integrating AWS with the SDK

## Configure a new profile

```bash
aws configure --profile Developer
AWS Access Key ID [None]: AKIA################
AWS Secret Access Key [None]: ######################################/#
Default region name [None]: us-west-2
Default output format [None]: json
```

## Verify the details of your profile
```bash
 aws sts get-caller-identity --profile Developer
{
    "UserId": "##################",
    "Account": "############",
    "Arn": "arn:aws:iam::############:user/UserName"
}
```