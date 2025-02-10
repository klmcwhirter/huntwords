#!/usr/bin/env bash

function echo_eval
{
    echo "$@"
    $@
}

echo $0: $(pwd)

echo_eval cd ui
echo_eval rm -fr node_modules/

npm install corepack@latest && \
corepack enable pnpm

# curl -fsSL https://get.pnpm.io/install.sh | sh -

mkdir -p ~/.local/share/pnpm-store
pnpm config set store-dir ~/.local/share/pnpm-store

echo_eval pnpm install
