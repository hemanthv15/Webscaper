import os
import google.generativeai as genai
import time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pagination_info(content):
    prompt = f"""
    Extract the pagination information from the HTML content below:
    Look for the following information:
    - Type of pagination (e.g. "first/previous/next/last" as fpnl or "page number" as pgn)
    - Next page selector as next
    - Next page number selector as next
    - Review container selector as container
    
    Do not include any other text or comments in the response.
    Return the information in a JSON format with the following keys:
    
        'pagination_type': 'fpnl' or 'pgn',
        'next': 'next page selector' or 'next page number selector',
        'container': 'review container selector',

    Here is the HTML content:
    {content}
    """
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    print(response.text)
    #logging the response for debugging
    with open('response.txt', 'a') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S")+"\n\n"+response.text)
    
    return response.text

def get_reviews(page):
    prompt = f"""
    Extract all the reviews from the following HTML: {page.content}
    Look for the following information:
    - Review container selector as container
    - Review title selector as title
    - Review body text selector as body
    - Review rating selector as rating
    - Reviewer name selector as name

    Do not include any other text or comments in the response.
    Return the information in a JSON format.
    """

    #logging the prompt for debugging
    with open('reviews.txt', 'a') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S")+"\n\n"+prompt)

    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return response.text