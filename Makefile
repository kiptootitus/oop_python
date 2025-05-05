# Makefile

# Default file to run
FILE=02_variables.py

# Run the Python script
run:
	python3 $(FILE)

# Clean up any compiled Python files (optional)
clean:
	find . -name '*.pyc' -delete
