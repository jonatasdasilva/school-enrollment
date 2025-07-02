#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  School Enrollment API

  Author: Jônatas da Silva Santos
  version: 1.0
  Ano: 2025
  
  Description:
    - pt-br: Uma API para matrícula de alunos em escolas.
    - en: An API for enrolling students in schools.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import routes

api = FastAPI() # Create instance of the calss FAstAPI.
origins = ["*"] # Specifies the request sources.


# Include Meddleware for anable CORS.
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes for API.
api.include_router(routes.router)

# Call for main
if __name__ == "__main__":
  print('Olá Dev 🥳,o School Enrollment API 🫀 - 🧠 estar em execução 🖖👊!')
  # API available for queries.
  uvicorn.run("__main__:api", host="0.0.0.0", port=8778,
              workers=4, log_level="info", reload=True)