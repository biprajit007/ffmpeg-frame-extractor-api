#!/usr/bin/env python3
"""REST API to extract frames at timestamps."""
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import shutil, subprocess, tempfile
from pathlib import Path
app = FastAPI(title='ffmpeg-frame-extractor-api')
class Payload(BaseModel):
    input_path: str
    timestamp: str
@app.post('/extract')
def extract(p: Payload):
    if shutil.which('ffmpeg') is None: raise HTTPException(500, 'ffmpeg not found')
    src=Path(p.input_path)
    if not src.exists(): raise HTTPException(404, 'input not found')
    out=Path(tempfile.mkdtemp())/'frame.jpg'
    subprocess.check_call(['ffmpeg','-y','-ss',p.timestamp,'-i',str(src),'-frames:v','1',str(out)])
    return FileResponse(out)
