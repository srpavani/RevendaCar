import openai

def get_car_ai_bio(model, brand, year):
    prompt1 = '''
    Provide a sales description for the {} {} {} car in 250 characters or less, highlighting its positive features to aid in selling the car. Be specific and concise.
    '''.format(brand, model, year)
    
    openai.api_key = ''  
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt1,
        max_tokens=250,
    )
    
    return response.choices[0].text
