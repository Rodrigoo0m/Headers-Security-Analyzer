import requests

def analyze_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        
        security_headers = {
            'Content-Security-Policy': headers.get('Content-Security-Policy'),
            'Strict-Transport-Security': headers.get('Strict-Transport-Security'),
            'X-Content-Type-Options': headers.get('X-Content-Type-Options'),
            'X-Frame-Options': headers.get('X-Frame-Options'),
            'X-XSS-Protection': headers.get('X-XSS-Protection'),
            'Referrer-Policy': headers.get('Referrer-Policy')
        }
        
        print(f"Analyzing security headers for {url}\n")
        
        for header, value in security_headers.items():
            if value:
                print(f"{header}: {value}")
            else:
                print(f"{header}: Not present")
    
    except requests.RequestException as e:
        print(f"Error making request to {url}: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to analyze: ")
    analyze_security_headers(url)
