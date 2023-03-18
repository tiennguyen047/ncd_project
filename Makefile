# This Makefile will run common task for kotllin
# make : build docker images

SCRIPT_DIR = build

# Build docker images, always the FIRST target in this Makefile
build: info
	@bash $(SCRIPT_DIR)/create_ncd_images.sh

# Project info
info:
	@echo "make file for build project"

# For deplyment ncd service
deploy: info
	@bash $(SCRIPT_DIR)/prepare_deployment_script.sh

# For test unit test, function test, system test
test: info
	@echo "For test project unit test, function test, system test"