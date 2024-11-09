import uvicorn
from fastapi import FastAPI, HTTPException,Path,Query,Body, Depends
from typing import Optional,List, Dict,Annotated
from sqlalchemy.orm import Session
from models import Base,User,Role,Customer,Contract,Service,Address,Commutator,Port,Task
from database import engine,session_local
from schemas import UserCreate,User as DbUser,RoleCreate,Role as DbRole,CustomerCreate,Customer as DbCustomer,ContractCreate,Contract as DbContract,ServiceCreate,Service as DbService,AddressCreate,Address as DbAddress, CommutatorCreate,Commutator as DbCommutator,PortCreate,Port as DbPort,TaskCreate,Task as DbTask

app=FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=session_local()
    try:yield db
    finally:db.close()


@app.post('/users/',response_model=DbUser)
async def create_user(user:UserCreate,db:Session=Depends(get_db)) -> DbUser:
    db_user=User(name=user.name,login=user.login,password=user.password,email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post('/roles/',response_model=DbRole)
async def create_role(role:RoleCreate,db:Session=Depends(get_db)) -> DbRole:
    db_role=Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@app.post('/customers/',response_model=DbCustomer)
async def create_Customer(customer:CustomerCreate,db:Session=Depends(get_db)) -> DbCustomer:
    db_customer=Customer(name=customer.name,phone_number=customer.phone_number,status=customer.status)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.post('/contracts/',response_model=DbContract)
async def create_Contract(contract:ContractCreate,db:Session=Depends(get_db)) -> DbContract:
    db_contract=Contract(date=contract.date,osmp=contract.osmp)
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

@app.post('/services/',response_model=DbService)
async def create_Service(service:ServiceCreate,db:Session=Depends(get_db)) -> DbService:
    db_service=Service(name=service.name)
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

@app.post('/addresses/',response_model=DbAddress)
async def create_Address(address:AddressCreate,db:Session=Depends(get_db)) -> DbAddress:
    db_address=Address(house=address.house,frac=address.frac,flat=address.flat)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

@app.post('/commutators/',response_model=DbCommutator)
async def create_Commutator(commutator:CommutatorCreate,db:Session=Depends(get_db)) -> DbCommutator:
    db_commutator=Commutator(name=commutator.name,ip=commutator.ip)
    db.add(db_commutator)
    db.commit()
    db.refresh(db_commutator)
    return db_commutator

@app.post('/ports/',response_model=DbPort)
async def create_Port(port:PortCreate,db:Session=Depends(get_db)) -> DbPort:
    db_port=Port(name=port.name,number=port.number,status_link=port.status_link)
    db.add(db_port)
    db.commit()
    db.refresh(db_port)
    return db_port

@app.post('/tasks/',response_model=DbTask)
async def create_Task(task:TaskCreate,db:Session=Depends(get_db)) -> DbTask:
    db_task=Task(topic=task.topic,description=task.description,date_creation=task.date_creation,date_from=task.date_from,date_to=task.date_to)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get('/users/',response_model=List[DbUser])
async def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()

@app.delete("/users/{user_id}")
async def delete_item(user_id: int):
    db = session_local()
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
 
 
if __name__ == "__main__":
    uvicorn.run(app)