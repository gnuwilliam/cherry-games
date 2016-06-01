# define colors
GREEN   := $(shell tput -Txterm setaf 2)
WHITE   := $(shell tput -Txterm setaf 7)
RESET   := $(shell tput -Txterm sgr0)

.PHONY: help

help:
	@echo '${GREEN}Usage:${RESET}'
	@echo '  make <target>'
	@echo
	@echo '${GREEN}Targets:${RESET}'
	@echo '  ${WHITE}clean${RESET}  clean cache files'
	@echo '  ${WHITE}test${RESET}   run all tests'
	@echo '  ${WHITE}run${RESET}    run the app'

clean:
	clear
	@echo '${GREEN}Cleaning files...${RESET}'
	@rm -rf tests/__pycache__
	@rm -rf tests/api/__pycache__
	@find . -name '*.pyc' -delete
	@echo '${GREEN}done!${RESET}'

test:
	clear
	@echo '${GREEN}Running tests...${RESET}'
	@py.test -p no:sugar

run:
	clear
	@echo '${GREEN}Running app...${RESET}'
	@python main.py
