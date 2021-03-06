# Telestream Cloud Timed Text Speech Python SDK

This library provides a low-level interface to the REST API of Telestream Cloud, the online video encoding service.

## Requirements.

Python 2.7 and 3.4+

## Getting Started
### Initialize client

```python
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint

configuration = telestream_cloud_tts.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
api_instance = telestream_cloud_tts.TtsApi(telestream_cloud_tts.ApiClient(configuration))
project_id = 'project_id_example'
```

### Create a new project

```python
project = api_instance.create_project(telestream_cloud_tts.Project(name = "Example project name"))
```

### Create a job from source URL
```
job = api_instance.create_job(project_id, telestream_cloud_tts.Job("http://url/to/file.mp4"))
pprint(job)
```

### Create a job from file
```
upload = telestream_cloud_tts.Uploader(project_id, api_instance, "/path/to/file.mp4", "", {})
upload.setup()
job_id = upload.start()
print(job_id)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloud.telestream.net/tts/v1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TtsApi* | [**create_corpus**](docs/TtsApi.md#create_corpus) | **POST** /projects/{projectID}/corpora/{name} | Creates a new Corpus
*TtsApi* | [**create_job**](docs/TtsApi.md#create_job) | **POST** /projects/{projectID}/jobs | Creates a new Job
*TtsApi* | [**create_project**](docs/TtsApi.md#create_project) | **POST** /projects | Creates a new Project
*TtsApi* | [**delete_corpus**](docs/TtsApi.md#delete_corpus) | **DELETE** /projects/{projectID}/corpora/{name} | Creates a new Corpus
*TtsApi* | [**delete_job**](docs/TtsApi.md#delete_job) | **DELETE** /projects/{projectID}/jobs/{jobID} | Deletes the Job
*TtsApi* | [**delete_project**](docs/TtsApi.md#delete_project) | **DELETE** /projects/{projectID} | Deletes the Project
*TtsApi* | [**get_job**](docs/TtsApi.md#get_job) | **GET** /projects/{projectID}/jobs/{jobID} | Returns the Job
*TtsApi* | [**get_project**](docs/TtsApi.md#get_project) | **GET** /projects/{projectID} | Returns the Project
*TtsApi* | [**getget_corpus**](docs/TtsApi.md#getget_corpus) | **GET** /projects/{projectID}/corpora/{name} | Returns the Corpus
*TtsApi* | [**job_outputs**](docs/TtsApi.md#job_outputs) | **GET** /projects/{projectID}/jobs/{jobID}/outputs | Returns the Job Outputs
*TtsApi* | [**job_result**](docs/TtsApi.md#job_result) | **GET** /projects/{projectID}/jobs/{jobID}/result | Returns the Job Result
*TtsApi* | [**list_corpora**](docs/TtsApi.md#list_corpora) | **GET** /projects/{projectID}/corpora | Returns a collection of Corpora
*TtsApi* | [**list_jobs**](docs/TtsApi.md#list_jobs) | **GET** /projects/{projectID}/jobs | Returns a collection of Jobs
*TtsApi* | [**list_projects**](docs/TtsApi.md#list_projects) | **GET** /projects | Returns a collection of Projects
*TtsApi* | [**train_project**](docs/TtsApi.md#train_project) | **POST** /projects/{projectID}/train | Queues training
*TtsApi* | [**update_project**](docs/TtsApi.md#update_project) | **PUT** /projects/{projectID} | Updates an existing Project


## Documentation For Models

 - [CorporaCollection](docs/CorporaCollection.md)
 - [Corpus](docs/Corpus.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Fragment](docs/Fragment.md)
 - [FragmentVariant](docs/FragmentVariant.md)
 - [Job](docs/Job.md)
 - [JobOutput](docs/JobOutput.md)
 - [JobResult](docs/JobResult.md)
 - [JobsCollection](docs/JobsCollection.md)
 - [Project](docs/Project.md)
 - [ProjectsCollection](docs/ProjectsCollection.md)
 - [Result](docs/Result.md)


## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header


## Author

cloudsupport@telestream.net


