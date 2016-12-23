all: docs

docs: FORCE
	MSG="$(shell git log -1 --pretty=%B | tr -d '\n')"
	@echo $(MSG)
	pandoc README.md -o docs/README.rst; \
	cd ~/pages/mcnp_companion/; \
	git rm -r *; \
	cd ~/code/mcnp_companion/docs/; \
	make html; \
	cp -r .build/html/* ~/pages/mcnp_companion/; \
	cd ~/pages/mcnp_companion/docs; \
	git add *; \
	git commit -am "$(shell git log -1 --pretty=%B | tr -d '\n')"; \
	git push origin gh-pages; \
	cd ~/code/mcnp_companion

FORCE:
