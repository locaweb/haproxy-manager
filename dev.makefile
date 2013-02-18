bin_pip         = pip
bin_python      = python
venv_dir        = .venv
venv_bin        = $(venv_dir)/bin

config_file     = etc/haproxy-manager.cfg

default_env     = PYTHONPATH=src HAPROXYMANAGER_CFG=$(config_file)

clean:
	@find . -name '*.pyc' -delete

pep:
	@$(venv_bin)/pep8 --repeat --show-source src setup.py

install_venv:
	$(bin_pip) install virtualenv

create_venv: install_venv
	virtualenv $(venv_dir)

bootstrap: create_venv
	$(venv_bin)/$(bin_pip) install -r pip-requires

test:
	@$(default_env) $(venv_bin)/nosetests $(TEST)

server:
	@$(default_env) $(venv_bin)/python bin/haproxy-manager -a foreground
