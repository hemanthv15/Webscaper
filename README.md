# Project: Reviews Extraction API

## Description
This project is a Flask-based API server designed to extract reviews from any given product page. It uses Playwright for browser automation and integrates with a language model to dynamically identify CSS selectors for reviews. The API handles pagination to ensure all reviews are retrieved.

## Features
- **Dynamic CSS Selector Identification**: Uses an LLM to identify relevant CSS selectors for reviews and pagination.
- **Pagination Handling (Incomplete)**: Extracts reviews across multiple pages.
- **Browser Automation**: Uses Playwright to load and interact with web pages.
- **JSON Response**: Returns extracted reviews in a structured JSON format.

## Endpoints
### 1. `/api/reviews`
- **Method**: `GET`
- **Query Parameters**:
  - `page`: The URL of the product page to extract reviews from.
- **Response**:
  ```json
  {
    "reviews_count": 5,
    "reviews": [
      {
        "title": "Great Product",
        "body": "I love this product! It works perfectly.",
        "rating": 5,
        "reviewer": "John Doe"
      },
      {
        "title": "Not Bad",
        "body": "It’s decent but could be better.",
        "rating": 3,
        "reviewer": "Jane Smith"
      }
    ]
  }
  ```

## Setup and Installation

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/reviews-extraction-api.git
   cd reviews-extraction-api
   ```

2. Create and activate a virtual environment (Optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r flask playwright google.generativeai
   playwright install
   ```

4. Set up your environment variables:
   - Create a `.env` file in the root directory.
   - Add your LLM API key:
     ```env
     GOOGLE_API_KEY=your-google-api-key
     ```

5. Run the Flask application:
   ```bash
   python main.py
   ```

6. Access the API:
   - Open a browser and navigate to: `http://127.0.0.1:5000/api/reviews?page=<product_page_url>`

## File Structure
```
reviews-extraction-api/
├── main.py          # Entry point for the Flask app
├── scraper.py       # Handles browser automation and scraping logic
├── llm_helper.py    # Integrates with the LLM for CSS selector identification
├── config.py        # Configuration for API keys and settings
├── requirements.txt # List of dependencies
├── .env             # Environment variables (ignored by Git)
├── page_content.html # Debugging HTML content
├── reviews.txt      # Debugging extracted reviews
└── README.md        # Documentation
```

## Example Usage

### Request:
```bash
GET /api/reviews?page=https://example.com/product-page
```

### Response:
```json
{
  "reviews_count": 5,
  "reviews": [
    {
      "title": "Great Product",
      "body": "I love this product! It works perfectly.",
      "rating": 5,
      "reviewer": "John Doe"
    },
    {
      "title": "Not Bad",
      "body": "It’s decent but could be better.",
      "rating": 3,
      "reviewer": "Jane Smith"
    }
  ]
}
```

## Known Issues
- Unable to handle pagination
- Limited support for pages with complex dynamic content.
- Requires an active internet connection for LLM integration.

## Future Enhancements
- Include Pagination support
- Improve Documentation
- Add support for additional review formats.
- Improve error handling and logging.
- Add a frontend interface for users to input URLs and view results.


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, contact:
- **Name**: Your Name
- **Email**: your.email@example.com

