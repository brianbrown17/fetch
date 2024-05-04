from google.cloud import secretmanager

# Initialize the Secret Manager client
client = secretmanager.SecretManagerServiceClient()

# Specify the name of your secret
secret_name = "projects/824544385686/secrets/google_maps_api_key"

# Access the secret
response = client.access_secret_version(request={"name": secret_name})
secret_value = response.payload.data.decode("UTF-8")

# Use the secret value in your application
print("Secret Value:", secret_value)