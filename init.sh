#!/bin/bash

# My Hello, World! script
sudo mkdir data
sudo mkdir data/backend
sudo mkdir data/mongo

sudo chmod -R 777 data

cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
