# Makefile

SHELL := /bin/bash
TAG := $(shell git describe --tags --abbrev=0)
VERSION := TAG
NEW_VERSION := $(shell echo $(TAG) | awk -F. '{$$NF = $$NF + 1;} 1' | sed 's/ /./g')

define colorecho
      @tput setaf 6
      @echo $1
      @tput sgr0
endef

.PHONY: run

doc:
	$(call colorecho, "Starting Documentation locally...")
	cd docs && bundle exec just-the-docs rake search:init \
	cd docs && bundle exec jekyll serve --trace

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
	$(call colorecho, "Run flakehell lint...")
	poetry run flakehell lint

check:
	@echo Old tag: $(TAG) New tag: $(NEW_VERSION)

release:
	$(call colorecho, "Releasing new version...")
	poetry version $(NEW_VERSION)
	git add .
	git tag $(NEW_VERSION)
	$(MAKE) changelog
	git tag -d $(NEW_VERSION)
	git add . && git commit -m "bump: version $(TAG) -> $(NEW_VERSION)" && git tag $(NEW_VERSION)
	git push
	git push --tags

release2docs:
	$(call colorecho, "Releasing new version...")
	{ echo '---'; echo 'title: CHANGELOG'; echo 'layout: default'; echo '---'; echo ''; cat CHANGELOG.MD; } > "docs/CHANGELOG.md"
