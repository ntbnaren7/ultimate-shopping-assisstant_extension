from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ultimate Shopping Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Ultimate Shopping Assistant API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

from scraper import scraper

@app.post("/api/v1/products/search")
async def search_products(query: str):
    results = await scraper.scrape_prices(query)
    return {"results": results}

from ml_engine import predictor

@app.get("/api/v1/products/{product_id}/history")
async def get_price_history(product_id: str):
    prediction = predictor.predict_price_drop(product_id)
    return prediction

from summarizer import summarizer

@app.get("/api/v1/products/{product_id}/reviews")
async def summarize_product_reviews(product_id: str):
    summary = summarizer.summarize_reviews(product_id)
    return summary



