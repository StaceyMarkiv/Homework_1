def domain_name(url):
    url = url.split("/")

    domain_el = ""
    for el in url:
        if "." in el:
            domain_el = el.split(".")
            break

    result = domain_el[1] if domain_el[0] == "www" else domain_el[0]
    return result


if __name__ == "__main__":
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
