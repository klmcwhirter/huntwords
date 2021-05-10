#!/bin/bash

function echocmd
{
    echo $*
    $*
}

function makeConfigMap
{
    namespace=$1
    configMapName=$2
    dir=$3

    echocmd pushd ${dir}

    files=""
    for f in $(find . -type f -print)
    do
        files="${files} --from-file=$f"
    done

    # namespace was deleted earlier
    # echocmd kubectl delete -n ${namespace} configmap ${configMapName}

    echocmd kubectl create -n ${namespace} configmap ${configMapName} ${files}

    echocmd popd
}

echocmd kubectl delete -f k8s/namespace.yml

echocmd pushd ui

echocmd npm run build

echocmd popd

echocmd kubectl apply -f k8s/namespace.yml

echocmd makeConfigMap huntwords huntwords-artifacts ui/dist/huntwords

echocmd rm -fr build
echocmd mkdir -p build/etc/nginx

if [ ! -f etc-default/nginx/nginx.conf ]
then
    # copy default config
    echocmd docker run -d --name nginx nginx:alpine
    echocmd docker cp nginx:/etc/nginx build/etc
    echocmd docker stop nginx && docker rm -v nginx
else
    echocmd cp -r etc-default/nginx build/etc
fi

# overwrite with local config
echocmd rm -fr build/etc/nginx/conf.d
echocmd cp -r etc build

echocmd makeConfigMap huntwords huntwords-nginx-config build/etc/nginx

# clean up
echocmd rm -fr build
echocmd rm -fr ui/dist

echocmd kubectl apply -f k8s/deployment.yml

echocmd kubectl apply -f k8s/ingress.yml
