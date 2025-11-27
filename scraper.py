import asyncio
from ddgs import DDGS
import google.generativeai as genai
import json

# Configure Gemini
genai.configure(api_key="AIzaSyBXVgxeol8dEtLsIlH_B_umVG7ha2oWJqA")

class PriceScraper:
    async def scrape_prices(self, product_name: str):
        results = []
        try:
            print(f"Searching DuckDuckGo for: {product_name}")
            
            # Use DuckDuckGo Search
            query = f"buy {product_name} online india price"
            
            # Get top 10 results
            ddgs = DDGS()
            search_results = list(ddgs.text(query, region='in-en', max_results=10))
            
            if not search_results:
                print("No results found on DuckDuckGo.")
                return []

            # Prepare text for Gemini
            search_text = ""
            for i, res in enumerate(search_results):
                search_text += f"Result {i+1}:\nTitle: {res['title']}\nLink: {res['href']}\nSnippet: {res['body']}\n\n"
            
            print(f"Sending {len(search_text)} chars to Gemini...")

            # Use Gemini to extract structured data
            # Explicitly using gemini-2.0-flash-lite as it was listed in available models
            model_name = 'gemini-2.0-flash-lite'
            print(f"Initializing Gemini Model: {model_name}")
            model = genai.GenerativeModel(model_name)
            
            prompt = f"""
            You are a smart shopping assistant. Analyze the following search results for the product "{product_name}".
            
            Your goal is to find 3-5 distinct online sellers and their current prices in INR (₹).
            Look for price patterns in the Titles and Snippets (e.g. "₹52,999", "Rs. 51,000").
            
            Return ONLY a valid JSON array of objects with these keys:
            - source: (e.g. "Amazon.in", "Flipkart", "Croma", "Reliance Digital")
            - price: (e.g. "₹52,999")
            - link: (The exact link provided in the search result)
            - shipping: (e.g. "Free", "See site")
            
            If a result mentions a price, use it. If multiple results are from the same store, pick the best one.
            If no prices are found in the text, but the link is a major retailer (Amazon/Flipkart), you can list it with price "Check Site".
            
            Search Results:
            {search_text}
            """
            
            response = model.generate_content(prompt)
            text_response = response.text.strip()
            
            # Clean up markdown
            if text_response.startswith("```json"):
                text_response = text_response[7:]
            if text_response.endswith("```"):
                text_response = text_response[:-3]
            
            results = json.loads(text_response)
            print(f"Gemini Extracted: {results}")

        except Exception as e:
            print(f"Error scraping/parsing: {e}")
            # Fallback
            results = [
                {"source": "Error Searching", "price": "N/A", "shipping": "-", "link": "#"}
            ]
            
        return results

scraper = PriceScraper()
