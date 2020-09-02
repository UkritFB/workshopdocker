FROM python:3.6-alpine 
# RUN echo First Build Docker images
WORKDIR /app  
# ADD . /app/www
COPY . .
# RUN pip3 -V
# RUN python3 -V
RUN pip3 install flask
EXPOSE 5008
CMD ["python3","server.py"]

# RUN pip3 install flask
# EXPOSE 5008cl
# CMD ["python","server.py"]