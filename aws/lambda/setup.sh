#!/bin/bash

# Create lambda function

if (( $# < 2 ))
then
	echo "SYNTAX: $0 <awsaccno> <rolename>"
	exit 1
fi

zip -9r showvms.zip . --exclude setup.sh
ACCOUNTNO=$1
ROLENAME=$2

aws lambda create-function --function-name staticsteve --runtime python3.7 --role arn:aws:iam::$ACCOUNTNO:role/service-role/$ROLENAME --handler showvms.starthere --description "Hello world" --zip-file fileb://showvms.zip
