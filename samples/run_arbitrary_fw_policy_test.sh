kubectl run my-task \
  --rm -it \
  --image=fw-policy-test:0.1\
  --overrides='
{
  "spec": {
    "hostNetwork": true,
    "containers": [
      {
        "name": "my-task",
        "image": "fw-policy-test:0.1",
        "imagePullPolicy": "Never",
        "stdin": true,
        "tty": true
      }
    ]
  }
}'
