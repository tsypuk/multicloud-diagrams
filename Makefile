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

doc: test images
	$(call colorecho, "Starting Documentation locally...")
	cd docs && bundle exec just-the-docs rake search:init \
	cd docs && bundle exec jekyll serve --trace

icons:
	$(call colorecho, "Preparing aws service icons")
	/Applications/draw.io.app/Contents/MacOS/draw.io -q 100 -x -f jpg -r -o docs/icons/jpg tmp/drawio && \
 	./resize_icons.sh

images: icons
	 /Applications/draw.io.app/Contents/MacOS/draw.io -q 100 -x -f jpg -r -o docs/docs/aws-components/output/jpg docs/docs/aws-components/output/drawio
	 /Applications/draw.io.app/Contents/MacOS/draw.io -q 100 -x -f jpg -r -o docs/docs/core-components/output/jpg docs/docs/core-components/output/drawio
	 /Applications/draw.io.app/Contents/MacOS/draw.io -q 100 -x -f jpg -r -o docs/docs/onprem-components/output/jpg docs/docs/onprem-components/output/drawio


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
