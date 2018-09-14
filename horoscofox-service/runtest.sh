#!/bin/bash
find . -name "*.pyc" -exec rm -f {} \;
export IS_TEST='1'
echo "🥑 Run script in test mode"

if [ "$1" = "complete" ]; then
    pipenv install --dev --system --deploy
fi

pytest -v -s --cov=src

export IS_TEST='0'
echo "🔥 Exit from test mode"
