success_callback = []
failure_callback = []
set_verbose=False

####### COMPLETION MODELS ###################
open_ai_chat_completion_models = [
  'gpt-3.5-turbo', 
  'gpt-4'
]
open_ai_text_completion_models = [
    'text-davinci-003'
]

cohere_models = [
    'command-nightly',
]

anthropic_models = [
  "claude-2", 
  "claude-instant-1"
]

####### EMBEDDING MODELS ###################
open_ai_embedding_models = [
    'text-embedding-ada-002'
]

from .utils import client, logging, exception_type  # Import all the symbols from main.py
from .main import *  # Import all the symbols from main.py

