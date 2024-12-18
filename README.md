# Release notes

- 2024/05/20 (1:00 am) release v1.0, with a basic gpt backend api server, and a simple vue.js web ui
- 2024/05/28 (11:36 pm) update deployment tutorial for GPT server
- torch version should be updated, https://github.com/meta-llama/llama3/issues/80
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```



# LocalGPT deploy

The final version should be "one click deploy on PC"


Currently you can manually deploy with following steps:

- 1 model preparation

1.1 create a directory D:/docker_volume

1.2 save model under D:/docker_volume/models

e.g. Qwen model "D:\docker_volume\models\Qwen1.5-4B-Chat", you can also use Llama3-8B-Chat, or Qwen1.5-7B-Chat



1.3 fetch local-gpt code
```
cd D:/docker_volume
git clone https://github.com/open-chinese/local-gpt.git
```

- 1 pull base image
```
docker pull nvcr.io/nvidia/pytorch:23.06-py3
```

- 2 start container
```
docker run --gpus all -it --rm -p 5050:5050 -p 5051:80 -v D:\docker_volume:/data --ipc=host nvcr.io/nvidia/pytorch:23.06-py3
```

- 3 setup env
```
cd /data/localgpt
bash init.sh
```

- 4 start server
```
cd /data/localgpt/gpt_server/app
python main.py
```

Now the gpt server should be started successfully, you can verify by the following instruction

```
curl --location 'http://localhost:5050/gpt/generate' \
--header 'Content-Type: application/json' \
--data '{
	"top_p": 0.95,
	"messages": [
        {"role": "system", "content": "Please help me to translate my input into Chinese."},
        {"role": "user", "content": "hello, what is your name? This is my first time in London, nice to see you here"},
        {"role": "assistant", "content": ""}
    ],
    "stop_words": ["。", "["], 
	"max_tokens": 40,
	"frequency_penalty": 0,
	"timeout": 30,
	"n": 1,
	"temperature": 1.0,
	"presence_penalty": 0
}
'
```

or with python scripts:

```
import requests
import json

url = "http://localhost:5050/gpt/generate"

payload = json.dumps({
  "top_p": 0.95,
  "messages": [
    {
      "role": "system",
      "content": "Please help me to translate my input into Chinese."
    },
    {
      "role": "user",
      "content": "hello, what is your name? This is my first time in London, nice to see you here"
    },
    {
      "role": "assistant",
      "content": ""
    }
  ],
  "stop_words": [
    "。",
    "["
  ],
  "max_tokens": 40,
  "frequency_penalty": 0,
  "timeout": 30,
  "n": 1,
  "temperature": 1,
  "presence_penalty": 0
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```




#### 3 Database

TODO
