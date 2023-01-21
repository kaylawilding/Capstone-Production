FROM python:3.10

#set working directory
WORKDIR /usr/src/app

#Copy files to computer
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "./loandefault.py"]