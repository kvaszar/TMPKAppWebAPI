import uvicorn
from fastapi import FastAPI, HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from models import Base,User,Role,Customer,Contract,Service,Address,Commutator,Port,Task
from database import engine,session_local
from schemas import UserCreate,User as DbUser,RoleCreate,Role as DbRole,CustomerCreate,Customer as DbCustomer,ContractCreate,Contract as DbContract,ServiceCreate,Service as DbService,AddressCreate,Address as DbAddress, CommutatorCreate,Commutator as DbCommutator,PortCreate,Port as DbPort,TaskCreate,Task as DbTask

app=FastAPI()

# Настройка CORS
origins=[
    'http;//localhost:8080',
    'http://127.0.0.1:8000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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
    db_user=db.query(User).filter(User.id==role.user_id).first()
    if db_user is None:raise HTTPException(status_code=404,detail='User not found')
    db_role=Role(name=role.name,user_id=role.user_id)
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
    db_customer=db.query(Customer).filter(Customer.id==contract.customer_id)
    if db_customer is None:raise HTTPException(status_code=404,detail='Customer not found')
    db_contract=Contract(date=contract.date,osmp=contract.osmp,customer_id=contract.customer_id)
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

@app.post('/services/',response_model=DbService)
async def create_Service(service:ServiceCreate,db:Session=Depends(get_db)) -> DbService:
    db_contract=db.query(Contract).filter(Contract.id==service.contract_id)
    if db_contract is None:raise HTTPException(status_code=404,detail='Contract not found')
    db_service=Service(name=service.name,contract_id=service.contract_id)
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
    db_address=db.query(Address).filter(Address.id==commutator.address_id).first()
    if db_address is None:raise HTTPException(status_code=404,detail='Address not found')
    db_commutator=Commutator(name=commutator.name,ip=commutator.ip,address_id=commutator.address_id)
    db.add(db_commutator)
    db.commit()
    db.refresh(db_commutator)
    return db_commutator

@app.post('/ports/',response_model=DbPort)
async def create_Port(port:PortCreate,db:Session=Depends(get_db)) -> DbPort:
    db_commutator=db.query(Commutator).filter(Commutator.id==port.commutator_id)
    if db_commutator is None:raise HTTPException(status_code=404,detail='Commutator not found')
    db_port=Port(name=port.name,number=port.number,status_link=port.status_link,commutator_id=port.commutator_id)
    db.add(db_port)
    db.commit()
    db.refresh(db_port)
    return db_port

@app.post('/tasks/',response_model=DbTask)
async def create_Task(task:TaskCreate,db:Session=Depends(get_db)) -> DbTask:
    db_contract=db.query(Contract).filter(Contract.id==task.contract_id)
    if db_contract is None:raise HTTPException(status_code=404,detail='Contract not found')
    db_task=Task(topic=task.topic,description=task.description,date_creation=task.date_creation,date_from=task.date_from,date_to=task.date_to,contract_id=task.contract_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get('/users/',response_model=List[DbUser])
async def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    db = session_local()
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

@app.get('/roles/',response_model=List[DbRole])
async def get_roles(db:Session=Depends(get_db)):
    return db.query(Role).all()

@app.delete("/roles/{role_id}")
async def delete_role(role_id: int):
    db = session_local()
    db_role = db.query(Role).filter(Role.id == role_id).first()
    db.delete(db_role)
    db.commit()
    return {"message": "Role deleted successfully"}

@app.get('/customers/',response_model=List[DbCustomer])
async def get_customers(db:Session=Depends(get_db)):
    return db.query(Customer).all()

@app.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):
    db = session_local()
    db_customer = db.query(Customer).filter(Customer.id == customer_id)
    db.delete(db_customer)
    db.commit()
    return {"message": "Customer deleted successfully"}

@app.get('/contracts/',response_model=List[DbContract])
async def get_contracts(db:Session=Depends(get_db)):
    return db.query(Contract).all()

@app.delete("/contracts/{contract_id}")
async def delete_contract(contract_id: int):
    db = session_local()
    db_contract = db.query(Contract).filter(Contract.id == contract_id)
    db.delete(db_contract)
    db.commit()
    return {"message": "Contract deleted successfully"}

@app.get('/services/',response_model=List[DbService])
async def get_services(db:Session=Depends(get_db)):
    return db.query(Service).all()

@app.delete("/services/{service_id}")
async def delete_service(service_id: int):
    db = session_local()
    db_service = db.query(Service).filter(Service.id == service_id)
    db.delete(db_service)
    db.commit()
    return {"message": "Service deleted successfully"}

@app.get('/addresses/',response_model=List[DbAddress])
async def get_addresses(db:Session=Depends(get_db)):
    return db.query(Address).all()

@app.delete("/addresses/{address_id}")
async def delete_address(address_id: int):
    db = session_local()
    db_address = db.query(Address).filter(Address.id == address_id)
    db.delete(db_address)
    db.commit()
    return {"message": "Address deleted successfully"}

@app.get('/commutators/',response_model=List[DbCommutator])
async def get_commutators(db:Session=Depends(get_db)):
    return db.query(Commutator).all()

@app.delete("/commutators/{commutator_id}")
async def delete_commutator(commutator_id: int):
    db = session_local()
    db_commutator = db.query(Commutator).filter(Commutator.id == commutator_id)
    db.delete(db_commutator)
    db.commit()
    return {"message": "Commutator deleted successfully"}

@app.get('/ports/',response_model=List[DbPort])
async def get_ports(db:Session=Depends(get_db)):
    return db.query(Port).all()

@app.delete("/ports/{port_id}")
async def delete_port(port_id: int):
    db = session_local()
    db_port = db.query(Port).filter(Port.id == port_id)
    db.delete(db_port)
    db.commit()
    return {"message": "Port deleted successfully"}

@app.get('/tasks/',response_model=List[DbTask])
async def get_tasks(db:Session=Depends(get_db)):
    return db.query(Task).all()

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    db = session_local()
    db_task = db.query(Task).filter(Task.id == task_id)
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app)