#!/bin/sh
##############################
# Perform docker compose
# From the following files:
# - docker-compose.yaml
# - prometheus.yaml
##############################

function help() {
  echo "Perform Docker Compose Function(s)"
  echo "Usage:"
  echo "- ${0} -u: docker-compose up"
  echo "- ${0} -d: docker-compose down"
  echo "- ${0} -l: docker-compose logs"
  echo "- ${0} -s: docker-compose stats"
  exit 0
}

function up() {
  echo "Performing docker compose up & detached"
  sudo docker compose up --detach
}

function down() {
  echo "Performing docker compose down"
  sudo docker compose down
}

function logs() {
  echo "Performing docker compose logs --follow"
  sudo docker compose logs --follow
}

function stats() {
  echo "Performing docker stats"
  sudo docker compose stats
}

# Conditional case for ARGS1
case "${1}" in
    "-u")
      up
      ;;
    "-d")
      down
      ;;
    "-l")
      logs
      ;;
    "-s")
      stats
      ;;
    *)
      help
      ;;
esac
