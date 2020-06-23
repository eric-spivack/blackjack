#!/usr/bin/env bash

cd "${0%/*}"

export APPLICATION_DIR="$(dirname $(pwd))"

. $APPLICATION_DIR/bin/with_venv.sh

activate_build_venv
with_venv

pushd "$APPLICATION_DIR" 1> /dev/null

echo "Running pytest"
pytest -s -vv --cov="$APPLICATION_DIR/src" --junit-xml="test_results.xml" --cov-report term-missing
 
echo "Generating coverage report"
coverage xml
coverage html -d coverage_html
coverage report --fail-under "85" --skip-covered

popd 1> /dev/null
