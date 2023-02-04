FROM python:3.9-slim 


RUN pip install numpy flask requests  pillow waitress
RUN pip install tensorflow
WORKDIR /app

COPY ["predict.py", "kitchenware_model.tflite", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "predict:app"]