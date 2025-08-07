# "https://gujarathighcourt.nic.in/","https://chatgpt.com/c/673191fa-68dc-800e-b78e-5ce37cd20458","https://github.com/OWASP/Nettacker?tab=readme-ov-file"
import requests

# List of URLs to check
urls = [
    "https://gujarathighcourt.nic.in/",
    "https://chatgpt.com/c/673191fa-68dc-800e-b78e-5ce37cd20458",
    "https://github.com/OWASP/Nettacker?tab=readme-ov-file"
]


def check_url(url):
    try:
        response = requests.get ( url, timeout = 3 )
        print ( f"Checking {url}..." )

        # Check if the server header is present
        if "Server" in response.headers:
            print ( "  Server information:", response.headers["Server"] )

        # Check status code
        if response.status_code == 200:
            print ( "  Status: Reachable" )
        else:
            print ( f"  Status: {response.status_code}" )

        # Additional checks
        if "X-XSS-Protection" not in response.headers:
            print ( "  Warning: Missing X-XSS-Protection header" )
        if "X-Content-Type-Options" not in response.headers:
            print ( "  Warning: Missing X-Content-Type-Options header" )
        if "Strict-Transport-Security" not in response.headers:
            print ( "  Warning: Missing Strict-Transport-Security header" )
        if "Content-Security-Policy" not in response.headers:
            print ( "  Warning: Missing Content-Security-Policy header" )

    except requests.RequestException as e:
        print ( f"  Error connecting to {url}: {e}" )
    print ( "-" * 50 )


# Check each URL in the list
for url in urls:
    check_url ( url )
