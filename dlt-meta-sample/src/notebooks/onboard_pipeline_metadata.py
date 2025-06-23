# Databricks notebook source
# MAGIC %pip install dlt-meta

# COMMAND ----------

onboarding_params_map = {
	"database": "dlt_meta.default",
	"onboarding_file_path": "abfss://config@<storage account name>.dfs.core.windows.net/Product_onboarding.json",
	"bronze_dataflowspec_table": "bronze_dataflowspec_table", 
 	"silver_dataflowspec_table": "silver_dataflowspec_table", 
	"overwrite": "True",
	"env": "dev",
	"version": "v1",
	"import_author": "Matias S."
}

from src.onboard_dataflowspec import OnboardDataflowspec
OnboardDataflowspec(spark, onboarding_params_map, uc_enabled=True).onboard_dataflow_specs()
