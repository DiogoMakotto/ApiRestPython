from flask_restful import Resource, reqparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str, required=True, help="URL cannot be blank!")
        args = parser.parse_args(strict=True)

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        try:
            driver.get(args['url'])
            title = driver.title
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            driver.quit()

        return {'title': title}
