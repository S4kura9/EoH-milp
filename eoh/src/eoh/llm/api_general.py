import http.client
import json
import requests
import time
class InterfaceAPI:
    def __init__(self, api_endpoint, api_key, model_LLM, debug_mode):
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.model_LLM = model_LLM
        self.debug_mode = debug_mode
        self.n_trial = 5

    def get_response(self, prompt_content):
        payload = {
                "model": self.model_LLM,
                "messages": [
                     {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt_content}
                ],
            }
       # print(payload["model"])
        #print(payload["messages"])
       # print("self.api_key:",self.api_key)
        headers = {
            "Authorization": f"Bearer {self.api_key}" ,
            "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
            "Content-Type": "application/json",
            "x-api2d-no-cache": "1",
        }
        
        response = None
        n_trial = 1
        while True:
            n_trial += 1
            if n_trial > self.n_trial:
                return response
            try:
                """conn = http.client.HTTPSConnection(self.api_endpoint)
                conn.request("POST", "/v1/chat/completions", payload_explanation, headers)
                res = conn.getresponse()
                data = res.read()
                json_data = json.loads(data)
                response = json_data["choices"][0]["message"]["content"]
                break
                """
                # Send POST request to the API
                print("Sending request to Zhizengzeng API...")
                #print(self.api_endpoint)
                response = requests.post(self.api_endpoint, headers=headers, json=payload,timeout=10)
                
                #print(response)
                response.raise_for_status()  # Raise error for invalid responses (4xx/5xx)
                json_data = response.json()

                # Extract the generated content from response
                generated_content = json_data["choices"][0]["message"]["content"]
                #print("Response received:", generated_content)
                break
            except:
                if self.debug_mode:
                    print("Error in API. Restarting the process...")
                continue
            

        return generated_content