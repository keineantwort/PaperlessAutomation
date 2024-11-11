# PaperlessAccess
This is the main module with helper objects to access Paperless.

## Usage
```
paperless = PaperlessAccess("cred.yaml").paperless()
docs = paperless.documents.all()
```

## Configuration
```
url: "<YOUR PAPERLESS URL>"
api_token: "<YOUR TOKEN>"
```