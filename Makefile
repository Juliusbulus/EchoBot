APP        ?= echobot
ENV_FILE   ?= .env
AUDIO_DIR  ?= /home/wotori/echobot/generated_audio
STATE_DIR  ?= /home/wotori/echobot/state

docker-build:
	docker build -t $(APP) .

# Interactive/dev run (Ctrl+C to stop; container removed after)
docker-run: ensure-dirs
	docker run --rm -it \
	  -p 8000:8000 \
	  --env-file $(ENV_FILE) \
	  -v "$(AUDIO_DIR)":/app/voice/generated_audio:rw \
	  -v "$(STATE_DIR)":/app/state:rw \
	  $(APP)

# Optional: background mode you can leave running
docker-run-detached: ensure-dirs stop
	docker run -d --name $(APP) \
	  -p 8000:8000 \
	  --env-file $(ENV_FILE) \
	  -v "$(AUDIO_DIR)":/app/voice/generated_audio:rw \
	  -v "$(STATE_DIR)":/app/state:rw \
	  --restart unless-stopped \
	  $(APP)
	@echo "Running: docker logs -f $(APP)  # to see logs"

stop:
	-@docker rm -f $(APP) >/dev/null 2>&1 || true

ensure-dirs:
	mkdir -p "$(AUDIO_DIR)" "$(STATE_DIR)"


docker-rebuild:
	docker image prune -f || true
	docker builder prune -f || true
	docker build --pull --no-cache -t echobot .

python-flake8:
	flake8 .

python-test:
	pytest .

python-lint-fix:
	black .
	mypy .
# 	ruff check . --fix
	flake8 .

python-test:
	python -m pytest .

scripts-collect-media:
	python3 ./scripts/obs_collect_media.py ./EchoBot.json ~/EchoBotMedia
