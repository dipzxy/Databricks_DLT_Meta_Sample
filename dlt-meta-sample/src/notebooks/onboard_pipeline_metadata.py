# Databricks notebook source
# MAGIC %pip install dlt-meta

# COMMAND ----------

onboarding_params_map = {
	"database": "dev_catalog.default",
	"onboarding_file_path": "/Volumes/dev_catalog/default/my-test-volume/config/Product_onboarding.json",
	"bronze_dataflowspec_table": "bronze_dataflowspec_table", 
 	"silver_dataflowspec_table": "silver_dataflowspec_table", 
	"overwrite": "True",
	"env": "dev",
	"version": "v1",
	"import_author": "Dipto B."
}

from src.onboard_dataflowspec import OnboardDataflowspec
OnboardDataflowspec(spark, onboarding_params_map, uc_enabled=True).onboard_dataflow_specs()
