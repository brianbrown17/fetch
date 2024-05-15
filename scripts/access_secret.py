from google.cloud import secretmanager

def access_secret(project_id, secret_id, version):
    """
    Access a secret- API token, etc- stored in Secret Manager
    """
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version
    name = client.secret_version_path(
        project=project_id, 
        secret=secret_id, 
        secret_version=version
    )

    # Access the secret version
    response = client.access_secret_version(name=name).payload.data.decode("utf-8")

    return response
