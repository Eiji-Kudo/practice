import sys
from langchain_community.document_loaders import SeleniumURLLoader

def get_content(url):
    if not url:
        return {"error": "URL parameter is required"}, 400

    try:
        # SeleniumURLLoaderを初期化。URLをリストとして渡す。
        loader = SeleniumURLLoader(urls=[url])

        # 指定されたURLからHTMLを取得
        # loadメソッドを引数なしで呼び出す
        html_content = loader.load()

        return {"content": html_content}, 200
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print("Usage: python app.py <URL>")
    #     sys.exit(1)

    # url = sys.argv[1]
    url = "https://ann.inc"
    result, status_code = get_content(url)
    print(f"Status Code: {status_code}\nResult: {result}")