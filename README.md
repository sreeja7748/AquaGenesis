## <h1><p align="center">🫧𓇼𓏲*ੈ✩‧₊˚ 🌊 ***AquaGenesis*** 🫧𓇼𓏲*ੈ✩‧₊˚ 🌊</p></h1>

## 📖Overview

Aquagenesis is backend API for classifying environmental DNA (eDNA) sequences into taxonomic groups using a trained machine learning model based on SILVA reference(prokaryotic dataset) data.

The backend accepts FASTA (`.fa`, `.fasta`) and gzipped FASTA (`.fa.gz`) files, reads the DNA sequences, predicts their taxonomy, and returns the results in JSON format.

---

## 🗂️Project Structure

```text
Aquagenesis/
│
├── backend/
│   ├── backend.py                  # FastAPI application
│   ├── silva_model.joblib          # Trained ML model + vectorizer
│   ├── test_sequences.fasta        # Sample FASTA file for testing
│   └── requirements.txt            # Python dependencies
│
└── README.md
```

---

## ✨Features✨

* Upload FASTA (`.fa`, `.fasta`) files
* Upload gzipped FASTA (`.fa.gz`) files
* Parse DNA sequences using Biopython
* Predict taxonomy using a trained SILVA-based model
* Return predictions as JSON
* Test the API through FastAPI Swagger UI

---

## ⚛ Tech Stacks

### Programming Language:

* Python

### Backend Framework

* FatAPI(Swagger UI)

### Machine Learning
* Scikit-learn
* Multinomial Naive Bayes
* CountVectorizer
  
### Bioinformatics
* Biopython
* FASTA file parsing
* eDNA (Environmental DNA) sequence analysis
* SILVA Taxonomy Database
* Data Processing
* Pandas (for CSV handling, if used during training)
* CSV datasets
* Model Storage
* Joblib
* API Testing
* Swagger UI (FastAPI Docs)
* File Formats
* FASTA (.fa, .fasta)
* Compressed FASTA (.fa.gz)
* CSV
  
### Python Libraries
* FastAPI
* Uvicorn
* Biopython
* scikit-learn
* Joblib
* python-multipart
* gzip
* io
* csv
  
### Version Control
* Git
* GitHub
  
### Development Environment
* Visual Studio Code
* Windows Powershell

  ---

## Sneak Peak
### Swagger UI
<img width="965" height="998" alt="Screenshot (248)" src="https://github.com/user-attachments/assets/5795aa3f-4e87-49c3-8883-c4eb9314a39a" />

### Default
<img width="624" height="679" alt="Screenshot (249)" src="https://github.com/user-attachments/assets/4a6567ec-30fa-46ab-a869-859e23bffdce" />

### After Execution
<img width="936" height="1018" alt="Screenshot (251)" src="https://github.com/user-attachments/assets/942e3b87-a8a0-4095-94d4-2f14d0781cc4" />

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sreeja7748/Aquagenesis.git
cd Aquagenesis/backend
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Start the FastAPI server using:

```bash
python -m uvicorn backend:app --reload
```

Once the server is running, the API will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically provides interactive API documentation.

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

From this page, you can test the `/predict` endpoint by uploading a FASTA or `.fa.gz` file.

---

## API Endpoint

### `POST /predict`

Uploads a FASTA or gzipped FASTA file and returns predicted taxonomy for each DNA sequence.

#### Request

* **File:** FASTA (`.fa`, `.fasta`) or gzipped FASTA (`.fa.gz`)

#### Example Response

```json
{
  "predictions": [
    {
      "id": "seq1",
      "taxonomy": "Bacteria;Proteobacteria;Gammaproteobacteria"
    },
    {
      "id": "seq2",
      "taxonomy": "Bacteria;Firmicutes;Bacilli"
    }
  ]
}
```

---

## Requirements

* Python 3.10 or higher
* FastAPI
* Uvicorn
* Biopython
* Joblib
* Scikit-learn

---

## Notes

* The trained model file (`silva_model.joblib`) must be present in the `backend` folder before running the API.
* This repository contains only the backend implementation. The frontend can communicate with this API through the `/predict` endpoint.

---

## License

This project is for educational and research purposes.
