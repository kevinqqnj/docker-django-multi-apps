#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A polls.taskapp beat -l INFO
