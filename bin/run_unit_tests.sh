#!/usr/bin/env bash

cd "${0%/*}"

export APPLICATION_DIR="$(dirname $(pwd))"

. $APPLICATION_DIR/bin/with_venv.sh

activate_build_venv
with_venv


pytest -s -vv --cov="$APPLICATION_DIR" --junit-xml="test_results.xml" --cov-report term-missing

echo "Running pytest"
pytest -s -vv --cov="$APPLICATION_DIR" --junit-xml="test_results.xml" --cov-report term-missing
 
echo "Generating coverage report"
coverage xml
coverage html -d coverage_html
coverage report --fail-under "$MIN_COVERAGE_PERCENTAGE" --skip-covered
popd_silent