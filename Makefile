# Makefile

SHELL := /bin/bash
TAG := $(shell git describe --tags --abbrev=0)
VERSION := TAG
NEW_VERSION := $(shell echo $(TAG) | awk -F. '{$$NF = $$NF + 1;} 1' | sed 's/ /./g')

DIRECTORY=docs/docs/aws2024-components/output/drawio
OUTPUT_DIR=docs/docs/aws2024-components/output/jpg
DRAWIO_APP=/Applications/draw.io.app/Contents/MacOS/draw.io
QUALITY=100
FORMAT=jpg

define colorecho
      @tput setaf 6
      @echo $1
      @tput sgr0
endef

.PHONY: run

# Function to get the drawio file from git status
get_drawio_file = $(shell git status $(DIRECTORY) | grep -oE "$(DIRECTORY)/[^\s]+\.drawio")

# Target to process drawio file
process_drawio:
	@drawio_file=$(call get_drawio_file) && \
	if [ -n "$$drawio_file" ]; then \
		echo "Processing file: $$drawio_file"; \
		$(DRAWIO_APP) -q $(QUALITY) -x -f $(FORMAT) $$drawio_file -o $(OUTPUT_DIR); \
	else \
		echo "No .drawio files found in the specified directory."; \
	fi


doc: test images
	$(call colorecho, "Starting Documentation locally...")
	cd docs && bundle exec just-the-docs rake search:init \
	cd docs && bundle exec jekyll serve --trace

icons:
	./resize_icons.sh

images: icons
	./gen_images.sh

landscape:
	$(call colorecho, "Generating new Landscape...")
	cd samples && poetry run python landscape.py
	/Applications/draw.io.app/Contents/MacOS/draw.io -x --border 2 -f png --scale 2 -o landscape.png landscape.drawio

changelog: test
	$(call colorecho, "Preparing CHANGELOG...")
	poetry run git-changelog -c angular -s docs,feat,test --output CHANGELOG.MD

test:
	$(call colorecho, "Run all Tests...")
	poetry run python -m unittest -v tests/*.py
	poetry run python -m unittest -v tests/aws/*.py
	poetry run python -m unittest -v tests/aws2024/*.py
	poetry run python -m unittest -v tests/core/*.py
	poetry run python -m unittest -v tests/onprem/*.py
	$(call colorecho, "Run flakehell lint...")
	poetry run flakehell lint

check:
	@echo Old tag: $(TAG) New tag: $(NEW_VERSION)

pre-release:
	$(call colorecho, "Preparing Release with new version...")
	poetry version $(NEW_VERSION)
	git add .
	git tag $(NEW_VERSION)
	$(MAKE) changelog
	$(MAKE) release2docs
	git tag -d $(NEW_VERSION)
	git add . && git commit -m "bump: version $(TAG) -> $(NEW_VERSION)" && git tag $(NEW_VERSION)

release: pre-release
	$(call colorecho, "Push to origin with TAGs...")
	git push
	git push --tags

release2docs:
	$(call colorecho, "Adding changelog to online docs...")
	{ echo '---'; echo 'title: CHANGELOG'; echo 'layout: default'; echo '---'; echo ''; cat CHANGELOG.MD; } > "docs/CHANGELOG.md"
