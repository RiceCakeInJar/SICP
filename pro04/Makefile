PHONY: all
all:
	cp ../../../ok ./
	cp ../../../scheme ./
	python3 ok --local --lock
	zip proj4-Code.zip -r abstract_trutle/ editor/ images/ tests/*.py *.py *.scm *.ok ok scheme scheme_reader mytests.rst