update_env:
	@echo "Updating the 'mercury_level_estimation_python' Conda environment from environment.yml..."
	conda env update --name mercury_level_estimation_python --file environment.yml
	@echo "Please activate the Conda environment with the following command: conda activate mercury_level_estimation_python"
