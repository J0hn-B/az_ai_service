export SUBSCRIPTION_KEY := $(shell terraform -chdir=azure/local_files_tf output -raw subscription_key)
export ENDPOINT := $(shell terraform -chdir=azure/local_files_tf output -raw endpoint)


#? Validate and deploy AI service
.PHONY: dbug
dbug:
	python3 -m pdb  app/local_files/main.py

.PHONY: test
test:
	python3 -m pytest -r app/tests 

.PHONY: deploy
deploy:
	python3 app/local_files/main.py
	python3 -m pytest -r app/tests

.PHONY: apply
apply:
	terraform -chdir=azure/local_files_tf init
	terraform -chdir=azure/local_files_tf fmt
	terraform -chdir=azure/local_files_tf validate
	terraform -chdir=azure/local_files_tf apply --auto-approve

.PHONY: destroy
destroy:
	terraform -chdir=azure/local_files_tf destroy --auto-approve