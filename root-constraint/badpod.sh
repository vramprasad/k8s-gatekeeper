#!/bin/bash
kubectl apply -f bad2.yaml
kubectl get events --namespace gk-test