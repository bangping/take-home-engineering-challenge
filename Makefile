.PHONY: dependency update_csv test clean

dependency:
	pip3 install -r requirements.txt

update_csv:
	curl -O https://data.sfgov.org/api/views/rqzj-sfat/rows.csv && \
	mv external/Mobile_Food_Facility_Permit.csv external/Mobile_Food_Facility_Permit.csv.bak && \
	mv rows.csv external/Mobile_Food_Facility_Permit.csv

test:
	pip3 install -r requirements.testing.txt
	pytest

clean:
	rm -rf script/__pycache__ tests/__pycache__
	rm -rf .pytest_cache tests/.pytest_cache
