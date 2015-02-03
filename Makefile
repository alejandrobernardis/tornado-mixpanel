clear:
	-rm -fRv build data dist docs libs *.egg-info

deps:
	mkdir -v libs
	pip install -t libs -r requirements.txt

