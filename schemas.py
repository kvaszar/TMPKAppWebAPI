from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    login: str
    password: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode=True




class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    class Config:
        orm_mode=True



class CustomerBase(BaseModel):
    name: str
    phone_number:str
    status: int

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    class Config:
        orm_mode=True



class ContractBase(BaseModel):
    date: str
    osmp: str

class ContractCreate(ContractBase):
    pass

class Contract(ContractBase):
    id: int
    class Config:
        orm_mode=True



class ServiceBase(BaseModel):
    name: str

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int
    class Config:
        orm_mode=True



class AddressBase(BaseModel):
    house: int
    frac: str
    flat: int

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    id: int
    class Config:
        orm_mode=True



class CommutatorBase(BaseModel):
    name: str
    ip: str

class CommutatorCreate(CommutatorBase):
    pass

class Commutator(CommutatorBase):
    id: int
    class Config:
        orm_mode=True



class PortBase(BaseModel):
    name: str
    number: int
    status_link: str

class PortCreate(PortBase):
    pass

class Port(PortBase):
    id: int
    class Config:
        orm_mode=True



class TaskBase(BaseModel):
    topic: str
    description: str
    date_creation: str
    date_from: str
    date_to: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    class Config:
        orm_mode=True