import json

new_data = """
{
   "Status": "Healthy",
   "Checks": [
    {
        "Name": "Connections",
        "Status": "Healthy"
        },
        {
            "Name": "ConnectionRead",
            "Status": "unHealthy"
            },
            {
            "Name": "redis",
            "Status": "Healthy"
            },
            {
            "Name": "ProcessCheck",
            "Status": "Healthy"
            },
            {
                "Name": "UserProfile",
                "Status": "unHealthy"
            },
            {
                "Name": "features",
                "Status": "unHealthy",
                "Description": "sample sample sample"
            },
            {
                "Name": "shutdown",
                "Status": "Healthy"
            },
            {
                "Name": "lifespan",
                "Status": "unHealthy"
        }
    ]
}
"""

# Deserialization, converting JSON back to a dictionary
data = json.loads(new_data) 


# make a function that will output the number of healthy and unhealthy checks - count how many there are
def health_check(data):

    checks = data["Checks"]
    healthy_count = 0 # Begin count of healthy checks at 0
    unhealthy_count = 0 # Begin count of unHealthy checks at 0
    unhealthy_names = [] # create a list to store the names of unhealthy checks

    for check in checks:
        if check["Status"] == "Healthy":
            healthy_count += 1
        else:
            unhealthy_count += 1
            unhealthy_names.append(check["Name"]) # append the name of the unhealthy check

    print(f"You have {healthy_count} Healthy checks")
    print(f"You have {unhealthy_count} Unhealthy checks")
    if unhealthy_names:
        print("Unhealthy check names:")
        for name in unhealthy_names:
            print(name)

# Call the health_check function
health_check(data)