4. Using Python and boto3, update the IAM password policy on an account. The script should have a command line argument that contains a JSON object with the KWARGS needed for the password policy.


import boto3
import json
import sys

# Opening JSON file
f = open(sys.argv[1], 'r')
# returns JSON object as a dictionary
data = json.load(f)
iam = boto3.client('iam')

# Function to update password policy based on the json file as command line argument.

def update_password_policy():
    print(data["HardExpiry"])
    print("------------------")
    response = iam.update_account_password_policy(
        MinimumPasswordLength=data["MinimumPasswordLength"],
        RequireSymbols=data["RequireSymbols"],
        RequireNumbers=data["RequireNumbers"],
        RequireUppercaseCharacters=data["RequireUppercaseCharacters"],
        RequireLowercaseCharacters=data["RequireUppercaseCharacters"],
        AllowUsersToChangePassword=data["AllowUsersToChangePassword"],
        MaxPasswordAge=data["MaxPasswordAge"],
        PasswordReusePrevention=data["PasswordReusePrevention"],
        HardExpiry=data["HardExpiry"]
    )
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print("Successfully updated Password Policy : ")
    else:
        print("Something went wrong for updating password policy : ")
        print("Status code :" + str(response["ResponseMetadata"]["HTTPStatusCode"]))


# Closing file
f.close()

update_password_policy()
