# backend.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from Bio import SeqIO
import gzip
import joblib
import io

app = FastAPI()

# Load the trained model and vectorizer once
model, vectorizer = joblib.load("silva_model.joblib")

@app.post("/predict")
async def predict_taxonomy(file: UploadFile = File(...)):
    # Decide how to open the uploaded file
    if file.filename.endswith(".gz"):
        handle = gzip.open(io.BytesIO(await file.read()), "rt")
    else:
        handle = io.StringIO((await file.read()).decode("utf-8"))

    results = []
    for record in SeqIO.parse(handle, "fasta"):
        seq = str(record.seq).strip()
        if not seq:
            continue
        X = vectorizer.transform([seq])
        pred = model.predict(X)[0]
        results.append({"id": record.id, "taxonomy": pred})

    return JSONResponse(content={"predictions": results})