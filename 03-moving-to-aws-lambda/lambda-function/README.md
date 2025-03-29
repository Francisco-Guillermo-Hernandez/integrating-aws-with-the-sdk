
## Install packages

```bash 
pip install -r requirements.txt --target ./package 
```

## Zip up the Lambda function
```bash
cd .. ; zip ~/lambda-function.zip lambda_function.py
````


## Creates a Lambda Function using a zip file

```bash
 aws lambda create-function \
 --function-name grid-maker \
 --runtime python3.9 \
 --timeout 30 \
 --handler lambda_function.lambda_handler \
 --role $LAMBDA_ROLE \
 --zip-file fileb://~/path-to/lambda-function.zip
````

## Update the Lambda function  
```bash
aws lambda update-function \
--function-name grid-maker \
--runtime python3.9 \
--timeout 30 \
--handler lambda_function.lambda_handler \
--role $LAMBDA_ROLE \
--zip-file fileb://~/path-to/lambda-function.zip
```