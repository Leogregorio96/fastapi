from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger():
    api_url = "https://api.z-api.io/instances/3BD6322606D6E0674FEFF626B4EBE407/token/D7ED546FAB2300706C2D0EEF/send-messages"

    payload = {
        "phone": "11964270049",
        "message": "COMIT NO VSCODE"
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Isso irá lançar um erro se a requisição não for bem-sucedida
        return "Resposta da APIhdfsjhgfsdjhfsdgjhs: " + response.text, 200  # Exibe a resposta da API
    except requests.exceptions.HTTPError as errh:
        return "Http Error: " + str(errh), 500
    except requests.exceptions.ConnectionError as errc:
        return "Error Connecting: " + str(errc), 500
    except requests.exceptions.Timeout as errt:
        return "Timeout Error: " + str(errt), 500
    except requests.exceptions.RequestException as err:
        return "Oops: Something Else " + str(err), 500

if __name__ == '__main__':
    app.run(debug=True)
