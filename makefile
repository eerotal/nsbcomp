CONF=nsbcomp.conf
ROOT_DIR=$(dir $(realpath $(lastword $(MAKEFILE_LIST))))

ifeq ($(ROOT_DIR),'')
$(error nsbcomp root dir variable empty! Won't continue)
endif

ifndef VERBOSE
.SILENT:
endif

.PHONY: configure clean LOC

configure:
	# Configure include path.
	echo -n 'INCLUDE_PATHS=' > $(CONF)
	echo $(ROOT_DIR) >> $(CONF)

	# Configure tmp directory path.
	echo -n 'DIR_TMP=' >> $(CONF)
	echo $(ROOT_DIR)'/tmp' >> $(CONF)

clean:
	# Clean generated files.
	rm -f nsbcomp.conf
	rm -f nsbcomp/*.pyc
	rm -rf nsbcomp/__pycache__
	rm -f *.nsmin
	rm -rf tmp

LOC:
	wc -l nsbcomp/*.py defs/*
