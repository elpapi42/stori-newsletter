#!/bin/bash

# My Hello, World! script
sudo mkdir data
sudo mkdir data/backend
sudo mkdir data/mongo

sudo chmod 777 -R data

cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
