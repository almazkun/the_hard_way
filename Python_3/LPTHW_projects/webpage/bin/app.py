import web


urls = (
    "/", "index"
)


app = web.application(urls, globals())


class Index:
    def Get(self):
        greeting = "Hello world!"
        return greeting


if __name__== "__main__":
    app.run()
    