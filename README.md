# Vanna.AI Streamlit App
<img width="1392" alt="Screenshot 2023-06-23 at 3 49 45 PM" src="./assets/vanna_demo.gif">

# Install

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

# Configure
Modify the `setup_vanna` function in [vanna_calls.py](./vanna_calls.py) to use your desired Vanna setup.

You can configure secrets in `.streamlit/secrets.toml` and access them in your app using `st.secrets.get(...)`.

Generate api key using ...

```bash
python ./bin/get-vanna-api-key.py
Check your email for the code and enter it here: 000FFF
00ff0f000f0f0f0000ff0ff0f0f0f00f
```

# Run

```bash
streamlit run app.py
```

# Notes

Chinook.sqlite is being created in the folder in which the script is being invoked



## License
[MIT](https://choosealicense.com/licenses/mit/)
