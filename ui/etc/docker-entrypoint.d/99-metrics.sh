#!/bin/sh
# vim:sw=2:ts=2:sts=2:et

function echo_bar
{
    echo -- ''
    echo -- '------------------------------------------------------------'
    echo -- $1
    echo -- '------------------------------------------------------------'
    echo -- ''
}

set -eu

LC_ALL=C
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

echo_bar PWD=`pwd`
ls -la

echo_bar '/usr/share/nginx/html'
ls -laR /usr/share/nginx/html

echo_bar '/etc/nginx'
ls -laR /etc/nginx


echo_bar 'SUMMARY'

echo SCRIPT: $0 $*
echo NGINX: `nginx -v`
echo
echo ui: http://localhost:${EXPOSED_UI_PORT}

echo_bar DONE
