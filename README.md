# Obtaining GCP Credentials for Storage

See https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python for more details.  Creedentials should not be stored 

To obtain a new key/credential files, go the the quickstart service account (listed under service accounts) and download.  You might need to create a new key.


# Creating the DOCKER image
```
docker build -t moshh-api/1.0.0 .
```

# Running the DOCKER image
```
docker run -p 5001:80 --name="moshh-api-1.0.0" moshh-api/1.0.0
```

# View all containers 
```
docker ps -a
```

# Remove container
get the container id with 
```
docker ps -a
```
```
docker rm <container_id>
```

# Pushing to google cloud Container Registry
* Tag the local image with a name that fits the GCP container registry format:

    ```
    docker tag SOURCE_IMAGE gcr.io/PROJECT_ID/TAG_NAME
    ```

    Example:

    ```
    docker tag moshh-api/1.0.0 gcr.io/moshh-338102/moshh-api/1.0.0
    ```

* Push the image:
    
    Note I discovered I had to be set as my user credential rather than logged in as a service account.  for some reason I couldn't get it to work when gcloud was set to the service account credentials
    ```
    docker push gcr.io/moshh-338102/moshh-api/1.0.0
    ```