import webbrowser

urls = {
}

for url in urls :
    webbrowser.get("firefox").open_new_tab(url)
