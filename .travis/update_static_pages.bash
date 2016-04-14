#!/bin/bash

set -e
set -x
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ "x$TRAVIS_PULL_REQUEST" != "xfalse" ] ; then
  exit 0
fi
git checkout ${TRAVIS_BRANCH}
${DIR}/regenerate_doc_index.py

git remote set-url origin --push $(git config --get remote.origin.url | sed 's;https://github.com/;git@github.com:;g')
git config user.name "DUNE Community Bot"
git config user.email "dune-community.bot@wwu.de"
git add ${DIR}/../docs/index.md
git commit -m '[doc] index update' || echo 'no changes to commit'
git push origin || echo ''
