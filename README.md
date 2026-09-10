# Student Management API

REST API sederhana untuk mengelola data mahasiswa menggunakan FastAPI dan SQLite.

## Fitur

- Menambahkan data mahasiswa
- Menampilkan seluruh data mahasiswa
- Menampilkan data mahasiswa berdasarkan ID
- Memperbarui data mahasiswa
- Menghapus data mahasiswa
- Validasi input

## Teknologi

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Struktur Project

```text
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── routers/
    └── students.py
```

## Instalasi

Clone repository:
```text
git clone https://github.com/Hafidh-cloude/student-management-api.git
cd student-management-api
```

## Install dependencies:
```text
uv sync
```
## Jalankan aplikasi:
```text
uv run uvicorn app.main:app --reload
```
## API akan berjalan di:
```text
http://127.0.0.1:8000
```
## Interactive API documentation:
```text
http://127.0.0.1:8000/docs
```
## API Endpoints
Method	Endpoint	Deskripsi:
```text
GET	/students/	Menampilkan seluruh mahasiswa
POST	/students/	Menambahkan mahasiswa
GET	/students/{id}	Menampilkan mahasiswa berdasarkan ID
PUT	/students/{id}	Memperbarui data mahasiswa
DELETE	/students/{id}	Menghapus data mahasiswa
```
### Contoh
Menambahkan Mahasiswa
```text
POST /students/
```
Request:
```text
{
  "name": "Hafidh",
  "major": "Informatics",
  "semester": 8
}
```
Response:
```text
{
  "id": 1,
  "name": "Hafidh",
  "major": "Informatics",
  "semester": 8
}
```
