import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('KXUshpUN2DLWmrJBiPf63YGtKnyos1w6a9nxKmE4jArq')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/c00bf373-4199-48fa-b418-075142f74843')

def english_to_french(english_text):
    '''
    This code converts english to french
    '''
    #write the code here
    frtr = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text = frtr['translations'][0]['translation']
    return french_text
def french_to_english(french_text):
    '''
    This code converts french to english
    '''
     #write the code here
    eng_tr = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text = eng_tr['translations'][0]['translation']
    return english_text
