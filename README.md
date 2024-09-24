# img-hosting
This is a python-base image hosting service.

## Send an image
API: `POST /upload/`

Parameter: `file=<form-data>`

Return: `{"filename": "<image_filename>"}`

## Get an image
API: `GET /img/<filename>/`

Parameter: `filename=<filename>`

Return: `the image file`