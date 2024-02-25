from dotenv import load_dotenv
import os


load_dotenv()

PORT = os.getenv("PORT")
MODEL_PATH = os.getenv("MODEL_PATH")
FOOD_CLASS_TEST_PATH= os.getenv("FOOD_CLASS_TEST_PATH")