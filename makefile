CONF=nsbcomp.conf

.PHONY: configure clean

configure:
	# Configure include path.
	echo -n 'INCLUDE_PATH=' > $(CONF)
	echo $(dir $(realpath $(lastword $(MAKEFILE_LIST)))) >> $(CONF)

clean:
	# Clean generated files.
	@rm -f nsbcomp/*.pyc
	@rm -rf nsbcomp/__pycache__
	@rm *.nsmin
	@rm -rf tmp
