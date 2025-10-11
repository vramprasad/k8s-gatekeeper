#!/bin/bash
helmfile sync
kubectl get events --namespace gk-test