import requests

class CaptchaError(Exception):
    pass

class CaptchaSolver:
    def __init__(self, api_key, task_type, website_url, proxy="", website_public_key="A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F"):
        self.api_key = api_key
        self.task_type = task_type
        self.website_url = website_url
        self.website_public_key = website_public_key
        self.url = 'https://capbypass.com/api/createTask'
        self.headers = {
            'Host': 'capbypass.com',
            'Content-Type': 'application/json',
        }
        self.proxy = proxy
    
    def create_captcha_task(self, blob=""):
        try:
            data = {
                "clientKey": self.api_key,
                "task": {
                    "type": self.task_type,
                    "websiteURL": self.website_url,
                    "websitePublicKey": self.website_public_key,
                    "data[blob]": blob,
                    "proxy": self.proxy
                }
            }

            response = requests.post(self.url, headers=self.headers, json=data)
            response_data = response.json()

            if "error" in response_data:
                raise CaptchaError(f"Error in creating captcha task: {response_data}")

            return response_data

        except requests.exceptions.RequestException as e:
            raise CaptchaError(f"Error in sending captcha request: {e}")

    def get_balance(self):
        try:
            data = {
                "clientKey": self.api_key
            }

            response = requests.post('https://capbypass.com/api/getBalance', headers=self.headers, json=data)
            response_data = response.json()

            return response_data["balance"]

        except requests.exceptions.RequestException as e:
            raise CaptchaError(f"Error in getting account balance: {e}")
