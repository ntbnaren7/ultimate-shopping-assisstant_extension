import random

class ReviewSummarizer:
    def summarize_reviews(self, product_id: str):
        # 1. Fetch reviews (Mocked)
        reviews = [
            "Great product, fast shipping!",
            "The quality is amazing for the price.",
            "Battery life could be better.",
            "Not what I expected, returned it.",
            "Highly recommend this seller."
        ]
        
        # 2. Analyze sentiment (Mocked logic)
        # In a real app, we'd use NLTK or TextBlob here.
        goods = [r for r in reviews if "Great" in r or "amazing" in r or "recommend" in r]
        bads = [r for r in reviews if "better" in r or "returned" in r]
        
        return {
            "total_reviews": len(reviews),
            "summary": {
                "goods": goods,
                "bads": bads
            },
            "overall_sentiment": "Positive" if len(goods) > len(bads) else "Mixed"
        }

summarizer = ReviewSummarizer()
