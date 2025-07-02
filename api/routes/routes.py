#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http import HTTPStatus
from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

#from api.models import Student
from .models import Student
from .settings import Settings
from sqlalchemy import func


# Create Router for API
router = APIRouter()


# Rota Principal
@router.get("/", response_model=dict, status_code=HTTPStatus.OK, tags=["Main"])
async def principal():
    """
    - pt-br:
        Rota principal para o School Enrollment API.
    - en:
        Main route to School Enrollment API.
    """
    return {"message": "Ola dev 👨🏽, vamos decolar na 🚀 do School Enrollment API!"}


# Rota de Listagem de alunos
@router.get("/students", status_code=HTTPStatus.OK, tags=["Students"])
async def list_students():
    """
    - pt-br:
        Rota para listar todos os alunos.
    - en:
        Route to list all students.
    """
    engine = create_engine(Settings().DATABASE_URL)
    with Session(engine) as session:
        students = session.scalars(select(Student)).all()
        session.close()
        return { "students": students }


# Rota de Matricula de alunos
@router.post("/students", status_code=HTTPStatus.CREATED, tags=["Students"])
async def create_student(request: Request):
    """
    - pt-br:
        Rota para matricular um aluno.
    - en:
        Route to enroll a student.
    """
    data = await request.json()
    engine = create_engine(Settings().DATABASE_URL)
    
    with Session(engine) as session:
        total_estudantes = session.scalar(select(func.count(Student.id)))
        if total_estudantes:
            student_exists =session.scalar(select(Student).where(Student.name == data['name'] and Student.responsible == data['responsible']))
            if student_exists:
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Student already exists!")
        student = Student(name=data['name'], age=data['age'], classroom=data['classroom'], responsible=data['responsible'])
        session.add(student)
        session.commit()
        current = session.refresh(student)
        session.close()

        return { "message": "Student enrolled successfully!", "student": student }


# Rota de exclusão de aluno
@router.delete("/students/{id}", status_code=HTTPStatus.OK, tags=["Students"])
async def delete_student(id: int):
    """
    - pt-br:
        Rota para excluir um aluno.
    - en:
        Route to delete a student.
    """
    engine = create_engine(Settings().DATABASE_URL)
    with Session(engine) as session:
        student = session.scalar(select(Student).where(Student.id == id))
        session.delete(student)
        session.commit()
        session.close()
        return { "message": "Student deleted successfully!", "student": student }


# Rota de atualização de aluno
@router.patch("/students/{id}", status_code=HTTPStatus.OK, tags=["Students"])
async def update_student(id: int, request: Request):
    """
    - pt-br:
        Rota para atualizar um aluno.
    - en:
        Route to update a student.
    """
    data = await request.json()
    engine = create_engine(Settings().DATABASE_URL)

    with Session(engine) as session:
        student = session.scalar(select(Student).where(Student.id == id))

        if not student:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Student not found!")
        else:
            if 'name' in data and student.name != data['name']:
                student.name = data['name']
            if 'age' in data and student.age != data['age']:
                student.age = data['age']
            if 'classroom' in data and student.classroom != data['classroom']:
                student.classroom = data['classroom']
            if 'responsible' in data and student.responsible != data['responsible']:
                student.responsible = data['responsible']
            session.add(student)
            session.commit()
            session.refresh(student)
            session.close()
            return { "message": "Student updated successfully!", "student": student }
