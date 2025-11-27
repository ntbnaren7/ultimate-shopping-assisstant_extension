import pandas as pd
from prophet import Prophet
import datetime
import random

class PricePredictor:
    def predict_price_drop(self, product_id: str):
        # 1. Generate synthetic historical data (since we don't have a real DB yet)
        # In a real app, we'd query the database: SELECT date, price FROM prices WHERE product_id = ...
        
        today = datetime.date.today()
        dates = [today - datetime.timedelta(days=x) for x in range(30, 0, -1)]
        
        # Simulate a price trend for an iPhone-like product in INR
        # Base price around ₹70,000 with some fluctuation
        base_price = 70000.0
        prices = []
        for i, date in enumerate(dates):
            # Add some random fluctuation and a slight downward trend
            # Fluctuation between -₹1000 and +₹1000
            price = base_price - (i * 50) + random.uniform(-1000, 1000)
            prices.append(price)
            
        df = pd.DataFrame({'ds': dates, 'y': prices})
        
        # 2. Train Prophet Model
        m = Prophet(daily_seasonality=True)
        m.fit(df)
        
        # 3. Predict future (next 7 days)
        future = m.make_future_dataframe(periods=7)
        forecast = m.predict(future)
        
        # 4. Extract prediction for next week
        next_week = forecast.tail(7)
        min_price_row = next_week.loc[next_week['yhat'].idxmin()]
        
        predicted_date = min_price_row['ds'].strftime('%Y-%m-%d')
        predicted_price = round(min_price_row['yhat'], 2)
        confidence = 0.85 # Mock confidence score
        
        return {
            "current_price": round(prices[-1], 2),
            "currency": "INR",
            "predicted_best_buy_date": predicted_date,
            "predicted_price": predicted_price,
            "confidence_score": confidence,
            "history": [{"date": d.strftime('%Y-%m-%d'), "price": round(p, 2)} for d, p in zip(dates, prices)]
        }

predictor = PricePredictor()
