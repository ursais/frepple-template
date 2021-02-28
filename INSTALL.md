# Installation of FrePPLe

## Table of Contents
* [Requirements](#Requirements)
* [Dev environment](#Dev-environment)
  * [On Github](#On-Github)
* [Test environment](#Test-environment)
* [QA environment](#QA-environment)
* [Production environment](#Production-environment)


## Requirements

Create a new repository `frepple-project` on Github or Gitlab

Clone this repository and push it to `frepple-project`

## Dev environment

Create the project:
```shell script
oc new-project frepple-project-dev --display-name="FrePPLe Project Dev"
```
Add permissions to the default Service Account of the project:
```shell script
oc adm policy add-scc-to-user anyuid -z default
oc adm policy add-scc-to-user privileged -z default
```
Edit the variables in helm/frepple/values.yaml

Run
```shell script
helm dependency update helm/frepple
helm install frepple helm/frepple
```
Go to the Build Config `frepple` on the OpenShift Console

Click on `Copy URL with Secret`.

### On Github

Go to the repository, then Settings > Webhooks > Add webhook.

Paste the URL into `Payload URL`.

Change the `Content Type` to `application/json`.

Click `Add webhook`.

## Test environment

Create the project:
```shell script
oc new-project frepple-project-test --display-name="FrePPLe Project Test"
```
Add permissions to the default Service Account of the project:
```shell script
oc adm policy add-scc-to-user anyuid -z default
oc adm policy add-scc-to-user privileged -z default
oc policy add-role-to-user \
    system:image-puller system:serviceaccount:frepple-project-test:default \
    --namespace=frepple-project-dev
```
Edit the variables in helm/frepple/values.test.yaml

Run
```shell script
helm install frepple -f helm/frepple/values.test.yaml helm/frepple
```

## QA environment

Create the project:
```shell script
oc new-project frepple-project-qa --display-name="FrePPLe Project QA"
```
Add permissions to the default Service Account of the project:
```shell script
oc adm policy add-scc-to-user anyuid -z default
oc adm policy add-scc-to-user privileged -z default
oc policy add-role-to-user \
    system:image-puller system:serviceaccount:frepple-project-qa:default \
    --namespace=frepple-project-dev
```
Edit the variables in helm/frepple/values.qa.yaml

Run
```shell script
helm install frepple -f helm/frepple/values.qa.yaml helm/frepple
```

## Production environment

Create the project:
```shell script
oc new-project frepple-project --display-name="FrePPLe Project Production"
```
Add permissions to the default Service Account of the project:
```shell script
oc adm policy add-scc-to-user anyuid -z default
oc adm policy add-scc-to-user privileged -z default
oc policy add-role-to-user \
    system:image-puller system:serviceaccount:frepple-project:default \
    --namespace=frepple-project-dev
```
Edit the variables in helm/frepple/values.production.yaml

Run
```shell script
helm install frepple -f helm/frepple/values.production.yaml helm/frepple
```
