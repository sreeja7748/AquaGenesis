### AquaGenesis

Aquagenesis backend API for classifying environmental DNA (eDNA) sequences into taxonomic groups using a trained machine learning model based on SILVA reference data.

The backend accepts FASTA (`.fa`, `.fasta`) and gzipped FASTA (`.fa.gz`) files, reads the DNA sequences, predicts their taxonomy, and returns the results in JSON format.

---

## Project Structure

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

## Features

* Upload FASTA (`.fa`, `.fasta`) files
* Upload gzipped FASTA (`.fa.gz`) files
* Parse DNA sequences using Biopython
* Predict taxonomy using a trained SILVA-based model
* Return predictions as JSON
* Test the API through FastAPI Swagger UI

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Aquagenesis.git
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
