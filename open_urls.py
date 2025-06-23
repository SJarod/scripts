import webbrowser

urls = {
    "url1",
    "url2"
}

for url in urls :
    webbrowser.get("firefox").open_new_tab(url)
