from fastapi import FastAPI,File,UploadFile,responses,APIRouter
from deta import Drive
from deta import Deta
import shutil



router = APIRouter(
    prefix='/upload_image',
    tags=['Upload Image'],
)
# deta = Deta("Project_Key")  # configure your Deta project
# drive = deta.Drive("images")

# @router.post("/upload")
# def upload(file:UploadFile= File(...)):
#     img = drive.put(file.filename,file.file)
#     return img


@router.post("/entity_upload")
def entity_cover_upload(id:int,uploadfile:UploadFile= File(...)):
    extension = uploadfile.filename.split('.')[1]
    path = f'images/entity/{id}.{extension}'
    with open(path,'w+b') as buffer:
        shutil.copyfileobj(uploadfile.file,buffer)
    return {'File name': path}\


@router.post("/gov_upload")
def governorate_cover_upload(id:int,uploadfile:UploadFile= File(...)):
    extension = uploadfile.filename.split('.')[1]
    path = f'images/gov/{id}.{extension}'
    with open(path,'w+b') as buffer:
        shutil.copyfileobj(uploadfile.file,buffer)
    return {'File name': path}

