mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "[theme]
pbase='light'
primaryColor='#4d4c50'
backgroundColor='#fdf8f8'
textColor='#0a0000'
font = ‘sans serif’
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml