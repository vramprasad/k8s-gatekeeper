#!/bin/bash
helmfile -e dev sync
kubectl get events --field-selector type=Normal -n "client-api-dev"
