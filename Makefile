export DAGSTER_HOME=${PWD}/.dagster
export DBT_PROFILES_DIR=${PWD}/imdb_dbt

dagster:
	@dagster-daemon run
dagit:
	@dagit
dbt_deps:
	@cd imdb_dbt && dbt deps
dbt_doc_gen: dbt_deps
	@cd imdb_dbt && dbt docs generate
dbt_doc_serve: dbt_doc_gen
	@cd imdb_dbt && dbt docs serve
