from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from .routes.articulos import articles
from .routes.clientes import customers
from .routes.factura import invoice
from .routes.detalle import details

description = """
Crud de facturaccion en FastApi y SqlLite

Moises Nuñez del Rosario | 2020-10457
"""

app = FastAPI(
    title="Facturación",
    description=description,
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(customers)
app.include_router(articles)
app.include_router(invoice)
app.include_router(details)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")