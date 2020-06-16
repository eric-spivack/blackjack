#!/usr/bin/env bash

set_venv () {
    if [[ -z "${#JENKINS_URL}" ]]; then
        # Avoid long paths that lead to issues running pip in virtualenv
        # https://github.com/pypa/pip/issues/1773
        export VENV="$(mktemp -d "/tmp/venv.XXXXXXXX")"
    else
        export VENV="$APPLICATION_DIR/venv/blackjack"
    fi

    if [[ ! -d "$VENV" ]]; then
        echo "Creating virtual environment $VENV"
        python3 -m venv $VENV
    fi
}

with_venv () {
    . "$VENV/bin/activate"
}

activate_build_venv () {
  with_venv
  pip3 install -r "$APPLICATION_DIR/src/requirements.txt" 1> /dev/null
}

if [[ ! -z "${#VENV}" ]]; then
    set_venv
fi
