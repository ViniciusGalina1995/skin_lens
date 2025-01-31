docker_build_local:
	docker build --tag=$(GAR_IMAGE):local .

docker_run_local:
	docker run -it -e PORT=8000 -p 8000:8000 $(GAR_IMAGE):dev

docker_run_local_interactively:
	docker run -it -e PORT=8000 -p 8000:8000 $(GAR_IMAGE):dev bash
