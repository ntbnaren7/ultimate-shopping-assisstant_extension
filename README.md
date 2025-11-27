# 🛍️ Ultimate Shopping Assistant

## 🌟 Overview

The **Ultimate Shopping Assistant** is a comprehensive browser extension designed to empower online shoppers by consolidating crucial buying information into a single, non-intrusive sidebar. It utilizes a powerful Python backend to deliver real-time price comparisons, predictive analysis, and aggregated review summaries directly on e-commerce product pages.

This project was initially architected and scaffolded using the **Google Antigravity Agentic AI IDE**.

## 🚀 Features

The extension provides the following key insights:

  * **Best Buying Links:** Real-time price comparison across major competitor sites, sorted by lowest effective price.
  * **Price Prediction (The Crystal Ball):** An AI-driven forecast indicating the predicted optimal future low price and the likely best day to buy, based on historical data and seasonal sales analysis.
  * **Historical Price Graph:** A clear visualization of the product's price fluctuations over time.
  * **Website Trust Ranking:** A proprietary 1-10 score for retailers based on reliability, return policies, and shipping speed.
  * **Review Summary:** Aggregated product reviews categorized into "Goods" and "Bads" for a quick overview.

## 🏗️ Architecture

The system is split into two interconnected components:

1.  **Client (Browser Extension):** A lightweight JavaScript application that injects a content script into product pages, scrapes product metadata, and displays the UI dashboard.

      * **Tech:** JavaScript (ES6+), HTML/CSS (Tailwind).
      * **Deployment:** Manifest V3 (Chrome/Firefox).

2.  **Server (Data & Intelligence Backend):** A Python API responsible for all heavy computation and data persistence.

      * **Tech:** Python 3.12, FastAPI/Flask (for speed).
      * **Data/ML:** PostgreSQL Database (for historical prices), Prophet/ARIMA for Time Series Analysis, Playwright/Scrapy for Web Scraping.

## ⚙️ Local Development Setup

### Prerequisites

To run the backend service locally, you must have the following installed:

  * **Python 3.12**
  * **Conda/Miniconda** (for environment management)
  * **PostgreSQL** (or a local substitute like Dockerized PostgreSQL)

### Step 1: Clone the Repository

```bash
git clone [YOUR_REPO_URL]
cd ultimate-shopping-assistant
```

### Step 2: Set Up the Python Environment

We use Conda to manage dependencies and ensure Python 3.12 compatibility. Replace `[YOUR_ENV_NAME]` with your desired name (e.g., `shop-assistant-env`).

```bash
# Create and activate the Conda environment
conda create -n [YOUR_ENV_NAME] python=3.12
conda activate [YOUR_ENV_NAME]

# Install all backend dependencies
pip install -r server/requirements.txt
```

### Step 3: Database Configuration

1.  Set up your PostgreSQL database instance.

2.  Create a `.env` file in the `server/` directory and populate it with your credentials:

    ```env
    # .env in server/
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=shopping_db
    DB_USER=your_user
    DB_PASS=your_password
    API_KEY=super-secret-key # For extension-backend authentication
    ```

3.  Run the database migrations (scripts will be provided in the `server/db/` directory):

    ```bash
    python server/db/migrate.py
    ```

### Step 4: Run the Backend Server

Start the API server, which will be accessible by the extension:

```bash
conda activate [YOUR_ENV_NAME]
python server/main.py
```

The server should be running on `http://127.0.0.1:8000` (or the port defined in `main.py`).

### Step 5: Install the Browser Extension

1.  In your Chrome or Firefox browser, navigate to the Extension Management page (`chrome://extensions` or `about:addons`).
2.  Enable **Developer Mode**.
3.  Click **"Load unpacked"** (or similar) and select the local **`extension/`** directory.
4.  The extension should now be installed and active.

## 🤝 Contributing

Contributions are welcome\! Please submit a feature branch following these steps:

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

-----

*Created using the **Google Antigravity Agentic AI IDE**.*
