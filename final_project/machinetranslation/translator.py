'''
This is the final project for python course
written by: Abdallah Alyamni
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# IBM watson translator credentials
apikey = os.environ['apikey']
url = os.environ['url']

# IBM watson translator instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    '''
    this function take english input and translates it to french text
    '''
    translation = language_translator.translate(text=englishText,model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

def frenchToEnglish(frenchText):
    '''
    this function take french input and translates it to english text
    '''
    translation = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    return translation['translations'][0]['translation']
