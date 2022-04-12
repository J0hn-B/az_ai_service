# ai_service

Generate and record local images description using Azure Computer Vision service.

## Requirements

Azure Subscription, bash, python, terraform

## How to

```bash
git clone https://github.com/J0hn-B/ai_service_azure.git
```

```bash
cd ~/ai_service_azure
```

## Usage

```bash
# Configure an azure ai service using terraform
make apply

# Call the API and record the results in the archive file
make deploy

# Test functions with pytest
make test

# Clean up
make destroy
```

## Description

Add your images inside `app/photos` dir.

![image](https://user-images.githubusercontent.com/40946247/143480995-9b651564-0b2a-41fc-a798-ce5b97471b91.png)

From `~/ai_service_azure`:

`make apply`

![image](https://user-images.githubusercontent.com/40946247/143474091-b3c7f3b3-043c-410c-ac4e-2ce9be78018e.png)

`make deploy`

![image](https://user-images.githubusercontent.com/40946247/143476348-b6c0ad86-b72c-439e-b965-fed372cc7033.png)

**Check the `analysis-archive` dir**

![image](https://user-images.githubusercontent.com/40946247/143477339-256c2e09-156a-499b-bc70-a215b0d6fad6.png)
