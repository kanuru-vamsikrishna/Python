from urllib.parse import urlparse
def domain_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path
    domain_parts = domain.split(".")
    if domain_parts[0] == "www":
        return domain_parts[1]
    return domain_parts[0]

result = domain_name("https://www.youtube.com/watch?v=juuYq1_akKg")
result2 = domain_name("platform.openai.com")
print("Result1:", result)
print("Result2:", result2)